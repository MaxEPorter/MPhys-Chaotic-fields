import numpy as np
import matplotlib.pyplot as plt
import field_lines

# ABC FIELD EXAMPLE
steps = np.linspace(0, 3000, 1000000)
abc_field = field_lines.MagneticField([
    lambda pos, a, b, c, lamb: a*np.sin(lamb*pos[2]) + c*np.cos(lamb*pos[1]),
    lambda pos, a, b, c, lamb: b*np.sin(lamb*pos[0]) + a*np.cos(lamb*pos[2]),
    lambda pos, a, b, c, lamb: c*np.sin(lamb*pos[1]) + b*np.cos(lamb*pos[0])],
    1, np.sqrt(2/3), np.sqrt(1/3), 1
)
ini = [0.213, 0.342, 0.001]  # one field line
lines = field_lines.generate_lines(steps, ini, abc_field)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(lines.y[0], lines.y[1], lines.y[2])

plt.show()