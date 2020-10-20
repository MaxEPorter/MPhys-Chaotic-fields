import solvefields
import matplotlib as plt

double = solvefields.double_abc_field(0, 10, 0.01, [1, 1, 1], [1, 1, 1, 1, 1, 1, 1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(double.x, double.y, double.z)

plt.show()
