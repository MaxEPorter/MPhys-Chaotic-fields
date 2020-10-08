from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class MagneticField:
    def __init__(self, field: list, *params):
        # argument field expects list of field components in cartesians
        # argument params for arbitrary number of parameters to be used in field
        # length of params must represent number of params in field

        # store field and input parameters
        self.params = params

        self.bx = field[0]
        self.by = field[1]
        self.bz = field[2]

    def magnitude(self, pos):
        # calculate the magnitude of the field at a particular pos(x, y, z)
        return np.sqrt(
            np.power(self.bx(pos, *self.params), 2) +
            np.power(self.by(pos, *self.params), 2) +
            np.power(self.bz(pos, *self.params), 2)
        )


# to arrange field equations in form used for ode solver
def to_solve_field_lines(s, pos: list, field: MagneticField):
    mag = field.magnitude(pos)
    return [field.bx(pos, *field.params)/mag,
            field.by(pos, *field.params)/mag,
            field.bz(pos, *field.params)/mag]


# generate list of field line origins
def get_line_begin(x: list, y: list, z: list):
    start = []
    for x in np.linspace(0.1, 2, 1):
        for y in np.linspace(0.1, 2, 1):
            for z in np.linspace(0.1, 2, 1):
                start.append([x, y, z])
    return start


# generate field lines
def generate_lines(path, initial_pos: list, mag_field: MagneticField):
    # path arg as list of path length values

    # find whether multiple lines are expected
    initial_pos = np.array(initial_pos)
    if initial_pos.ndim == 1:  # one field line expected
        sol = solve_ivp(lambda s, pos: to_solve_field_lines(s, pos, mag_field),
                        [path[0], path[-1]],
                        initial_pos,
                        t_eval=path)
        return sol

    else:
        sols = []
        for pos in initial_pos:  # multiple field lines expected
            sols.append(solve_ivp(lambda s, pos: to_solve_field_lines(s, pos, mag_field),
                                  [path[0], path[-1]],
                                  pos,
                                  t_eval=path))
        return sols


# UNIFORM FIELD EXAMPLE
steps = np.linspace(0, 5, 1000)  # generate path length, smaller step length increases accuracy
# input field component functions, will be static field in y direction
uniform_field = MagneticField([
    lambda pos: 0,   # B_x
    lambda pos: 3,   # B_y
    lambda pos: 0])  # B_z
ini = [[1, 1, 0], [2, 1, 0], [3, 1, 0]]  # beginning of field lines
lines = generate_lines(steps, ini, uniform_field)  # list of line solutions
# line.y contains list of output positions
# eg line.y[0] will be list of x coordinates, line.y[1] will be y, line.y[2] will be z

# plot all lines
plt.figure()
for line in lines:
    plt.plot(line.y[0], line.y[1])


# ABC FIELD EXAMPLE
steps = np.linspace(0, 3000, 1000000)
abc_field = MagneticField([
    lambda pos, a, b, c, lamb: a*np.sin(lamb*pos[2]) + c*np.cos(lamb*pos[1]),
    lambda pos, a, b, c, lamb: b*np.sin(lamb*pos[0]) + a*np.cos(lamb*pos[2]),
    lambda pos, a, b, c, lamb: c*np.sin(lamb*pos[1]) + b*np.cos(lamb*pos[0])],
    1, np.sqrt(2/3), np.sqrt(1/3), 1
)
ini = [0.213, 0.342, 0.001]  # one field line
lines = generate_lines(steps, ini, abc_field)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(lines.y[0], lines.y[1], lines.y[2])

plt.grid()
plt.show()




"""

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
"""
