import random
a=['r','p','s']
z=0
r=0
while (True):
	p=input("your choice r/p/s: ")
	c=random.choice(a)

	print("you chose ",p, "computer chose ",c)
	if(p=='r' or p=='p' or p=="s"):
		if (p=='c'):
			print("its a tie")
		elif((p=='r' and c=='p') or (p=='p' or c=='s')):
			z=z+1
			print("computer won",z, "times")
		else:
			z=r+1
			print("you won," ,r, "times")
	else:
		print("give proper inputs")
		break
	if(z==3 or r==3):
		if (z==3):
			print("im sorry ,computer has won the game")
	else:
			print("congrats you won against computer , have a great day")