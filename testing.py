import solvefields
import matplotlib.pyplot as plt


abc = solvefields.abc_field(0, 1000, 0.01, [1, 2, 1], [1, 2, 2, 1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(abc.x, abc.y, abc.z)

plt.show()