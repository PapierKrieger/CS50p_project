import argparse
from os import system, name as sys_name
import sys
from pynput import keyboard
import world as w


def main():
    print("=== WELCOME TO THIS SHORT ESCAPE ROOM ===")
    print("Goal: collect the key and get to the exit...")

    args = get_args()
    world = initialize_game(args)
    run(world)


def initialize_game(args):
   """
    Creates an instance of the game world and draws it for the first time

   :param args: The given command-line arguments
   :type args: argparse.Namespace
   :return: The game world
   :rtype: World
   """
   world = w.World(args.x, args.y)
   draw_game(world)
   return world

def game_win():
    """
    Handles the win condition

    :raise SystemExit: If the game is over
    """
    print("Congratulations! You won!")
    sys.exit("--A short game by Malte Bodenbach--")


def get_args():
    """
    Gets the provided command-line arguments\n
    2 arguments are possible, both are optional

    :return: The command-line arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="A simple escape room game")
    parser.add_argument("-x", type=int, nargs="?", default=10, help="X coordinate as integer")
    parser.add_argument("-y", type=int, nargs="?", default=10, help="Y coordinate as integer")
    return parser.parse_args()

def run(world):
    """
    Instantiates a keyboard listener which checks for arrow-key presses.\n
    This keeps the game running as the listener is using a separate thread

    :param world: The game world
    :type world: World
    """
    with keyboard.Listener(on_press=lambda event: player_movement(event, world)) as listener:
        listener.join()

def draw_game(world):
    """
    Draws the game area and if player has reached the door with the key it calls game_win()

    :param world: The game world
    :type world: World
    """
    clear_console()
    for row in world.tilemap:
        print(" ".join(map(str, row)))

    if world.has_won:
        game_win()
    return 0


def player_movement(key, world):
    """
    Moves and draws the player, then calls draw_game()
    :param key: The key that was pressed
    :type key: pynput.keyboard.Key
    :param world: The game world
    :type world: World
    :return: 0 if function executed successfully
    :rtype: int
    """
    world.tilemap[world.player_x, world.player_y] = w.FLOOR
    match key:

        case keyboard.Key.left:
            if not world.tilemap[world.player_x, world.player_y - 1] == w.WALL:
                if world.tilemap[world.player_x, world.player_y -1] == w.DOOR and world.has_key == False:
                    world.player_y += 1 #make sure player doesn't move
                elif world.tilemap[world.player_x, world.player_y - 1] == w.DOOR and world.has_key == True:
                    world.has_won = True
                world.player_y -= 1

        case keyboard.Key.right:
            if not world.tilemap[world.player_x, world.player_y + 1] == w.WALL:
                if world.tilemap[world.player_x, world.player_y +1] == w.DOOR and world.has_key == False:
                    world.player_y -= 1 #make sure player doesn't move
                elif world.tilemap[world.player_x, world.player_y + 1] == w.DOOR and world.has_key == True:
                    world.has_won = True
                world.player_y += 1

        case keyboard.Key.up:
            if not world.tilemap[world.player_x - 1, world.player_y] == w.WALL:
                if world.tilemap[world.player_x - 1, world.player_y] == w.DOOR and world.has_key == False:
                    world.player_x += 1 #make sure player doesn't move
                elif world.tilemap[world.player_x - 1, world.player_y] == w.DOOR and world.has_key == True:
                    world.has_won = True
                world.player_x -= 1

        case keyboard.Key.down:
            if not world.tilemap[world.player_x + 1, world.player_y] == w.WALL:
                if world.tilemap[world.player_x + 1, world.player_y] == w.DOOR and world.has_key == False:
                    world.player_y -= 1 #make sure player doesn't move
                elif world.tilemap[world.player_x + 1, world.player_y] == w.DOOR and world.has_key == True:
                    world.has_won = True
                world.player_x += 1

        case keyboard.Key.esc:
            sys.exit("Thanks for playing!")

    if world.tilemap[world.player_x, world.player_y] == w.KEY:
        world.has_key = True

    world.tilemap[world.player_x, world.player_y] = w.PLAYER
    draw_game(world)
    return 0

def clear_console():
    """
    Clears the console depending on OS environment
    """
    if sys_name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    return 0



if __name__ == "__main__":
    main()
