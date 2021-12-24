from pathlib import Path

from loader import Loader

class Engine:
    def __init__(self, game_path: Path):
        self._game_path = game_path
        self._loader = Loader(game_path)