from os import system, name as sys_name
import sys

import argparse

from pynput import keyboard
import world as w


def main():
    world = initialize_game()
    run(world)


def initialize_game():
    print("=== WELCOME TO THIS SHORT ESCAPE ROOM ===")
    print("Goal: collect the key and get to the exit...")

    args = get_args()

    world = w.World(args.x, args.y)
    draw_game(world)
    return world

def game_win():
    print("Congratulations! You won!")
    sys.exit("--A short game by Malte Bodenbach--")


def get_args():
    parser = argparse.ArgumentParser(description="A short escape room game")
    parser.add_argument("-x",default=10, help="Horizontal size of the room")
    parser.add_argument("-y",default=10, help="Vertical size of the room")
    return parser.parse_args()

def run(world):
    with keyboard.Listener(on_press=lambda event: player_movement(event, world)) as listener:
        listener.join()

def draw_game(world):
    clear_console()
    for row in world.tilemap:
        print(" ".join(map(str, row)))

    if world.has_won:
        game_win()


def player_movement(key, world):
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

def clear_console():
    if sys_name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")



if __name__ == "__main__":
    main()
