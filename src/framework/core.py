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
    pass


class State:
    pass


class Transition:
    pass
