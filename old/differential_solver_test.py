import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import odeint


# Test differentiating SHM
# tested

def ode(y, t):
    x, xp = y
    ode = [xp, -x]
    return ode


y0 = [0, 1]
t = np.linspace(0, 10, 100)
sol = scipy.integrate.odeint(ode, y0, t)

plt.plot(t, sol[:, 0])



def shm(t, x, omega):
    return [x[1], -omega*x[0]]

t = np.linspace(0, 20, 1000)
xini = [0, 1]
om = 1

sol = scipy.integrate.solve_ivp(lambda t, x: shm(t, x, om), [t[0], t[-1]], xini, t_eval=t)
plt.plot(sol.t, sol.y[0])










plt.show()
