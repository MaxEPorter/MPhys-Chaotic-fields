import field_lines
import matplotlib.pyplot as plt
import numpy as np

# UNIFORM FIELD EXAMPLE
steps = np.linspace(0, 5, 1000)  # generate path length, smaller step length increases accuracy
# input field component functions, will be static field in y direction
uniform_field = field_lines.MagneticField([
    lambda pos: 0,   # B_x
    lambda pos: 3,   # B_y
    lambda pos: 0])  # B_z
ini = [[1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0]]  # beginning of field lines
lines = field_lines.generate_lines(steps, ini, uniform_field)  # list of line solutions
# line.y contains list of output positions
# eg line.y[0] will be list of x coordinates, line.y[1] will be y, line.y[2] will be z

# plot all lines
plt.figure()
for line in lines:
    plt.plot(line.y[0], line.y[1], color='blue')

plt.title(r'Field lines for Uniform field $( B_y = 3 )$')
plt.xlabel('x')
plt.ylabel('y')


# ARROW PLOT
"""
plt.figure()
x = np.linspace(0, 5, 10)
y = np.linspace(0, 5, 10)
X, Y = np.meshgrid(x, y)

u = []
v = []
for a, b in zip(x, y):
    u.append(uniform_field.bx([a, b], *uniform_field.params))
    v.append(uniform_field.by([a, b], *uniform_field.params))

U, V = np.meshgrid(u, v)

plt.quiver(X, Y, U, V)
"""

ax = field_lines.arrow_plot_2d(uniform_field)


plt.show()
