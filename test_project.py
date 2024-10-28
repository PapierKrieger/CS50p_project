from world import World
from project import initialize_game, game_win, get_args, clear_console, draw_game
import pytest

# test project file
def test_initialize_game():
    game = initialize_game(10, 10)
    assert isinstance(game, World)

def test_game_win():
    with pytest.raises(SystemExit):
        game_win()

def test_get_args():
    with pytest.raises(SystemExit):
        get_args()

def test_draw_game():
    world = World()
    assert draw_game(world) == 0

def test_clear_console():
    assert clear_console() == 0


# test world class
def test_world_generate_walls():
    world = World()
    assert world.generate_walls() == 0
    assert world.tilemap[0,0] == "\u2588"
    assert world.tilemap[2,2] == " "

def test_world_generate_door():
    world = World()
    assert world.generate_door() == 0

def test_world_generate_key():
    world = World()
    assert world.generate_key() == 0
    assert world.tilemap[world.key_x,world.key_y] == "\u26b7"
    assert world.tilemap[world.key_x,world.key_y] is not " "

def test_world_generate_player():
    world = World()
    assert world.generate_player() == 0
    assert str(world.tilemap[world.player_x,world.player_y]) is "A"