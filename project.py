from os import system, name as sys_name
import sys
import numpy as np
from pynput import keyboard
from random import randrange

WALL = "#"
FLOOR = " "
DOOR = "-"
KEY = "~"
PLAYER = "A"

def main():
    world = initialize_game()
    run(world)


def initialize_game():
    print("=== WELCOME ===")
    world = World()
    draw_game(world)
    return world

def game_win():
    print("Congratulations! You won!")
    sys.exit("A short game by Malte Bodenbach")


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
    world.tilemap[world.player_x, world.player_y] = FLOOR
    match key:

        case keyboard.Key.left:
            if not world.tilemap[world.player_x, world.player_y - 1] == WALL:
                if world.tilemap[world.player_x, world.player_y -1] == DOOR and world.has_key == False:
                    world.player_y += 1 #make sure player doesn't move
                elif world.tilemap[world.player_x, world.player_y - 1] == DOOR and world.has_key == True:
                    world.has_won = True
                world.player_y -= 1

        case keyboard.Key.right:
            if not world.tilemap[world.player_x, world.player_y + 1] == WALL:
                if world.tilemap[world.player_x, world.player_y +1] == DOOR and world.has_key == False:
                    world.player_y -= 1 #make sure player doesn't move
                elif world.tilemap[world.player_x, world.player_y + 1] == DOOR and world.has_key == True:
                    world.has_won = True
                world.player_y += 1

        case keyboard.Key.up:
            if not world.tilemap[world.player_x - 1, world.player_y] == WALL:
                if world.tilemap[world.player_x - 1, world.player_y] == DOOR and world.has_key == False:
                    world.player_x += 1 #make sure player doesn't move
                elif world.tilemap[world.player_x - 1, world.player_y] == DOOR and world.has_key == True:
                    world.has_won = True
                world.player_x -= 1

        case keyboard.Key.down:
            if not world.tilemap[world.player_x + 1, world.player_y] == WALL:
                if world.tilemap[world.player_x + 1, world.player_y] == DOOR and world.has_key == False:
                    world.player_y -= 1 #make sure player doesn't move
                elif world.tilemap[world.player_x + 1, world.player_y] == DOOR and world.has_key == True:
                    world.has_won = True
                world.player_x += 1

    if world.tilemap[world.player_x, world.player_y] == KEY:
        world.has_key = True

    world.tilemap[world.player_x, world.player_y] = PLAYER
    draw_game(world)

def clear_console():
    if sys_name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


class World:
    def __init__(self, x=10, y=10):
        if 3 < x < 30 and 3 < y < 30:
            pass
        else:
            raise ValueError("room cannot be smaller than 4x4")
        self.x = x
        self.y = y
        self.tilemap = np.full((x, y), FLOOR, dtype=str)

        self.has_key = False
        self.has_won = False

        self.player_x = 0
        self.player_y = 0

        self.generate_walls()
        self.generate_door()
        self.generate_key()
        self.generate_player()

        print(self.tilemap)

    def generate_walls(self):
        for i in range(self.x):
            self.tilemap[i, 0] = WALL
            self.tilemap[i, -1] = WALL

        for i in range(self.y):
            self.tilemap[0, i] = WALL
            self.tilemap[-1, i] = WALL

    def generate_door(self):
        direction = randrange(1, 4) # 1: ^ | 2: > | 3: v | 4: <
        match direction:
            case 1: self.tilemap[randrange(1, self.x - 1), 0] = DOOR
            case 2: self.tilemap[0, randrange(1, self.y - 1)] = DOOR
            case 3: self.tilemap[randrange(1, self.x - 1), -1] = DOOR
            case 4: self.tilemap[-1, randrange(1, self.y - 1)] = DOOR

    def generate_key(self):
        key_x = randrange(1, self.x - 1)
        key_y = randrange(1, self.y - 1)

        self.tilemap[key_x, key_y] = KEY

    def generate_player(self):
        self.player_x = randrange(1, self.x - 1)
        self.player_y = randrange(1, self.y - 1)

        if self.tilemap[self.player_x, self.player_y] == KEY:
            self.generate_player()
        else:
            self.tilemap[self.player_x, self.player_y] = PLAYER


if __name__ == "__main__":
    main()
