#Rock Paper Scissor Game
import random
import sys
import time

human_score = 0
computer_score = 0
#target_score = 100

print("""Rock Paper Scissor Game
\nGame Instruction:
Play against the computer and try to win
  Win 100 points to beat the computer
  Press q to Quit the game...
""")

#Important steps

while True:

    #For Human 
    human = input("\nYour Choice(r,p,s)").lower()
    if human == 'r':
      print("Your Choice = Rock")
      human_val = 1

    elif human == 'p':
      print("Your Choice = Paper")
      human_val = 2

    elif human == 's':
      print("Your Choice = Scissor")
      human_val = 3

    elif human == 'q':
      print("Quiting the game!")
      time.sleep(1)
      sys.exit(1)

    else:
      print("Only press r,p,s or q to quit the game")
      continue

    #For Computer
    computer_val = random.randint(1,3)
    if computer_val == 1:
      print("Computer\'s Choice = Rock")

    elif computer_val == 2:
      print("Computer\'s Choice = Paper")

    else:
      print("Computer\'s Choice = Scissor")

    #Important Agorthim
    if computer_val == human_val:
      print("It\'s a tie")

    elif computer_val == 1 and human_val == 2:
      print("You Win")
      human_score += 10
      print("Your Score =", human_score)
      print("Computer Score =", computer_score)

    elif computer_val == 1 and human_val == 3:
      print("Computer Win")
      computer_score += 10
      print("Your Score =", human_score)
      print("Computer Score =", computer_score)

    elif computer_val == 2 and human_val == 1:
      print("Computer Win")
      computer_score += 10
      print("Your Score =", human_score)
      print("Computer Score =", computer_score)

    elif computer_val == 2 and human_val == 3:
      print("You Win")
      human_score += 10
      print("Your Score =", human_score)
      print("Computer Score =", computer_score)

    elif computer_val == 3 and human_val == 1:
      print("You Win")
      human_score += 10
      print("Your Score =", human_score)
      print("Computer Score =", computer_score)

    elif computer_val == 3 and human_val == 2:
      print("Computer Win")
      computer_score += 10
      print("Your Score =", human_score)
      print("Computer Score =", computer_score)

    else:
      pass

    #Score
    if human_score == 100 or computer_score == 100:
      break

#Game Winner
if human_score == 100:
  print("\nYou beat the Computer!")
  time.sleep(5)
  sys.exit(1)

elif computer_score == 100:
  print("\nYou lost, Computer Wins!")
  time.sleep(5)
  sys.exit(1)


    
      
      
