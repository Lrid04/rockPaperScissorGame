from random import randrange

class BackEnd:

    def __init__(self):
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.options = [1, 2, 3]
        self.player_choice = player_choice
        self.computer_choice = computer_choice
    
    def pick_option(self):
        if self.options == 1:
            self.player_choice = "Rock"
        elif self.options == 2:
            self.player_choice = "Paper"
        else:
            self.player_choice = "Scissors"

    def computer_option(self):
        computer_picked = randrange(1, 3)
        if computer_picked == 1:
            self.computer_choice = "Rock"
        elif computer_picked == 2:
            self.computer_choice = "Paper"
        else:
            self.computer_choice = "Scissors"

    def rock_paper_scissors(player_choice, computer_choice, total_player_wins, total_computer_wins):
        if player_choice == computer_choice:
            return "Tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "scissors" and computer_choice == "paper") or \
                (player_choice == "paper" and computer_choice == "rock"):
            total_player_wins += 1
            return "You win!"
        else:
            total_computer_wins += 1
            return "Computer wins!"

    