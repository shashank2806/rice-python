#!/usr/bin/env python
try:
    import simplegui
except ImportError:  
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
# define global variables
t = 0
s = 0
w = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global deciseconds, seconds
    minutes = t // 600
    seconds = (t % 600) // 10
    deciseconds = (t % 600) % 10
    if seconds < 10:
        return str(minutes) + ":" + "0" + str(seconds) + "." + str(deciseconds)
    else:
        return str(minutes) + ":" + str(seconds) + "." + str(deciseconds)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    global s, w
    if timer.is_running():
        s += 1
    timer.stop()
    if deciseconds == 0 and seconds != 0:
        w += 1
def reset():
    global t, s, w
    t, s, w = 0, 0, 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t),[70,105], 25, "Yellow    ")
    canvas.draw_text(str(w) + "/" + str(s), [150,20], 20, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
# start frame
frame.start()

# Please remember to review the grading rubric
