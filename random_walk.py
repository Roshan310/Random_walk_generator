""" THIS IS A BUGGY ONE
    It will take some time to complete this project.
 """

import matplotlib.pyplot as plt
import math
import random
import time

origin = 0
step = origin
step_lenght = 1
coin_states = ['H', 'D']
PAUSE_DURATION = 0.8
x_steps = []
y_steps = []


def get_y(x):
    if x == 0:
        return 0

    return (get_y(x-1) + math.exp(1))

while True:
    if step == 20:
        break
    if random.choice(coin_states) == 'H':
        step += 1
        x_steps.append(step)
    else:
        step -= 1
        x_steps.append(step)

    y_value = get_y(step)
    y_steps.append(y_value)
    print(f"X: {step}, Y: {y_value}")

print(len(x_steps), len(y_steps))

plt.plot(x_steps, y_steps, 'ro')
plt.show()
