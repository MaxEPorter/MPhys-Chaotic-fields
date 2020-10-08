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
ini = [[1, 1, 0], [2, 1, 0], [3, 1, 0]]  # beginning of field lines
lines = field_lines.generate_lines(steps, ini, uniform_field)  # list of line solutions
# line.y contains list of output positions
# eg line.y[0] will be list of x coordinates, line.y[1] will be y, line.y[2] will be z

# plot all lines
plt.figure()
for line in lines:
    plt.plot(line.y[0], line.y[1])