import numpy as np
import matplotlib.pyplot as plt
import chaoticfields as chaos


def multi_line():
    start = 0
    end = 1000
    step = 0.1
    n = 5
    ini = [[i, j, k] for i in np.linspace(0, 2*np.pi, n) for j in np.linspace(0, 2*np.pi, n) for k in np.linspace(0, 2*np.pi, n)]

    param = [1, np.sqrt(2/3), np.sqrt(1/3), 1]
    #param = [1, 1, np.sqrt(2/3), np.sqrt(2/3), np.sqrt(1/3), np.sqrt(1/3), 1, -0.5]

    fig = plt.figure()
    ax = fig.add_subplot()

    for i in ini:
        points = chaos.abc_poincare(start, end, step, i, param, "z", 0)
        ax.scatter(points[0], points[1], s=0.02)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel(r'$\frac{x}{2 \pi}$')
        ax.set_ylabel(r'$\frac{y}{2 \pi}$')


multi_line()
plt.show()