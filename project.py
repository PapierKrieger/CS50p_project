import numpy as np
from random import randrange

WALL = "#"
FLOOR = " "
DOOR = "-"
KEY = "~"
PLAYER = "A"


def main():
    initialize_game()
    run()


def initialize_game():
    print("sup bitch this my game")
    room = Room()
    print(room)



def run():
    ...


def draw_map():
    ...


def draw_player():
    ...


class Room:
    def __init__(self, x=10, y=10):
        if 3 < x < 30 and 3 < y < 30:
            pass
        else:
            raise ValueError("room cannot be smaller than 4x4")
        self.x = x
        self.y = y
        self.tilemap = np.full((x, y), FLOOR, dtype=str)

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
        player_x = randrange(1, self.x - 1)
        player_y = randrange(1, self.y - 1)

        if self.tilemap[player_x, player_y] == KEY:
            self.generate_player()
        else:
            self.tilemap[player_x, player_y] = PLAYER


if __name__ == "__main__":
    main()
