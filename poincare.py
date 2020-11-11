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
    xy = solvefields.abc_poincare(start, end, step, ini, param, "z", 0.5)

    ax.scatter(xy[0], xy[1], color='purple', s=0.05)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel(r'$\frac{x}{2 \pi}$')
    ax.set_ylabel(r'$\frac{y}{2 \pi}$')


def multi_line():
    start = 0
    end = 100
    step = 0.1
    n = 30
    ini = [[i, j, k] for i in np.linspace(0, 2*np.pi, n) for j in np.linspace(0, 2*np.pi, n) for k in np.linspace(0, 2*np.pi, n)]

    param = [1, np.sqrt(2/3), np.sqrt(1/3), 1]

    fig = plt.figure()
    ax = fig.add_subplot()

    for i in ini:
        points = solvefields.abc_poincare(start, end, step, i, param, "z", 0)
        ax.scatter(points[0], points[1], color='purple', s=0.05)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel(r'$\frac{x}{2 \pi}$')
        ax.set_ylabel(r'$\frac{y}{2 \pi}$')


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


def lyapunov(end, step, ini, param):

    x = solvefields.lyapunov(end, step, ini, param)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.scatter(x[0], x[1], color='green', s=2)
    ax.set_xlabel('s')
    ax.set_ylabel('$\lambda$')

    print(len(x[0]))


if __name__ == '__main__':
    #poincare_one_line(0, 100000, 0.1, [0.5*2*np.pi, 0.5*2*np.pi, 0.5*2*np.pi], [1, np.sqrt(2/3), np.sqrt(1/3), 1])
    multi_line()
    #var_abc()
    #var_double()
    #abc_field.plot_one(0, 10000, 0.1, [0.1, 0.1, 0.1], [1, np.sqrt(2/3), np.sqrt(1/3), 1])
    #lyapunov(20000, 0.0001, [0.1, 0.1, 0.1], [1, np.sqrt(2/3), np.sqrt(1/3), 1])

    plt.show()

