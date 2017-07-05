# implementation of card game - Memory
try:
	import simplegui
except ImportError:
	import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


import random

# list of numbers
l1 = [0,1,2,3,4,5,6,7]
l2 = [0,1,2,3,4,5,6,7]
DECK = l1 + l2

# helper function to initialize globals
def new_game():
    global state, exposed, index1, index2, counter
    index1 = 0 # index of first card exposed
    index2 = 0 # index of second card exposed
    state = 0
    counter = 0
    # card is exposed or not.
    exposed = [False, False, False, False, False, False, False, 
          False, False, False, False, False, False, False, 
          False, False]
    random.shuffle(DECK)
    

     
# define event handlers
def mouseclick(pos):
    global state, index1, index2, counter
    i = pos[0] // 50 # index of card clicked
    if exposed[i] == False: # Clicking on exposed card does nothing.
        exposed[i] = True # expose cards
        if state == 0:
            counter += 1
            index1 = i # store index of card
            state = 1
        elif state == 1:
            index2 = i
            state = 2
        else:
        	# if previous two exposed are not equal, flip them.
            if DECK[index1] != DECK[index2]:
                exposed[index1] = False
                exposed[index2] = False
            counter += 1
            index1 = i
            state = 1

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for index in range(len(DECK)):
        if exposed[index]:
            canvas.draw_text(str(DECK[index]), [index * 50 + 10, 65], 40, 'White')
        else:
            canvas.draw_line([index * 50 + 25, 0], [index * 50 + 25, 100], 48, 'Green')
    label.set_text("Turn = " + str(counter))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()