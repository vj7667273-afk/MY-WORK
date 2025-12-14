import random

player1 = input("Select rock,paper,or scissor:").lower()
player2 = random.choice(["ROCK","PAPER","SCISSOR"]).lower()
print("player 2 selected:",player2)

if player1 =="ROCK"and player2 =="PAPER":
    print("player2 won")

elif player1 =="PAPER"and player2 =="SCISSOR":
   print("player2 won")
elif player1 =="SCISSOR"and player2 =="ROCK":
   print("player2 won")
elif player1 == player2:
   print("Tie")
else :
   print("player1 won")