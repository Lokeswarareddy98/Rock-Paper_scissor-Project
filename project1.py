"""
Workflow of the project 
1.input from user=rock,paper,scissor
2.computer choice=radomly
print result
Cases:
A-Rock:
Rock-Rock=Tie
Rock-Paper=Paper win
Rock-scissor=Rock win
B-Paper
paper-paper=tie
paper-rock=paper win
paper-scissor=scissor win
c-scissor
scissor-scissor=tie
scissor-paper=scissor win
scissor rock=rock win
"""
import random
item_list=['Rock','Paper','Scissor']
user_input=input('Enter your choice:')
computer_choice=random.choice(item_list)
print(f'The computer choice {computer_choice}')
#print(f'User_input={user_input} Computer choice={Computer_choice}')
if user_input==computer_choice:
    print("The game tie")
elif user_input=='Rock':
    if computer_choice=='Paper':
        print('The paper covers the rock as the paper wins')
    else:
        print('The Rock breaks the scissors as the Rock wins')
elif user_input=='Paper':
    if computer_choice=='Rock':
        print('The Rock covers the paper as the paer wins')
    else:
        print('Scissor cuts the paper as the scissor wins')
else:
    if computer_choice=='Paper':
        print('The Scissor cuts the paper as the scissor wins ')
    else:
        print('Rock breaks the scissor as the rock wins')






