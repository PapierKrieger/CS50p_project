import numpy as np
from random import randrange

WALL = "\u2588"
FLOOR = " "
DOOR = "-"
KEY = "\u26b7"
PLAYER = "A"


class World:
    """
    The game world. Contains play area, player and key as well as has_won and has_key flags
    """
    def __init__(self, x, y):
        """
        Initializes the world with the given coordinates.

        :param x: play area height
        :type x: int
        :param y: play area width
        :type y: int
        :raise ValueError: If x or y are smaller than 4 or larger than 30
        """
        if 3 < x <= 30 and 3 < y <= 30:
            pass
        else:
            raise ValueError("room cannot be smaller than 4x4 or larger than 30x30")
        self.x = x
        self.y = y
        self.tilemap = np.full((x, y), FLOOR, dtype=str)

        self.has_key = False
        self.has_won = False

        self.key_x = randrange(1, self.y - 1)
        self.key_y = randrange(1, self.x - 1)

        self.player_x = 0
        self.player_y = 0

        self.generate_walls()
        self.generate_door()
        self.generate_key()
        self.generate_player()

    def generate_walls(self):
        """
        Place wall characters at appropriate positions on play area
        :return: 0 if method completed successfully
        :rtype: int
        """
        for i in range(self.x):
            self.tilemap[i, 0] = WALL
            self.tilemap[i, -1] = WALL

        for i in range(self.y):
            self.tilemap[0, i] = WALL
            self.tilemap[-1, i] = WALL
        return 0

    def generate_door(self):
        """
        Set door location in play area
        :return: 0 if method completed successfully
        :rtype: int
        """
        direction = randrange(1, 4) # 1: ^ | 2: > | 3: v | 4: <
        match direction:
            case 1: self.tilemap[randrange(1, self.x - 1), 0] = DOOR
            case 2: self.tilemap[0, randrange(1, self.y - 1)] = DOOR
            case 3: self.tilemap[randrange(1, self.x - 1), -1] = DOOR
            case 4: self.tilemap[-1, randrange(1, self.y - 1)] = DOOR
        return 0

    def generate_key(self):
        """
        Set key location in play area

        :return: 0 if method completed successfully
        :rtype: int
        """
        self.tilemap[self.key_x, self.key_y] = KEY
        return 0

    def generate_player(self):
        """
        Set player location in play area

        :return: 0 if method completed successfully
        :rtype: int
        """
        self.player_x = randrange(1, self.x - 1)
        self.player_y = randrange(1, self.y - 1)

        if self.tilemap[self.player_x, self.player_y] == KEY:
            self.generate_player()
        else:
            self.tilemap[self.player_x, self.player_y] = PLAYER
        return 0

