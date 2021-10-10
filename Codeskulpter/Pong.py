# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
width = 600
height = 400       
ball_radius = 20
pad_width = 8
pad_height = 80
half_pad_width = pad_width / 2
half_pad_height = pad_height / 2
paddle1_pos, paddle2_pos = height // 2, height // 2
paddle1_vel = 0
paddle2_vel = 0
ball_pos = [width // 2, height // 2]
ball_vel = [0, 0]
score1, score2 = 0, 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [width // 2, height // 2]
    if direction == "right":
        ball_vel = [random.randrange(2, 5), -random.randrange(1, 4)]
    elif direction == "left":
        ball_vel = [-random.randrange(2, 5), -random.randrange(1, 4)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = height // 2
    paddle2_pos = height // 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball("left")


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
     
    # draw mid line and gutters
    canvas.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    canvas.draw_line([pad_width, 0],[pad_width, height], 1, "White")
    canvas.draw_line([width - pad_width, 0],[width - pad_width, height], 1, "White")
    
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= ball_radius:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= height - ball_radius:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[0] <= pad_width + ball_radius:
        if paddle1_pos - half_pad_height <= ball_pos[1] <= paddle1_pos + half_pad_height:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score1 += 1

            spawn_ball("right")
    elif ball_pos[0] >= width - pad_width - ball_radius:
        if paddle2_pos - half_pad_height <= ball_pos[1] <= paddle2_pos + half_pad_height:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score2 += 1
            spawn_ball("left")
    # draw ball
    canvas.draw_circle(ball_pos, ball_radius, 1, "Wihte", "White")
    # update paddle's vertical position, keep paddle on the screen
    if not(paddle1_pos + paddle1_vel >= height - half_pad_height or paddle1_pos + paddle1_vel <= 0 + half_pad_height):
        paddle1_pos += paddle1_vel
    if not(paddle2_pos + paddle2_vel >= height - half_pad_height or paddle2_pos + paddle2_vel <= 0 + half_pad_height):
        paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_line([pad_width / 2.0, paddle1_pos - half_pad_height],
                     [pad_width / 2.0, paddle1_pos + half_pad_height], 9, "Wihte")
    canvas.draw_line([width - pad_width // 2, paddle2_pos - half_pad_height],
                     [width - pad_width // 2, paddle2_pos + half_pad_height], 9, "Wihte")   
        
    # draw scores
    canvas.draw_text(str(score1), [width//2 + 100, 50], 50, "red")
    canvas.draw_text(str(score2), [width//2 - 150, 50], 50, "red")    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
