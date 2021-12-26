from abc import ABC
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Protocol, Tuple


class SaveGame:
    def __init__(self, save_file: Path) -> None:
        self.save_file: Path = save_file
        self.players: Optional[Dict[str, Player]] = None

    def save(self) -> None:
        pass

    def load(self) -> None:
        pass


class GameObject(Protocol):
    id: str
    title: str
    description: str


class HashableGameObject(GameObject, ABC):
    def __init__(self, id: str):
        self.id = id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"


class RuleApplianceType(str, Enum):
    ALWAYS = "always"
    ON_TRANSITION_ACCEPTED = "accepted"
    ON_TRANSITION_REFUSED = "refused"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self._value_}')"


class RuleAdaption(str, Enum):
    ADD = "add_rule"
    SUB = "sub_rule"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self._value_}')"


class GlobalRule(HashableGameObject):
    def __init__(
            self,
            rule_id: str,
            title: str,
            description: str,
            rule: Dict[
                Tuple[str], Dict[RuleAdaption, List[str]]
            ],  # Dict[ List[state], Dict[ RuleAdaption(ADD|SUB), List[state] ] ]
    ) -> None:
        self.id: str = rule_id
        self.title = title
        self.description = description
        self.rule: Dict[Tuple[str], Dict[RuleAdaption, List[str]]] = rule


class TransitionRule(GlobalRule):
    def __init__(
            self,
            rule_id: str,
            title: str,
            description: str,
            rule: Dict[
                Tuple[str], Dict[RuleAdaption, List[str]]
            ],  # Dict[ List[state], Dict[ RuleAdaption(ADD|SUB), List[state] ] ]
            rule_appliance_type: RuleApplianceType,
    ) -> None:
        super(GlobalRule, self).__init__(
            rule_id, title, description, rule
        )

        self.rule_appliance_type: RuleApplianceType = rule_appliance_type


class Scene(HashableGameObject):
    def __init__(self, scene_id: str, title: str = "", description: str = "") -> None:
        self.id: str = scene_id
        self.title: str = title
        self.description: str = description
        self.transitions: List[Transition] = []


class Transition(HashableGameObject):
    def __init__(
            self, transition_id: str, title: str = "", description: str = ""
    ) -> None:
        self.id = transition_id
        self.title = title
        self.description = description
        self.required_states: List[str] = []
        self.transition_to_scene: Optional[Scene] = None
        self.to_applying_rules: List[Rule] = []


class Player(HashableGameObject):
    def __init__(
            self, player_id: str, name: str, description: str, current_scene: Scene
    ) -> None:
        """Initialize Player

        :param player_id: The ID of the Player
        :param current_scene: Indicates in which scene player is currently located.
        """

        self.id: str = player_id
        self.title = name
        self.description = description
        self.current_scene: Scene = current_scene
        self.states: List[str] = []
        self.rules: List[GlobalRule] = []


class Room(HashableGameObject):
    def __init__(self, room_id: str, title: str = "", description: str = "") -> None:
        self.id = room_id
        self.title = title
        self.description = description
