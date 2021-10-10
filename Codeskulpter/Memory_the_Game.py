# implementation of card game - Memory

import simplegui
import random
# helper function to initialize globals
def new_game():
    global deck_of_card, exposed, state, turns
    turns = 0
    label.set_text("Turns = " + str(turns))
    state = 0
    deck_of_card = range(8) * 2
    random.shuffle(deck_of_card)
    exposed = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]

# define event handlers
def mouseclick(pos):
    global exposed, state, first_card, second_card, x, y, turns
        
    for num in range(len(deck_of_card)):
        num_pos = 50*num
        if num_pos < pos[0] < num_pos + 50:
            if exposed[num] == False:
                exposed[num] = True
                if state == 0:
                    x = num
                    first_card = deck_of_card[x]
                    state = 1
                elif state == 1:
                    y = num
                    second_card = deck_of_card[y]
                    state = 2
                    turns += 1
                    label.set_text("Turns = " + str(turns))
                else:
                    if first_card != second_card:
                        exposed[x], exposed[y] = False, False
                    x = num
                    first_card = deck_of_card[x]
                    state = 1
            
def draw(canvas):
    for num in range(len(deck_of_card)):
        num_pos = 50*num
        if exposed[num] == True:
            canvas.draw_text(str(deck_of_card[num]), [num_pos + 18, 60], 25, "White")
        else:
            canvas.draw_polygon([[num_pos, 0], [num_pos+50, 0], [num_pos+50, 100], [num_pos, 100]], 5, "Teal", "Navy")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = ")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric