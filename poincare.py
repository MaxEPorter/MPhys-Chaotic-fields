import solvefields
import saveload
import abc_field
import double_abc_field

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')


def one_line():
    start = 0
    end = 100000
    step = 0.1
    ini = [0.27, 0.03, 0.79]
    #param = [1, 1, np.sqrt(2/3), np.sqrt(2/3), np.sqrt(1/3), np.sqrt(1/3), 1, -0.5]
    param = [1, np.sqrt(2/3), np.sqrt(1/3), 1]

    abc_field.plot_one(start, end, step, ini, param)

    fog = plt.figure()
    ox = fog.add_subplot()
    f = solvefields.abc_poincare(start, end, step, ini, param)
    print(f)
    a = [[], []]
    for x, y in zip(f[0], f[1]):
        x, y = (x/(2*np.pi), y/(2*np.pi))
        x, y = (x-int(x), y-int(y))
        a[0].append(x)
        a[1].append(y)

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


def delta(line0, line1, index):
    return np.sqrt(
        np.power(line1.x[index] - line0.x[index], 2) +
        np.power(line1.y[index] - line0.y[index], 2) +
        np.power(line1.z[index] - line0.z[index], 2)
    )


def mu(lines, index, mid):
    mub = 0
    for i in range(len(lines)):
        mub += delta(lines[mid], lines[i], index)
    mub = mub/len(lines)
    return mub


def var():
    start = 0
    end = 10000
    step = 0.1
    vol = 4  # must be odd
    ini = [[i, j, k] for i in np.linspace(-0.05, 0.05, vol) for j in np.linspace(-0.05, 0.05, vol) for k in
           np.linspace(-0.05, 0.05, vol)]
    print(ini)
    mid = int((vol**3 + 1)/2)

    param = [1, np.sqrt(1/3), np.sqrt(2/3), 1]
    lines = []
    for i in ini:
        lines.append(solvefields.abc_field(start, end, step, i, param))

    var = []
    for i in range(len(lines[0].s)):

        mub = mu(lines, i, mid)
        v = 0
        for j in range(len(lines)):
            v += np.power(delta(lines[mid], lines[j], i) - mub, 2)
        var.append(v/len(lines))

    s = np.log10(np.array(lines[0].s))
    var = np.log10(np.array(var))

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(s, var, color='purple')
    ax.set_xlabel('log10(s)')
    ax.set_ylabel('log10(variance)')


if __name__ == '__main__':
    #one_line()
    #multi_line()
    var()
    plt.show()




