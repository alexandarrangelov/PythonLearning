import random

random_num = random.randint(0,2)

if random_num == 0:
	computer_choise = "rock"
	pass
elif random_num == 1:
	computer_choise = "paper"
elif random_num == 2:
	computer_choise = "scissors"


print('...rock...')
print('...paper...')
print('...scissors...')

player1 = input('Player 1 choice : ')
print(f'Computer choise is : {computer_choise}')


if player1=="rock" and computer_choise=="scissors":
	print('Player1 wins!')
	pass
elif player1=="rock" and computer_choise=="paper":
	print('Player2 wins!')
elif player1 == "rock" and computer_choise=="scissors":
	print('Player1 wins!')
elif player1=="paper" and computer_choise=="scissors":
	print('Player2 wins!')
elif player1 == computer_choise:
	print('It is a tie!')
else :
	print('Something went wrong!')



