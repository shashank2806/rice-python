# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global count
    global num_range
    if num_range == 100:
        count = 7
    else:
        count = 10
    print ""
    print "New Game, Range is [0,"+ str(num_range) + ")"
    secret_number = random.randrange(0,num_range)
    print "Number of remaining guesses are " + str(count)
    print ""


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    global secret_number
    secret_number = random.randrange(0,num_range)
    new_game()
    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    global secret_number
    secret_number = random.randrange(0,num_range)
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global count
    count -= 1
    print "Guess was " + guess
    guess = int(guess)
    if count == 0 and secret_number != guess:
        print "You ran out guesses, The number was " + str(secret_number)
        print
        new_game()
    elif secret_number < guess:
        print "Lower!"
        print "Number of remaining guesses are " + str(count)
        print ""
    elif secret_number > guess:
        print "Higher!"
        print "Number of remaining guesses are " + str(count)
        print ""
    else:
        print "Correct!"
        print "Number of remaining guesses are " + str(count)
        new_game()
    
    
    
    

    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_input("Guess",input_guess,50)
frame.add_button("Range is [0,100)",range100)
frame.add_button("Range is [0,1000)",range1000)

# call new_game 
new_game()



# always remember to check your completed program against the grading rubric
