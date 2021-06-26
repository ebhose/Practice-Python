#!/usr/bin/env python3



game = input("Do you want to play (q to exit): ")

while game != 'q':
    player_1 = input("Player 1 choice: ")
    player_2 = input("Player 2 choice: ")

    if (player_1 == 'rock' and player_2 == 'scissors') or \
       (player_1 == 'scissors' and player_2 == 'paper') or \
       (player_1 == 'paper' and player_2 == 'rock'):
           print("Player 1 wins!!")

    elif (player_2 == 'rock' and player_1 == 'scissors') or \
       (player_2 == 'scissors' and player_1 == 'paper') or \
       (player_2 == 'paper' and player_1 == 'rock'):
           print("Player 2 wins!!")

    elif player_1 == player_2:
        print("It's a draw!!")

    else:
        print("Invalid options")

    game = input("Do you want to play again (q to exit): ")

