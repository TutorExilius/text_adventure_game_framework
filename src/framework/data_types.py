from enum import Enum


class Player:
    pass


class RuleApplianceType(str, Enum):
    ALWAYS = "always"
    ON_TRANSITION_ACCEPTED = "accepted"
    ON_TRANSITION_REFUSED = "refused"


class Rule:
    pass


class Scene:
    def __init__(self, scene_id: str, title: str = "") -> None:
        self.scene_id: str = scene_id
        self.title = title
        self.transitions: Dict[str, Transition] = {}  # str("transistion_id") -> Transition()


class State:
    pass


class Transition:
    pass
