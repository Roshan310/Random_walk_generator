""" THIS IS A BUGGY ONE
    It will take some time to complete this project.
 """
 # 1D implementation 
import matplotlib.pyplot as plt
import numpy as np
import random

origin = 0
step = origin
coin_states = ['H', 'D']

random_steps = []
time_stamp = []
count = 0

while count < 1000:

    if random.choice(coin_states) == 'H':
        step += 1
        count += 1
        random_steps.append(step)
        time_stamp.append(count)
    else:
        step -= 1
        count += 1
        random_steps.append(step)
        time_stamp.append(count)


plt.plot(time_stamp, random_steps)
plt.show()
