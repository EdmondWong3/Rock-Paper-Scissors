import random, sys

player_score = 0
opponent_score = 0

input_converter = {
    "ROCK" : """
     ______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)
    """,

    "PAPER" : """
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)
    """,

    "SCISSORS" : """
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)
    """,

    "1" : """
    ______
 (____   '---
(_____)      
(_____)      
 (____)      
  (___)__.---  
    """,

    "2" : """
        _______
   ____(____   '---
  (______          
(_______          
  (_______         
    (__________.---
    """,
    
    "3" : """
       _______
  ____(____   '---
 (______          
(__________       
      (____)      
       (___)__.---
    """
}

class Opponent:
    def __init__(self):
        pass
    

    def opponent_action(self):
        opponent_input = str(random.randint(1,3))
        return opponent_input


class Player:
    def __init__(self):
        pass
    

    def player_action(self):
        while True:
            player_input = input("What's the game plan?: Rock Paper Scissors > ").upper()
            if player_input not in ("ROCK", "PAPER", "SCISSORS"):
                print("You entered an invalid character. Please try again and type one of the following: 'Rock' 'Paper' 'Scissors'")
            else:
                break
        return player_input


def victory_defeat_check():
    print(f"Player's Score: {player_score}  Opponent's Score: {opponent_score}")
    if player_score == 3:
        sys.exit("You got to 3 points before your opponent. Congrats for winning!")
    elif opponent_score == 3:
        sys.exit("Your opponent got to 3 points before you. Sorry, better luck next time!")


def play_game():
    print("""Welcome to Edmond's Rock Paper Scissors Game
    
    Classic Rules:
        1. Rock beats Scissors
        2. Paper beats Rock
        3. Scissors beats Paper
    
    First to 3 points wins. Good luck!
    """)
    player = Player()
    opponent = Opponent()
    global player_score
    global opponent_score
    while True:
        player_action = player.player_action()
        print(f"Player: {input_converter[player_action]}")
        opponent_action = opponent.opponent_action()
        print(f"Opponent: {input_converter[opponent_action]}")
        if player_action == "ROCK" and opponent_action == "1":
            print("You TIE!")
            victory_defeat_check()
        elif player_action == "ROCK" and opponent_action == "2":
            print("You LOSE!")
            opponent_score += 1
            victory_defeat_check()
        elif player_action == "ROCK" and opponent_action == "3":
            print("You WIN!")
            player_score += 1
            victory_defeat_check()
        elif player_action == "PAPER" and opponent_action == "1":
            print("You WIN!")
            player_score += 1
            victory_defeat_check()
        elif player_action == "PAPER" and opponent_action == "2":
            print("You TIE!")
            victory_defeat_check()
        elif player_action == "PAPER" and opponent_action == "3":
            print("You LOSE!")
            opponent_score += 1
            victory_defeat_check()
        elif player_action == "SCISSORS" and opponent_action == "1":
            print("You LOSE!")
            opponent_score += 1
            victory_defeat_check()
        elif player_action == "SCISSORS" and opponent_action == "2":
            print("You WIN!")
            player_score += 1
            victory_defeat_check()
        elif player_action == "SCISSORS" and opponent_action == "3":
            print("You TIE!")
            victory_defeat_check()


if __name__ == "__main__":
    play_game()




