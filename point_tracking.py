class PointTracking:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def user_win(self):
        self.user_score += 1

    def computer_win(self):
        self.computer_score += 1
      
    def display_score(self):
      print(f"User: {self.user_score} | Computer: {self.computer_score}")

    def display_final_result(self):
        if self.user_score > self.computer_score:
            print("\nCongratulations! You won the game!")
        elif self.user_score < self.computer_score:
            print("\nSorry, you lost the game.")
        else:
            print("\nThe game ended in a tie.")

    