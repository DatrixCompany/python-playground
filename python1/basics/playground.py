import numpy as np

# hash_val = 0
# data = np.zeros((3, 3))
# data2 = [[1, 1, 1], [0, 0, 0], [1, 0, 0]]
# print(data2)
# print(data)
# data = np.array(data2)


# for i in np.nditer(data):
#     print(i)
#     hash_val = hash_val * 3 + i + 1
# print(hash_val)
x = 4 + \
    4 * \
    8

# l = np.array(())

# grid[row (height), col (width)] = np.zeros((5, 10))
grid = np.zeros((10, 5))
grid[1, 1] = 1
grid[0, 3] = 5
grid[5, 0] = -5
state_action_values = np.full((10, 4), 0.5)
state_action_values[4, 1] = 0.7
state_action_values[4, 2] = 0.7
state_action_values[6, 3] = 0.7
state_action_values[8, 2] = 0.7

state_row = state_action_values[3]
axisN = np.argmax(state_action_values)
axis0 = np.argmax(state_action_values, axis=0)
axis1 = np.argmax(state_action_values, axis=1)
# print(axisN, axis0, axis1)

# actions_from_state = state_action_values[4]
# q_best = np.max(actions_from_state)
# best_actions = np.where(actions_from_state == q_best)[0]
# action = np.random.choice(best_actions)
# print(action)

g = {'x': 2, 'y': 3, "k": 4}
z = {f'{key}_comp': value*2 if value == 2
     else value * 5
     for key, value in g.items() if value % 2 == 0}
print(z)
