import numpy as np
import time
import math

# GAME CONFIG
START_LEVEL = 1
WIDTH = 6
HEIGHT = 10
GRID_SIZE = WIDTH * HEIGHT
SYMBOLS = {
    "APPLE": -1,
    "FREE": 0,
    "SNAKE": 1,
}


MAX_LEVEL = GRID_SIZE

# ACTIONS
UP = 'up'
RIGHT = 'right'
DOWN = 'down'
LEFT = 'left'
ACTIONS = [UP, RIGHT, DOWN, LEFT]

# STATE


class State:
    def __init__(self, game):
        self.data = game
        self.hash_val = None
        self.hash()

    # compute the hash value for one state, it's unique
    def hash(self):
        if self.hash_val is None:
            self.hash_val = 0
            for i in np.nditer(self.data.space):
                self.hash_val = self.hash_val * 3 + i + 1
        return self.hash_val

    def next_state(self):
        direction = self.data.snake.direction
        self.data.turn(direction)
        return self.data

# VALUES


class Values:
    def __init__(self):
        self.data = {}

    def get_all_values(self):
        pass

    @staticmethod
    def get_value(game):
        '''
        [key]: @space_hash
          @is_end
          @is_valid_eat
          @head
          @tail
          @apple
          @space (head, tail, apple)
          @space_hash
          @distances [top, right, bot, left]
        '''
        print(game)


# REWARD
'''
  EAT:   +  lvl * (GRID_SIZE - lvl_steps)
  STEP:  -  1
'''


def reward_function(state):
    status, level, is_valid_eat, level_steps = state
    reward = 0
    reward -= 1
    if (status == 'PLAYING'):
        if (is_valid_eat):
            reward += level * (GRID_SIZE - level_steps)
    return reward


# ERRORS


def random_action(): np.random.choice(ACTIONS)


# Only with limited amount of states. In this case theres too many states.
def get_action(state, state_action_values, epsilon=0.1):
    if np.random.randint(low=0, high=1) < epsilon:
        return random_action()
    else:
        # greedy function to get best action
        actions_from_state = state_action_values[state.hash_val]
        q_best = np.max(actions_from_state)
        best_actions = np.where(actions_from_state == q_best)[0]
        action = ACTIONS[np.random.choice(best_actions)]
        return action


def value_aprox_func(state):
    pass


class Model:
    def __init__(self):
        self.state_action_values = {}


model = Model()


def play_1(game):
    state = State(game)
    hash_val = state
    reward = reward_function(state)
    action = get_action(hash_val, model.state_action_values, 0.9)
    model.state_action_values[hash_val, action] = reward

    direction = game.snake.direction
    game.turn(direction)
    return game


if __name__ == '__main__':
    pass
