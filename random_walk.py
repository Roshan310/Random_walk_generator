import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

origin = 0
step = origin
step_lenght = 1
coin_states = ['H', 'T']

x_steps = []
y_steps = []

fig, ax = plt.subplots(figsize=(6, 5))
ax.set(xlim=(-10, 10), ylim=(-50, 50))

while True:
    if step == 10:
        break
    if random.choice(coin_states) == 'H':
        step += 1
        x_steps.append(step)
    else:
        step -= 1
        x_steps.append(step)

y_steps = np.cumsum(x_steps)

line = ax.plot(y_steps[0], x_steps[0], color='k', lw=2)[0]  # plotting the first line

# aimation function to change the line every frame
def animate(i):
    line.set_data(y_steps[:i], x_steps[:i])
    return line

print(len(x_steps))
# calling the funcanimation function
anim = FuncAnimation(fig, animate, interval=100, cache_frame_data=False)

plt.draw()
plt.show()






