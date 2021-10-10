# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100

# helper function to start and restart the game

def new_game():
    global secret_num
    global num_of_guesses
    num_of_guesses = int(math.ceil(math.log(num_range, 2)))
    secret_num = random.randrange(0, num_range)
    print "New game. Range from 0 to", num_range
    print "Number of remaining guesses is", num_of_guesses
    print "\n"

# handler for the buttons function

def range100():
    global num_range
    global secret_num
    num_range = 100
    new_game()

def range1000():
    global num_range
    global secret_num
    num_range = 1000
    new_game()
    
def input_guess(guess):
    global secret_num
    global num_range
    global num_of_guesses
    guess = int(guess)
    print "Guess was", guess
    num_of_guesses -= 1
    print "Number of remaining guesses is", num_of_guesses
    if guess == secret_num:
        print "Correct!"
        print "\n"
        new_game()
    elif num_of_guesses == 0:
        print "You ran out of guesses. The number was", secret_num
        print "\n"
        new_game()
    elif  guess > secret_num:
        print "Lower!"
    elif guess < secret_num:
        print "Higher!"
   
   
    print "\n"



    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [ 0 , 100 )", range100, 200)
frame.add_button("Range is [ 0 , 1000 )", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

frame.start()

