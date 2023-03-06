import random
from winner import Winner
from looser import Looser
from point_tracking import PointTracking


class RPSGame:

  def __init__(self, num_rounds=7, win_threshold=2):
    self.num_rounds = num_rounds
    self.win_threshold = win_threshold
    self.num_wins = 0
    self.num_losses = 0
    self.round_count = 1
    self.winner = Winner()
    self.looser = Looser()
    self.point_tracking = PointTracking()

  def get_user_choice(self):
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
      print("Invalid choice. Please try again.")
      user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

  def get_computer_choice(self):
    return random.choice(["rock", "paper", "scissors"])

  def determine_winner(self, user_choice, computer_choice):
    if user_choice == computer_choice:
      return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
      self.point_tracking.user_win()
      return "user"
    else:
      self.point_tracking.computer_win()
      return "computer"

  def display_scores(self):
    self.point_tracking.display_score()

  def display_motivational_message(self):
    if self.num_wins >= self.win_threshold:
      self.winner.display_message()
    elif self.num_losses >= self.win_threshold:
      self.looser.display_message()

  def display_final_result(self):
    self.point_tracking.display_score()
    self.point_tracking.display_final_result()

  def play_game(self):
    print("Let's play Rock, Paper, Scissors!")
    while self.round_count <= self.num_rounds:
      print(f"\nRound {self.round_count}:")
      user_choice = self.get_user_choice()
      computer_choice = self.get_computer_choice()
      print(
        f"You chose {user_choice}, and the computer chose {computer_choice}.")
      winner = self.determine_winner(user_choice, computer_choice)
      if winner == "user":
        print("You win this round!")
        self.num_wins += 1
      elif winner == "computer":
        print("The computer wins this round.")
        self.num_losses += 1
      else:
        print("It's a tie!")
      self.display_scores()
      self.display_motivational_message()
      self.round_count += 1
    print("\nGame over!")
    self.display_final_result()
