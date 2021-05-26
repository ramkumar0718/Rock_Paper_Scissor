import random
import time
import sys

hum_score = 0
comp_score = 0

def intro():
    print("Rock Paper Scissor !!!")
	print("Instructions:\n")
	print("Play against the computer and try to win.")
	print("    Win 100 points to beat the computer.")
	print("    Press q to Quit the game.")
intro()

def display_score():
	print("Your score is", hum_score, ".")
	print("Computer score is", comp_score, ".")

def hum_win():
	global hum_score
	print("You Win.")
	hum_score += 10
	display_score()

def comp_win():
	global comp_score
	print("Computer Win.")
	comp_score += 10
	display_score()


while True:
	hum = input("\nType your choice(r, p, s): ").lower()

	if hum == 'r':
		print("Your choice is rock.")
		human = 1

	elif hum == 'p':
		print("Your choice is paper.")
		human = 2

	elif hum == 's':
		print("Your choice is scissor.")
		human = 3

	elif hum == 'q':
		print("exiting...")
		time.sleep(2)
		sys.exit()

	else:
		print("Please type only (r, p, s) or q to quit !")
		continue

	# Computer choice

	comp = random.randint(1, 3)

	if comp == 1:
		print("Computer choice is rock.")

	elif comp == 2:
		print("Computer choice is paper.")

	elif comp == 3:
		print("Computer choice is scissor.")

	# Main Algorithm

	if human == comp:
		print("It is tie.")

	elif human == 1 and comp == 2:
		comp_win()

	elif human == 1 and comp == 3:
		hum_win()

	elif human == 2 and comp == 1:
		hum_win()

	elif human == 2 and comp == 3:
		comp_win()

	elif human == 3 and comp == 1:
		comp_win()

	elif human == 3 and comp == 2:
		hum_win()

	# Checks game end or not

	if hum_score == 100 or comp_score == 100:
		break

# Display Final Score

if hum_score == 100:
	print("\nYou beat the computer !")
	time.sleep(2)
	sys.exit()

if comp_score == 100:
	print("\nYou lost, Computer Wins !")
	time.sleep(2)
	sys.exit()




	