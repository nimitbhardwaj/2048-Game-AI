try:
    from game import Game2048
    from manager import GameManager
    from main import run_game, main
except ImportError:
    from .game import Game2048
    from .manager import GameManager
    from .main import run_game, main

