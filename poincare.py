import solvefields
import saveload
import matplotlib.pyplot as plt
import numpy as np

sol = solvefields.abc_field(0, 10000, 0.01, [1.5, 2.3, 1.5], [1, np.sqrt(2/3), np.sqrt(1/3), 1])
# saveload.save(sol, 'poincare1')

#sol = saveload.load('poincare1')

x = []
y = []

for i in range(len(sol.s)):

    zplane = 0

    try:

        if sol.z[i] < zplane and sol.z[i+1] > zplane:
            x.append(sol.x[i])
            y.append(sol.y[i])

    except IndexError:
        break


traj = plt.figure()
trajax = traj.add_subplot(111, projection='3d')
trajax.plot(sol.x, sol.y, sol.z, color='purple')
trajax.set_xlabel('x')
trajax.set_ylabel('y')
trajax.set_zlabel('z')

fig = plt.figure()
ax = fig.add_subplot()

ax.plot(x, y, 'r.')

plt.show()