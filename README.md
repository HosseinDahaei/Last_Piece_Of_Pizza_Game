![pexels-maksim-goncharenok-4773769](https://user-images.githubusercontent.com/47916989/229536012-146cdbb2-c86e-44a9-b5d4-222004729870.jpg)
# Last Piece Of Pizza Game

When I was 16 years old and I had started programming with C language for the computer student Olympiad, I was solving many classic questions. I happened to see some of my codes a few days ago and I decided to rewrite some of them. These code models and solves a very simple game that is related to the topic of game theory.

# Rules:

The game starts with two people eating pizza At the beginning of the game, they decide to divide this pizza into N pieces and agree to eat some pieces from this pizza, which is at least 1, and at most M, which is a set value. The winner is the one who can eat the last piece of pizza.

The purpose of the program is to play with you and be able to win 100%. In the way that it allows you to choose the value of N, M instead it chooses who will start the game first.

# How does it work?

Considering that the movements of the players are completely equal, we say that the game is fair and that whether a player wins or loses depends only on the current state of the game. Now we think about solvable and small situations.

We know that if there is no pizza pieces left, the person whose turn it is is a loser. So for the status 0, the loss is certain. The goal of each player is that the opposite player is the loser, so if the number of pizza pieces is smaller than or equal to M, the player eats all the pieces until the opposite player reaches zero and becomes a loser. If with just one move we can reach the losing situation, it will be the winning situation. According to this rule, we make an Array and fill it from the beginning, according to which we can decide whether to start the game or not, and also with Moving from the win state to the loss state, we defeat the opponent player 100%.


# Prerequisites:
You just should install colorama package:

    pip install colorama

