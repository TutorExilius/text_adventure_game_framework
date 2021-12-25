# Test Application

from pprint import pprint

from framework.data_types import (
    Player,
    Rule,
    RuleAdaption,
    RuleApplianceType,
    Scene,
    Transition,
)

scene = Scene("main_scene", "The Kitchen", "You are in the kitchen, alone,..")
player = Player("player_1", "Player 1", "Ein Spieler", scene)
rule = Rule(
    "kitchen_bathroom_lost_key",
    "Key is broken by using it.",
    (
        "You used the key and opend the door to the bathroom."
        "The key is broken by trying pulling it out,..."
    ),
    {("has_kitchen_key",): {RuleAdaption.SUB: ["has_kitchen_key"]}},
    RuleApplianceType.ON_TRANSITION_ACCEPTED,
)

transition = Transition("kitchen_to_bathroom_by_key_use")
transition.required_states.append("has_kitchen_key")
transition.to_applying_rules.append(rule)
scene.transitions.append(transition)
player.current_scene = scene
player.states.append("has_kitchen_key")

pprint(player)

# rule_dict = BaseEncoder().encode(rule)
# pprint(rule_dict)
