# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    #pass==null statement in python
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        print "please enter correct choice"

    


def number_to_name(number):
   
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Bad Choice"
   

def rpsls(player_choice): 
    comp_choice=random.randrange(0,5)
    player_choice=name_to_number(player_choice)
    print "Player choose",number_to_name(player_choice)
    print "Computer choose",number_to_name(comp_choice)
    
    if (player_choice - comp_choice)%5==1 or (player_choice - comp_choice)%5==2:
        print "Player wins!\n"
    elif (player_choice - comp_choice)%5==3 or (player_choice - comp_choice)%5==4:
        print "Computer wins!\n"
    else:
        print "Player and computer tie!\n"
        
   

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


