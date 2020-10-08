import numpy as np
import matplotlib.pyplot as plt
import field_lines

# (WIRE FIELD mu_0*I/2pi=1)
steps = np.linspace(0, 14.2, 1000000)
wire_field = field_lines.MagneticField([
    lambda pos: (1/(pos[0]**2+pos[1]**2))*(-pos[1]),
    lambda pos: (1/(pos[0]**2+pos[1]**2))*(pos[0]),
    lambda pos: 0])
ini = [[1, 2, 1], [1, 2, 2],[1, 2, 3]] # one field line
lines = field_lines.generate_lines(steps, ini, wire_field, method='DOP853')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for line in lines:
    plt.plot(line.y[0], line.y[1], line.y[2])

plt.show()
