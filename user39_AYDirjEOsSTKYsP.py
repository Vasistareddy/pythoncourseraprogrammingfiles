# Implementation of classic arcade game Pong

import simplegui
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
paddle1_pos = [(HEIGHT/2-HALF_PAD_HEIGHT),(HEIGHT/2-HALF_PAD_HEIGHT),(HEIGHT/2+HALF_PAD_HEIGHT),(HEIGHT/2+HALF_PAD_HEIGHT)]
paddle2_pos = [(HEIGHT/2-HALF_PAD_HEIGHT),(HEIGHT/2-HALF_PAD_HEIGHT),(HEIGHT/2+HALF_PAD_HEIGHT),(HEIGHT/2+HALF_PAD_HEIGHT)]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, paddle1_vel, paddle2_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2 , HEIGHT/2]
    ball_vel = [random.randrange(120, 240)/60, random.randrange(60, 180)/60]
    
    if direction == "Right":
        ball_vel[1] = - ball_vel[1]
    if direction == "Left":
        ball_vel[1] = - ball_vel[1]
        ball_vel[0] = - ball_vel[0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1, score2 = 0,0
    spawn_ball("Left")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1), (WIDTH/2 - 100, 50), 50, 'Green')
    canvas.draw_text(str(score2), (WIDTH/2 + 100, 50), 50, 'Green')
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= HEIGHT-BALL_RADIUS:#bottom floor
        ball_vel[1] = -(ball_vel[1])
    if ball_pos[0] >= WIDTH-(BALL_RADIUS + PAD_WIDTH):#Right wall
        ball_vel[0] = -(ball_vel[0])
    if ball_pos[1] < BALL_RADIUS: #top roof
        ball_vel[1] = -(ball_vel[1])
    if ball_pos[0] < BALL_RADIUS+PAD_WIDTH:
        ball_vel[0] = -(ball_vel[0])
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 10, 'Yellow', 'Orange')
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos[0]],[PAD_WIDTH,paddle1_pos[1]],[PAD_WIDTH,paddle1_pos[2]],[0,paddle1_pos[3]]], 1, 'White')
    canvas.draw_polygon([[WIDTH-PAD_WIDTH,paddle2_pos[0]],[WIDTH,paddle2_pos[1]],[WIDTH,paddle2_pos[2]],[WIDTH-PAD_WIDTH,paddle2_pos[3]]], 1, 'White')
    # determine whether paddle and ball collide
    
    if ball_pos[0] - BALL_RADIUS <=20 and ball_pos[1] in range(paddle1_pos[1],paddle1_pos[2]):
        ball_vel[0]=ball_vel[0]+(0.10 * ball_vel[0])
        #pass
    elif ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        spawn_ball("Right")
        score2 = score2+1
    if (WIDTH-PAD_WIDTH)-ball_pos[0] <=20 and ball_pos[1] in range(paddle2_pos[1], paddle2_pos[2]):
        ball_vel[0]=ball_vel[0]+(0.10 * ball_vel[0])
        #pass
    elif ball_pos[0]>=(WIDTH-PAD_WIDTH)-BALL_RADIUS:
        spawn_ball("Left")
        score1 = score1+1
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel, paddle2_vel = 50, 50
    if paddle1_pos[2] <= HEIGHT:
        if key == simplegui.KEY_MAP["s"]:
            paddle1_pos[0] += paddle1_vel
            paddle1_pos[1] += paddle1_vel
            paddle1_pos[2] += paddle1_vel
            paddle1_pos[3] += paddle1_vel
    if paddle2_pos[2] <=HEIGHT:
        if key == simplegui.KEY_MAP["down"]:
            paddle2_pos[0] += paddle2_vel
            paddle2_pos[1] += paddle2_vel
            paddle2_pos[2] += paddle2_vel
            paddle2_pos[3] += paddle2_vel
        
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if paddle1_pos[0] >= 0:
        if key == simplegui.KEY_MAP["w"]:
            paddle1_pos[0] -= paddle1_vel
            paddle1_pos[1] -= paddle1_vel
            paddle1_pos[2] -= paddle1_vel
            paddle1_pos[3] -= paddle1_vel
    if paddle2_pos[0] >=0:
        if key == simplegui.KEY_MAP["up"]:
            paddle2_pos[0] -= paddle2_vel
            paddle2_pos[1] -= paddle2_vel
            paddle2_pos[2] -= paddle2_vel
            paddle2_pos[3] -= paddle2_vel

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()
