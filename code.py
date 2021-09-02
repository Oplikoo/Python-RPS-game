###Made By Oplikoo
###Have Any Errors? Type it in the errors tab and I will answer them as soon as possible!
###Have fun with the code!
###--------------------------------------------------------------------------------

#Imports the random library(ITS IMPORTANT OR THE WHOLE CODE WILL NOT EVEN RUN!)
import random

#create a list with all the options avilable in the game that the bot can do
game_options = ['scissors' , 'paper' , 'rock']

#its random from the list one option
botchoose = str(random.choice(game_options))

#its get the choose of the user
userchoose = str(input("Lets Play Rps! To choose scissors type scissors, to chhose paper type paper, and to choose rock type rock.(not capital letters) What you choose? "))

#theres all the options can be in the game

#If its a tie
if(userchoose == botchoose):
    print("The bot chose ", userchoose ," too! Its a Tie!")
#all the scissors options(without a tie)
elif(userchoose == "scissors" , botchoose == "paper"):
    print("Your choose : scissors ; The bot choose : paper - You won!")
elif(userchoose == "scissors" , botchoose == "rock"):
    print("Your choose : scissors ; The bot choose : rock - You lose!")
#all the paper options(without a tie)
elif(userchoose == "paper" , botchoose == "rock"):
    print("Your choose : paper ; The bot choose : rock - You won!")
elif(userchoose == "paper" , botchoose == "scissors"):
    print("Your choose : paper ; The bot choose : scissors - You lose!")
#all the rock options(without a tie)
elif(userchoose == "rock" , botchoose == "paper"):
    print("Your choose : rock ; The bot choose : paper - You lose!")
elif(userchoose == "rock" , botchoose == "scissors"):
    print("Your choose : rock ; The bot choose : scissors - You won!")
#------------------------------------------------------------------------------


#And yes that is all the code...
#Not so hard to edit or view
#Like this project? A star in this github project will be amazing(and also will support me to make more github projects)!
