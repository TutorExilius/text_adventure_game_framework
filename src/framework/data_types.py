from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Protocol


class SaveGame:
    def __init__(self, save_file: Path) -> None:
        self.save_file = save_file
        self.players: Optional[Dict[str, Player]] = None

    def save(self) -> None:
        pass

    def load(self) -> None:
        pass


class GameObject(Protocol):
    id: str


class Player(GameObject):
    def __init__(self, player_id: str, current_scene: str) -> None:
        """Initialize Player

        :param player_id: The ID of the Player
        :param current_scene: Indicates in which scene player is currently located.
        """

        self.id = player_id
        self.current_scene: str = current_scene
        self.states: List[State] = []


class RuleApplianceType(str, Enum):
    ALWAYS = "always"
    ON_TRANSITION_ACCEPTED = "accepted"
    ON_TRANSITION_REFUSED = "refused"


class Rule(GameObject):
    pass


class Scene(GameObject):
    def __init__(self, scene_id: str, title: str = "") -> None:
        self.scene_id: str = scene_id
        self.title = title
        self.transitions: Dict[
            str, Transition
        ] = {}  # str("transistion_id") -> Transition()


class State(GameObject):
    pass


class Transition(GameObject):
    pass
