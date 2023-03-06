
import random 
class Looser:
    def __init__(self):
        self.losing_messages = [
            "Failure is the key to success!",
            "Don't watch the clock; do what it does. Keep going.",
            "You have the courage and power to achieve greatness.",
            "Don't give up! You can still do this!",
            "You are better than this! Keep trying!",
        ]

    def display_message(self):
        print(random.choice(self.losing_messages))