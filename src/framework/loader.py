from collections import defaultdict
from pathlib import Path
from typing import Dict

from data_types import Player, Rule, Scene, State, Transition


class Loader:
    def __init__(self, game_path: Path):
        self.player: Dict[str, Player] = {}
        self.rules: Dict[str, Rule] = defaultdict(list)
        self.scenes: Dict[str, Scene] = defaultdict(list)
        self.states: Dict[str, State] = defaultdict(list)
        self.transitions: Dict[str, Transition] = defaultdict(list)

        self._load_game_configuration_files(game_path)

    def _load_game_configuration_files(self):
        self._load_player()
        self._load_rules()
        self._load_scenes()
        self._load_states()
        self._load_transitions()

    def _load_player(self):
        pass

    def _load_rules(self):
        pass

    def _load_scenes(self):
        pass

    def _load_states(self):
        pass

    def _load_transitions(self):
        pass
