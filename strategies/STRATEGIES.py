from strategies.RandomStrategy import RandomStrategy
from strategies.HumanStrategy import HumanStrategy
from strategies.QLearnStrategy import QLearnStrategy
from strategies.ValueIterStrategy import ValueIterStrategy

HUMAN = 0
Q_LEARNING = 1
VALUE_ITERATION = 2
RANDOM = 3


def enum_to_strategy(robot, other_bot, world, type, from_store):
    """
    Convert one of the values above into a strategy object.
    :param robot: The robot that this strategy applies to.
    :param world: The world that the strategy applies to.
    :param type: The type enum of the strategy.
    :return: A Strategy Object.
    """
    if type == HUMAN:
        return HumanStrategy(world)
    elif type == Q_LEARNING:
        return QLearnStrategy(robot, other_bot, world, from_store)
    elif type == VALUE_ITERATION:
        return ValueIterStrategy(robot, other_bot, world, from_store)
    elif type == RANDOM:
        return RandomStrategy(robot, world)
    else:
        raise Exception("Strategy not recognized: %s" % (type))


def key_to_strategy(key):
    if key == "h":
        return HUMAN
    elif key == "v":
        return VALUE_ITERATION
    elif key == "q":
        return Q_LEARNING
    elif key == "r":
        return RANDOM
    else:
        return None
