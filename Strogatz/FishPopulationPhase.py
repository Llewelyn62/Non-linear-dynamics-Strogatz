import matplotlib.animation as animation
from scipy.integrate import odeint
from numpy import arange
import matplotlib.pyplot as plt

def BoatFishSystem(state, t):
    fish, boat = state
    d_fish = fish * (2 - boat - fish)
    d_boat = -boat * (1 - 1.5 * fish)
    return [d_fish, d_boat] 
t = arange(0, 20, 0.1)
init_state = [1, 1]
state = odeint(BoatFishSystem, init_state, t)

fig = plt.figure()
plt.xlabel('number of fish')
plt.ylabel('number of boats')
plt.plot(state[:, 0], state[:, 1], 'b-', alpha=0.2)

def animate(i):
    plt.plot(state[0:i, 0], state[0:i, 1], 'b-')

ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()