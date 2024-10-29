from collections import namedtuple
from world import World
from project import initialize_game, game_win, get_args, clear_console, draw_game
import pytest

# test project file
def test_initialize_game():
    # mock args to be able to access the "arguments" by using args.x and args.y inside of initialize_game()
    Mock_args = namedtuple("args", ["x", "y"])
    mock_args = Mock_args(10, 10)

    game = initialize_game(mock_args)
    assert isinstance(game, World)

def test_game_win():
    with pytest.raises(SystemExit):
        game_win()

def test_get_args():
    with pytest.raises(SystemExit):
        get_args()

def test_draw_game():
    world = World(10, 10)
    assert draw_game(world) == 0

def test_clear_console():
    assert clear_console() == 0


# test world class
def test_world_generate_walls():
    world = World(10, 10)
    assert world.generate_walls() == 0
    assert world.tilemap[0,0] == "\u2588"
    assert world.tilemap[2,2] == " " or world.tilemap[2,2] == "\u26b7" #also checks for key

def test_world_generate_door():
    world = World(10, 10)
    assert world.generate_door() == 0

def test_world_generate_key():
    world = World(10, 10)
    assert world.generate_key() == 0
    assert world.tilemap[world.key_x,world.key_y] == "\u26b7"
    assert world.tilemap[world.key_x,world.key_y] is not " "

def test_world_generate_player():
    world = World(10, 10)
    assert world.generate_player() == 0
    assert str(world.tilemap[world.player_x,world.player_y]) is "A"