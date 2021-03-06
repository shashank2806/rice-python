# Implementation of classic arcade game Pong

try:
    import simplegui
except ImportError:  
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0 

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120/60, 240/60), -random.randrange(60/60, 180/60)]
    else:
        ball_vel = [-random.randrange(120/60, 240/60), -random.randrange(60/60, 180/60)]
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
       
    # draw mid line and gutters
    canvas.draw_text(str(score1), (230, 60), 50, 'White')
    canvas.draw_text(str(score2), (330, 60), 50, 'White')
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White") 
    
    # update ball
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS) or ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    #gutter collision
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS) and ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0]
        #increase ball velocity bu 10%
        ball_vel[0] += 0.1 * ball_vel[0]
        ball_vel[1] += 0.1 * ball_vel[1]
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS) and ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] += 0.1 * ball_vel[0]
        ball_vel[1] += 0.1 * ball_vel[1]
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        score1 += 1
        spawn_ball(LEFT)
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)
       

        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw paddles
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if paddle1_pos <= HALF_PAD_HEIGHT: 
        paddle1_pos = HALF_PAD_HEIGHT
    if paddle1_pos >= (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos = (HEIGHT - HALF_PAD_HEIGHT)
     
    paddle2_pos += paddle2_vel
    if paddle2_pos <= HALF_PAD_HEIGHT: 
        paddle2_pos = HALF_PAD_HEIGHT
    if paddle2_pos >= (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos = (HEIGHT - HALF_PAD_HEIGHT)   
    

    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if simplegui.KEY_MAP["down"] == key:
        paddle2_vel = 5
    if simplegui.KEY_MAP["up"] == key:
        paddle2_vel = -5
    if simplegui.KEY_MAP["s"] == key:
        paddle1_vel = 5
    if simplegui.KEY_MAP["w"] == key:
        paddle1_vel = -5

def keyup(key):
    global paddle1_vel, paddle2_vel
    if simplegui.KEY_MAP["down"] == key:
        paddle2_vel = 0
    if simplegui.KEY_MAP["up"] == key:
        paddle2_vel = 0
    if simplegui.KEY_MAP["s"] == key:
        paddle1_vel = 0
    if simplegui.KEY_MAP["w"] == key:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
new_game()
frame.start()
