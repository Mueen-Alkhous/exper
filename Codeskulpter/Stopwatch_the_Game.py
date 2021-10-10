# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter, count1, count2  = 0, 0, 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(counter):
    return str(counter // 600)+":"+  '%02d' % ((counter  % 600)// 10,) +"."+str((counter  % 600) % 10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global count1, count2
    if timer.is_running():
        count1 += 1
        if counter % 10 == 0 and counter > 0:
                count2 += 1
        timer.stop()

def reset():
    global counter, count1, count2
    counter, count1, count2  = 0, 0, 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), (70, 160), 65, 'White')
    canvas.draw_text(str(count2)+"/"+str(count1), (220, 50), 40, 'green')
      
# create frame
frame = simplegui.create_frame("Test", 300, 300)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw)

# start frame
frame.start()

