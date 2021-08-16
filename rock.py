import sys
import random
user1_ans=input("do u want to chosse rock paper scissor : " )
#user2_ans=input("%s do u want to chosse rock paper scissor"  %user2)
comp=random.choice(['rock','paper','scissor'])
def fun(user1,user2):
	if user1==comp:
		print("its a tie bro")
	elif user1=="rock":
		if comp=="scissor":
			print("computer is choosen scissor")
			return("rock wins!")
		else:
			return("paper wins")
	elif user1=="scissor":
		if comp=="paper":
			print("computer is choosen paper")
			return("scissor wins!")
		else:
			print("rock win!")
	elif user1=="scissor":
		if comp=="rock":
			print("computer is choosen rock")
			return("rock wins!")
		else:
			print("paper wins!")
	elif user1=="paper":
		if comp=="rock":
			print("computer is choosen rock")
			return("paper win!")
		else:
			print("scissor wins!")
	else:
			print("ivalid input")
			sys.exit
print(fun(user1_ans,comp))	
	
