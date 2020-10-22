import solvefields
import saveload
import abc_field

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

"""
sol = solvefields.abc_field(0, 1000, 0.1, [1.5, 1.5, 0], [1, np.sqrt(2/3), np.sqrt(1/3), 1])
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
"""
start = 0
end = 1000000
step = 0.1
ini = [0.2, 0.5, 0.1]
param = [1, np.sqrt(1/3), np.sqrt(2/3), 1]

#abc_field.plot_one(start, end, step, ini, param)

fog = plt.figure()
ox = fog.add_subplot()
f = solvefields.poincare(start, end, step, ini, param)
ox.scatter(f[0], f[1], marker='.', color='purple', s=0.2)

plt.show()
