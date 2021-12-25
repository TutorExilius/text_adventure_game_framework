from pathlib import Path
from typing import Dict, List

from .data_types import Player, Rule, Scene, Transition


class Loader:
    def __init__(self, game_path: Path):
        self.player: Dict[str, Player] = {}
        self.rules: Dict[str, Rule] = {}
        self.scenes: Dict[str, Scene] = {}
        self.states: List[str] = []
        self.transitions: Dict[str, Transition] = {}

        self._load_game_configuration_files(game_path)

    def _load_game_configuration_files(self, game_path: Path) -> None:
        self._load_player()
        self._load_rules()
        self._load_scenes()
        self._load_states()
        self._load_transitions()

    def _load_player(self) -> None:
        pass

    def _load_rules(self) -> None:
        pass

    def _load_scenes(self) -> None:
        pass

    def _load_states(self) -> None:
        pass

    def _load_transitions(self) -> None:
        pass
