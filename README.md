# games

## TikTakToe

This is an implementation of the game TikTakToe to play in the commandline. <br>
There are two settings: You can either play against an opponent, or you can play aganist a bot that takes random positions.
This game has to be played until all positions are filled and will not recognize a draw in advance.
<br>
The class TikTakToe represents one game. The class has several methods to work. The class variables include the tiktaktoe field, list that stores all valid moves made, 
a status which works as a flag, move_command which stores the current move made and winner which stores the winner of the game.

Apart from dundermethods there is:
  - __init__() decides randomly on initializsation which player beginns
  - check_input() : This cleans user input and controlls if the input is valid
  - next_move(): This funktion sets the next move and changes the field. If the position is already taken it warns the user
  - get_status(): This checks if one player achieved 3 in a row and changes a class variable
  - get_turn(): checks which player is next
  - get_winner(): this looks if someone has scored 3 in a row or if there is a draw and notifies the console.
  - get_bot_move(): this method filters all possible positions and lets a bot randomly choose one of them. 
  - get_move(): this method takes in user input or calls get_bot_move depending on whos turn it is. 
  - make_move(): This combines the methods next_move() and get_status() to see if a user has won the game
  - run_game(): this initializes the game
  
  - main(): this takes in the first user input
  
