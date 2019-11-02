
print('...rock...')
print('...paper...')
print('...scissors...')

player1 = input('(Player 1 choice : )')
#Anti cheat system
print('>>>No Cheating<<<\n'*100)

player2 = input('(Player 2 choice : )')


if player1=="rock" and player2=="scissors":
	print('Player1 wins!')
	pass
elif player1=="rock" and player2=="paper":
	print('Player2 wins!')
elif player1 == "rock" and player2=="scissors":
	print('Player1 wins!')
elif player1=="paper" and player2=="scissors":
	print('Player2 wins!')
elif player1 == player2:
	print('It is a tie!')
else :
	print('Something went wrong!')



