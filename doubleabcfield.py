

import numpy as np
import matplotlib.pyplot as plt
import field_lines

default_params = [1, np.sqrt(2/3), np.sqrt(1/3), 1]
new_params = [1, 1, #a1a2
              np.sqrt(2/3), np.sqrt(2/3), #b1b2
              np.sqrt(1/3), np.sqrt(1/3), #c1c2
              1, -0.5] #lambs

newer_params = [2, 1, #a1a2
              2, 1, #b1b2
              2, 1, #c1c2
              4, 4] #lambs

# doubleABC FIELD
steps = np.linspace(0, 100, 10000)
abc_field = field_lines.MagneticField([
    lambda pos, a1, a2, b1, b2, c1, c2, lambpos, lambneg: a1*np.sin(lambpos*pos[2]) + c1*np.cos(lambpos*pos[1]) + a2*np.sin(lambneg*pos[2]) + c2*np.cos(lambneg*pos[1]),
    lambda pos, a1, a2, b1, b2, c1, c2, lambpos, lambneg: b1*np.sin(lambpos*pos[0]) + a1*np.cos(lambpos*pos[2]) + b2*np.sin(lambneg*pos[0]) + a2*np.cos(lambneg*pos[2]),
    lambda pos, a1, a2, b1, b2, c1, c2, lambpos, lambneg: c1*np.sin(lambpos*pos[1]) + b1*np.cos(lambpos*pos[0]) + c2*np.sin(lambneg*pos[1]) + c2*np.cos(lambneg*pos[0])],
    *newer_params
)
ini = [0, 1000000, 0]  # one field line
line_DOP = field_lines.generate_lines(steps, ini, abc_field, method='DOP853')
# line_RK = field_lines.generate_lines(steps, ini, abc_field, method='RK45')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(line_DOP.y[0], line_DOP.y[1], line_DOP.y[2], color='red')
# plt.plot(line_RK.y[0], line_RK.y[1], line_RK.y[2], color='blue')

# arrow = field_lines.arrow_plot_3d(abc_field, [0,1],[0,1],[0,1],10)

plt.show()