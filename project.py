import numpy as np

WALL = "#"
FLOOR = " "
DOOR = "-"
KEY = "~"
PLAYER = "A"


def main():
    initialize_game()
    run()


def initialize_game():
    #startup msg
    #ask for room size
    room = Room()



def run():
    ...


def draw_map():
    ...


def draw_player():
    ...


class Room:
    def __init__(self, X=10, Y=10):
        if X < 3 or Y < 4:
            raise ValueError("Room size too small")
        self._tilemap = np.array(f"{range(X)}; {range(Y)}")

    def generate_walls(self):
        ...

    def generate_door(self):
        ...

    def generate_key(self):
        ...

    def generate_player(self):
        ...


if __name__ == "__main__":
    main()
