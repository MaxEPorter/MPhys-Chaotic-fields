import solvefields
import saveload
import abc_field
import double_abc_field

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')


def one_line():
    start = 0
    end = 1000
    step = 0.1
    ini = [0.27, 0.03, 0.79]
    #param = [1, 1, np.sqrt(2/3), np.sqrt(2/3), np.sqrt(1/3), np.sqrt(1/3), 1, -0.5]
    param = [1, np.sqrt(2/3), np.sqrt(1/3), 1]

    abc_field.plot_one(start, end, step, ini, param)

    fog = plt.figure()
    ox = fog.add_subplot()
    f = solvefields.double_abc_poincare(start, end, step, ini, param)
    ox.scatter(f[0], f[1], marker='.', color='purple')#, s=0.2)


def multi_line():
    start = 0
    end = 1000
    step = 0.1
    ini = [[i, j, k] for i in np.linspace(-10, 10, 15) for j in np.linspace(-10, 10, 15) for k in np.linspace(-10, 10, 15)]
    print(len(ini))

    param = [1, np.sqrt(1/3), np.sqrt(2/3), 1]

    points = []
    for i in ini:
        points.append(solvefields.abc_poincare(start, end, step, i, param))

    fig = plt.figure()
    ax = fig.add_subplot()

    for p in points:
        ax.scatter(p[0], p[1], marker='.', color='purple')




if __name__ == '__main__':
    one_line()
    #multi_line()
    plt.show()




