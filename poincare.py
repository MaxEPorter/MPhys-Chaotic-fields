import solvefields
import saveload
import abc_field
import double_abc_field

import matplotlib.pyplot as plt
import numpy as np
import pandas

plt.style.use('seaborn-whitegrid')


def poincare_one_line(start=0, end=100, step=0.1, ini=[0.2, 3.2, 1.7], param=[1, np.sqrt(2/3), np.sqrt(1/3), 1]):

    #abc_field.plot_one(start, end, step, ini, param)

    fog = plt.figure()
    ax = fog.add_subplot()
    xy = solvefields.abc_poincare(start, end, step, ini, param, "z", 0.2)

    ax.scatter(xy[0], xy[1], color='purple', s=0.05)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel(r'$\frac{x}{2 \pi}$')
    ax.set_ylabel(r'$\frac{y}{2 \pi}$')


def multi_line():
    start = 0
    end = 1000
    step = 0.1
    ini = [[i, j, k] for i in np.linspace(-10, 10, 15) for j in np.linspace(-10, 10, 15) for k in np.linspace(-10, 10, 15)]
    print(len(ini))

    param = [1, np.sqrt(1/3), np.sqrt(2/3), 1]

    points = []
    f = []
    for i in ini:
        points.append(solvefields.abc_poincare(start, end, step, i, param))
        a = [[], []]
        for x, y in zip(points[0], points[1]):
            x, y = (x/(2*np.pi), y/(2*np.pi))
            x, y = (x-int(x), y-int(y))
            a[0].append(x)
            a[1].append(y)

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


def var_abc():

    f = solvefields.line_variance(5, 10000, 0.1, [1, np.sqrt(1/3), np.sqrt(2/3), 1], 'abc')

    s = np.log10(np.array(f[0]))
    var = np.log10(np.array(f[1]))

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(s, var, color='purple')
    ax.set_xlabel(r'$\log_{10} s$')
    ax.set_ylabel(r'$\log_{10} \sigma^2$')

    a = [i for i in s if i > 2.08]
    index = len(s) - len(a)
    b = var[index:]

    try:
        p = np.polyfit(a, b, deg=1)
        fit = np.polyval(p, a)
        ax.plot(a, fit, color='black', label='{}'.format(p[0]))
        print(p)
        ax.legend()
    except:
        print('fit didnt work')


def var_double():
    f = solvefields.line_variance(5, 10000, 0.1, [1, 1, np.sqrt(1/3), np.sqrt(1/3), np.sqrt(2/3), np.sqrt(2/3), 1, -0.5], 'double')

    s = np.log10(np.array(f[0]))
    var = np.log10(np.array(f[1]))

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(s, var, color='purple')
    ax.set_xlabel(r'$\log_{10} s$')
    ax.set_ylabel(r'$\log_{10} \sigma^2$')

    a = [i for i in s if i > 1.86]
    index = len(s) - len(a)
    b = var[index:]

    try:
        p = np.polyfit(a, b, deg=1)
        fit = np.polyval(p, a)
        ax.plot(a, fit, color='black', label='{}'.format(p[0]))
        ax.legend()
    except:
        print('fit didnt work')


if __name__ == '__main__':
    poincare_one_line(0, 10000000, 0.1, [0.5*2*np.pi, 0.6*2*np.pi, 0.5*2*np.pi], [1, np.sqrt(2/3), np.sqrt(1/3), 1])
    #multi_line()
    #var_abc()
    #var_double()

    plt.show()

