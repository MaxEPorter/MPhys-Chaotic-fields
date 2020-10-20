import numpy as np
import matplotlib.pyplot as plt
import field_lines

default_params = [1, np.sqrt(2/3), np.sqrt(1/3), 1] # ones they used
new_params = [1, 1, 3, 1]  # looks like theirs
new_params = [1, 2, 2, 1]

# ABC FIELD EXAMPLE
steps = np.linspace(0, 1000, 10000)
abc_field = field_lines.MagneticField([
    lambda pos, a, b, c, lamb: a*np.sin(lamb*pos[2]) + c*np.cos(lamb*pos[1]),
    lambda pos, a, b, c, lamb: b*np.sin(lamb*pos[0]) + a*np.cos(lamb*pos[2]),
    lambda pos, a, b, c, lamb: c*np.sin(lamb*pos[1]) + b*np.cos(lamb*pos[0])],
    *new_params
)
ini = [0.213, 0.342, 0.1]  # one field line
ini = [1, 2, 1]
line_DOP = field_lines.generate_lines(steps, ini, abc_field, method='DOP853')
# line_RK = field_lines.generate_lines(steps, ini, abc_field, method='RK45')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(line_DOP.y[0], line_DOP.y[1], line_DOP.y[2], color='red')
# plt.plot(line_RK.y[0], line_RK.y[1], line_RK.y[2], color='blue')

fig = plt.figure()
ax2 = fig.add_subplot(111)
ax2.plot(line_DOP.t, line_DOP.y[0], label='x')
ax2.plot(line_DOP.t, line_DOP.y[1], label='y')
ax2.plot(line_DOP.t, line_DOP.y[2], label='z')
ax2.legend()

# arrow = field_lines.arrow_plot_3d(abc_field, [0,1],[0,1],[0,1],10)

plt.show()
