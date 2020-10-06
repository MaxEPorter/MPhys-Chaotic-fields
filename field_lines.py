from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



class MagneticField:
    def __init__(self, parameters):

        self.params = parameters

        self.bx = lambda pos: self.params[0]*np.sin(self.params[3]*pos[2]) + self.params[2]*np.cos(self.params[3]*pos[1])
        self.by = lambda pos: self.params[1]*np.sin(self.params[3]*pos[0]) + self.params[0]*np.cos(self.params[3]*pos[2])
        self.bz = lambda pos: self.params[2]*np.sin(self.params[3]*pos[1]) + self.params[1]*np.cos(self.params[3]*pos[0])

    def magnitude(self, pos):
        return np.sqrt(
            np.power(self.bx(pos), 2) +
            np.power(self.by(pos), 2) +
            np.power(self.bz(pos), 2)
        )


def solve_field_line(s, pos, field):
    mag = field.magnitude(pos)
    return [field.bx(pos)/mag, field.by(pos)/mag, field.bz(pos)/mag]


steps = np.linspace(0, 3000, 1000000)

start = []
for x in np.linspace(0.1, 2, 1):
    for y in np.linspace(0.1, 2, 1):
        for z in np.linspace(0.1, 2, 1):
            start.append([x, y, z])

print(start)
start = [[0.213, 0.342, 0.001]]

mag_field = MagneticField([1, np.sqrt(2/3), np.sqrt(1/3), 1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for p in start:

    sol = solve_ivp(lambda s, pos: solve_field_line(s, pos, mag_field), [steps[0], steps[-1]], p, t_eval=steps)
    plt.plot(sol.y[0], sol.y[1], sol.y[2])


plt.grid()

#ax.set_zlim(0, 2)
#ax.set_ylim(0, 2)
#ax.set_xlim(0, 2)

plt.show()
