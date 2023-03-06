# Rock-Paper-Scissors-Game
This is a Python implementation of the classic game of rock-paper-scissors. The game can be played between a user and a computer. The user can choose rock, paper, or scissors, and the computer will randomly select one of these options. The winner of each round is determined by the rules of the game: rock beats scissors, scissors beats paper, and paper beats rock. The game ends after 7 rounds, and the player with the most points at the end of the game is declared the winner.

## Installation:

To run this game, you must have Python 3 installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

## Usage:

To start the game, run the main.py file in your terminal:

Follow the instructions on the screen to play the game. You will be prompted to enter your choice of rock, paper, or scissors, and the computer's choice will be displayed on the screen. The winner of each round will be announced, and the scores will be displayed after each round. At the end of the game, the winner will be announced.

## Features:
➢ The game can be played between a user and a computer.
➢ The user can choose rock, paper, or scissors.
➢ The computer's choice is randomly selected.
➢ The winner of each round is determined by the rules of the game and for each win ,
winner gets 1 Point.
➢ The game ends after 7 rounds.
➢ After every round , score of user & computer will be displayed.
➢ If the user wins repeatedly , the computer will start to compliment the user
➢ If the user loses persistently, the computer will start to motivate the user
➢ The player with the most points at the end of the game is declared the winner.

## File Structure:

#### game.py: 
Contains the Game class, which implements the logic for the rock-paper-scissors game
#### winner.py: 
Contains the Winner class, which is responsible for displaying acompliment message when the user repeatedly wins the game.
#### looser.py: 
Contains the Looser class, which is responsible for displaying a motivational quotes when the user persistently loses the game.
#### motivation_quotes.py: 
Contains the MotivationQuotes class, which is responsible for displaying motivational quotes during the game
#### point_tracking.py: 
Contains the PointTracking class, which is responsible for keeping track of the user and computer's scores, displaying the final score and result status like who wins, who loses, or Tie.
#### main.py: 
Contains the main function, which creates an instance of the RPSGame class and starts the game.
#### README.md: 
Contains information about the rock-paper-scissors game and instructions on how to use it



## Contributing:
Contributions to this project are welcome. If you find a bug or want to suggest a new feature, please create a new issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
