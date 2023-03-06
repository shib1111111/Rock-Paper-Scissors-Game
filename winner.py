import random

class Winner:
    def __init__(self):
        self.winning_messages = [
            "You can do it!",
            "Believe in yourself!",
            "Go get 'em tiger!",
            "Success is just around the corner!",
            "You are doing great!",
            "Awesome! Keep it up!",
            "You're a Rockstar!"
        ]

    def display_message(self):
        print(random.choice(self.winning_messages))
