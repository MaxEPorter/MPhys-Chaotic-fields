from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


class MagneticField:
    def __init__(self, parameters):

        self.params = parameters

        self.bx = lambda pos: pos[0]
        self.by = lambda pos: 0
        self.bz = lambda pos: 0

    def magnitude(self, pos):
        return np.sqrt(
            np.power(self.bx(pos), 2) +
            np.power(self.by(pos), 2) +
            np.power(self.bz(pos), 2)
        )


def solve_field_line(s, pos, field):
    mag = field.magnitude(pos)
    return [field.bx(pos)/mag, field.by(pos)/mag, field.bz(pos)/mag]


steps = np.linspace(0, 3, 100)

start = []
for x in np.linspace(0.1, 2, 100):
    for y in np.linspace(0.1, 2, 100):
        start.append([x, y, 0])

mag_field = MagneticField([1, 1, 1])

for p in start:

    try:
        sol = solve_ivp(lambda s, pos: solve_field_line(s, pos, mag_field), [steps[0], steps[-1]], p, t_eval=steps)
        plt.plot(sol.y[0], sol.y[1])
    except ValueError:
        print("Div by 0 err")
    except RuntimeWarning:
        print("wow!")

plt.grid()
plt.xlim(0, 2)
plt.ylim(0, 2)
plt.show()
