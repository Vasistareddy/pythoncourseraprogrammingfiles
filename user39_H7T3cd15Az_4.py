# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

global secret_number
num_range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global i
    global num_range
    secret_number = random.randrange(0,num_range)
    low = 0
    high = num_range
    i = int(math.ceil((math.log((high-low+1),10) / math.log(2,10))))
    print "New game. Range is from 0 to", num_range
    print "Number of guesses remaining is", i
    print " "
   
    


# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()

def range1000():
    global num_range
    num_range = 1000
    new_game()
            
def input_guess(guess):
    global i
    guess = int(guess)
    print 'Guess was', guess
    i = i - 1
    print 'Number of remaining guesses is' , i
    if (secret_number > guess) and i > 0:
        print "Higher!\n"
        
    elif secret_number < guess and i > 0:
        print "Lower\n"
        
    elif secret_number == guess and i >= 0:
        print "Correct!\n"
        new_game()
        
    else:
        print "You ran out of guesses." + " " + "The number was ", secret_number
        print " "
        new_game()
    

frame = simplegui.create_frame("Guess the number", 300, 300)
button1 = frame.add_button("Range is [0-100)", range100, 150)
button2 = frame.add_button("Range is [0-1000)", range1000, 150)
label = frame.add_input("Enter a guess", input_guess, 150)
new_game()
frame.start()
