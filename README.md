  # ESCAPE ROOM GAME
  ## Video Demo:  <URL HERE>
  ## Description
  My project is a simple escape room-type game with random player and key position generation as well as 
  variable room size.
  It incorporates the use of classes, libraries, docstrings and console interaction.
  



  ### How to play
  Open a terminal application and navigate to this projects root folder.
  If you are using Windows 10 or Linux this can be done by right-clicking in this directory and 
  selecting "open in terminal".

  Now enter the following command:
  `python project.py [-x] [N] [-y] [y]`
  where `-x N` and `-y N` are optional arguments which you can give to specify the game area size. 
  If you want this, simply replace "N" with a number between 4 and 30 for each, 
  ending up with something like `python project.py -x 25 -y 15` for instance.

  If you want to quit the game at any point, simply press the escape-key.




  ### Project Files
  Before you read each of these, there is also a more comprehensive description you can find in the documentation.
  
  #### __project.py__
  This is the main project file.
  This file handles the instansiation of the game world and includes the game logic itself.
  It contains the following functions:

  __main():__\
  This is the main function of the project.
  It prints a short welcome message for the player explaining what to do, then it executes the `get_args()`, 
  `initialize_game()` and `run()` functions to initialize and start the game.

  __initialize_game():__\
  This function creates an object of the World class, then draws the game in the terminal by calling `draw_game()` 
  once and then returns the world object.\
  It takes one argument, `args`, that is of the type argparse.Namespace which contains both command-line arguments.

  __game_win():__\
  This gets called when the `world.has_won`-flag is set to `True`.\
  It simply prints a message congratulating the player and exits the game.

  __get_args():__\
  This uses the argparser library to check for command-line arguments and then returns those as an object of 
  argparse.Namespace .\
  To note here is that the user can pass two arguments, x and y (both have to be integers), to the program
  which then determine the size of the play area when initializing the Wold object.\
  Both of these arguments are completely optional, as the program defaults to a value of 10 for both values.
  The minimum and maximum values for both x and y are 4 and 30 respectively.

  __run():__\
  This function takes one argument, `world`, which is an object of the World class.
  It then creates an instance of the `keyboard.Listener` from the `pynput` library.\
  This listener waits for a key press of any of the directional arrow-keys and then calls `player_movement()`
  via a lambda function. I chose to use this in order to be able to pass not just the pressed key to the called function,
  but also the World object.\
  This function is also responsible for keeping the game running, because the keyboard listener works on a seperate
  thread (according to the pynput documentation).\
  There is no call for `listener.stop()` because it gets stopped when `game_win()` gets called anyway.

  __draw_game():__\
  The `draw_game()` function takes one World object as an argument, in order to be able to access the play area.
  It first calls `clear_console()` and then enters a for-loop to go through each row of the play area (`world.tilemap`)
  and join it together, then print that string.\
  Finally it checks if the `world.has_won` flag has been set to `True` and if so it calls `game_win()`.

  __player_movement():__\
  This is the function that handles all key presses and the resulting changes to the play area array.\
  It takes two arguments, `key` of the type `keyboard.Key` and `world` which is a World object.\
  The first step here is that the current location of the player get set to the floor character, as the player will be moved off of it.
  Then the `key` is matched to which key was pressed, and then the corresponding logic is executed.

  This logic checks if there is a wall in the direction the player wants to move, if there is a door and if they have the key.
  Depending on which of these is true or false the player position in the relevant directions variable is changed by 1 or -1,
  if the player stepped onto the key then `world.has_key` is set to `True` and if the player has
  reached the door while having aquired the key, the `world.has_won` flag gets set to `True`.

  Finally, the player position is updated using the changed data and then `draw_game()` is called to update the terminal with the
  changed values.


  __clear_console():__\
  This function has a check for which operating system the user is on and clears the terminal accordingly.
  Note: this was only tested on Windows 11, as i do not own a device running Linux or MacOS.

  #### __world.py__
  This is the World class, containing the initialization of the game area and stores the key and player locations as well as
  the flags for the win condition and whether or not the player has collected the key.
  It also contains the following methods:

  __ __init__()__\
  This checks if the provided x and y size is within the defined bounds of 4-30 and assigns the values to their variables.
  It creates a 2d-array using `numpy` with the specified x and y size
  to contain the game area and the characters corresponding to whatever is in each of the locations.\
  Finally it calls all of the four generation methods to fill the game area with its contents.

  __generate_walls()__\
  This method goes along the game areas outer bouds and places a character corresponding to a wall in each of the locations.

  __generate_door()__\
  Firstly, a random direction out of the 4 possible is generated to determine on what wall the door will be placed on.
  Then the character corresponding to the door is placed in a random location along that wall, excluding the corners.

  __generate_key()__\
  This method sets the key character somewhere in the valid play area (within the walls) by accessing `self.key_x` and `self.key_y`
  which were previously randomly determined.

  __generate_player()__\
  This generates a random position for the player inside the viable game area and then checks if the generated location is already
  occupied by the key character. If this is the case, the method simply calls itself again.
  If not, the player character (currently an "A") is placed here.

  #### __test_project.py__
  This is the file executed by pytest which tests all functions and methods within `project.py` and `world.py` that can be tested.
  An explanation of each test follows:

  __test_initialize_game()__\
  This checks that the return type from `initialize_game()` is an object of the type World.
  To note in this test is that i created a `namedtuple` to pass to the function, because it accesses the command-line arguments
  with `args.x` and `args.y`.

  __test_game_win()__\
  Simply checks if the function raises a `SystemExit` exception.

  __test_get_args__\
  The only test i can actually do here is, if the function raises a `SystemExit` exception. This is due to the fact that i
  specified in `get_args()` that both arguments need to be an `int`, but pytest launches with a `str`.

  __test_draw_game__\
  Checks that the function returns `0`, meaning it executed successfully.

  __test_clear_console()__\
  Same as `test_draw_game()`, there is just no way to test if the terminal has been cleared.

  Now follow the tests for the World class:

  __test_world_generate_walls()__\
  Checks if the function exits with code `0`, if the top left location in the game area is a wall character,
  and that the location [2,2] is an empty space (" ") or the key character.

  __test_world_generate_door__\
  Checks that the method exited with code `0`

  __test_world_generate_key__\
  Validates that the generated key location contains the key character, not " "

__test_world_generate_player()__\
Asserts that the method exited with code `0` and that the player location contains the "A" representing the player.
