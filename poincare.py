import solvefields
import saveload
import abc_field
import double_abc_field

import matplotlib.pyplot as plt
import numpy as np
import pandas
import imageio

plt.style.use('seaborn-whitegrid')


def poincare_one_line(start=0, end=100, step=0.1, ini=[0.2, 3.2, 1.7], param=[1, np.sqrt(2/3), np.sqrt(1/3), 1]):

    abc_field.plot_one(start, end, step, ini, param)

    fog = plt.figure()
    ax = fog.add_subplot()
    xy = solvefields.abc_poincare(start, end, step, ini, param, "z", 0)

    ax.scatter(xy[0], xy[1], color='purple', s=0.05)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel(r'$\frac{x}{2 \pi}$')
    ax.set_ylabel(r'$\frac{y}{2 \pi}$')


def multi_line():
    start = 0
    end = 1000
    step = 0.1
    n = 5
    ini = [[i, j, k] for i in np.linspace(0, 2*np.pi, n) for j in np.linspace(0, 2*np.pi, n) for k in np.linspace(0, 2*np.pi, n)]

    param = [1, np.sqrt(2/3), np.sqrt(1/3), 1]

    fig = plt.figure()
    ax = fig.add_subplot()

    for i in ini:
        points = solvefields.abc_poincare(start, end, step, i, param, "z", 0)
        ax.scatter(points[0], points[1], s=0.02)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel(r'$\frac{x}{2 \pi}$')
        ax.set_ylabel(r'$\frac{y}{2 \pi}$')


def poincare_gif():
    n = 30
    start = 0
    end = 100000
    step = 0.1
    ini = [0.5*2*np.pi, 0.5*2*np.pi, 0.5*2*np.pi]
    param = [1, np.sqrt(2/3), np.sqrt(1/3), 1]
    plane = [i for i in np.linspace(0, 0.999, n)]

    ims = []
    for i in plane:

        fig = plt.figure()
        ax1 = fig.add_subplot()

        xy = solvefields.abc_poincare(start, end, step, ini, param, 'z', i)

        ax1.scatter(xy[0], xy[1], s=1, color='dodgerblue')

        # ax1.set_title('x = 0-2$\pi$')
        ax1.set_xlabel(r'x/2$\pi$')
        ax1.set_ylabel(r'y/2$\pi$')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.set_title('plane of z={:.3f}'.format(i))

        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=10)


def poincare_multi_gif():
    n = 30
    lines = 10
    start = 0
    end = 100
    step = 0.1
    ini = [[i, j, k] for i in np.linspace(0, 2*np.pi, lines) for j in np.linspace(0, 2*np.pi, lines) for k in np.linspace(0, 2*np.pi, lines)]
    param = [1, np.sqrt(2/3), np.sqrt(1/3), 1]
    plane = [i for i in np.linspace(0, 0.999, n)]

    ims = []
    for i in plane:

        fig = plt.figure()
        ax = fig.add_subplot()

        for j in ini:
            points = solvefields.abc_poincare(start, end, step, j, param, "z", i)
            ax.scatter(points[0], points[1], s=0.05)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_xlabel(r'$\frac{x}{2 \pi}$')
            ax.set_ylabel(r'$\frac{y}{2 \pi}$')
            ax.set_title('plane of z={:.3f}'.format(i))

        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=10)






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

    lyapunov_distance = 200
    lyapunov_steps = lyapunov_distance / step

    max_steps = end / step
    n_points = max_steps / lyapunov_steps
    print(n_points)

    #"""

    x = solvefields.lyapunov(end, step, ini, param)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x[0], x[1], color='green')
    ax.scatter(x[0], x[1], color='blue', s=2)
    ax.set_xlabel('s')
    ax.set_ylabel('$\lambda$')
    #"""

    #print(len(x[0]))

    """
    end = 200
    line1 = solvefields.abc_field_euler(0, end, step, ini, param)
    line2 = solvefields.abc_field_euler(0, end, step, [ini[0] + 0.000001, ini[1], ini[2]], param)

    fog = plt.figure()
    ox = fog.add_subplot()
    ox.plot(line1.s, line1.x)
    ox.plot(line2.s, line2.x)
    """

if __name__ == '__main__':
    #abc_field.plot_one(0, 10000, 0.1, [0.4*2*np.pi, 0.4*2*np.pi, 0.4*2*np.pi], [1, np.sqrt(2/3), np.sqrt(1/3), 1])
    #poincare_one_line(0, 10000, 0.1, [0.4*2*np.pi, 0.4*2*np.pi, 0.4*2*np.pi], [1, np.sqrt(2/3), np.sqrt(1/3), 1])
    multi_line()
    #poincare_multi_gif()
    #poincare_gif()
    #var_abc()
    #var_double()
    #abc_field.plot_one(0, 20000, 0.1, [0.5*2*np.pi, 0.5*2*np.pi, 0.5*2*np.pi], [1, np.sqrt(2/3), np.sqrt(1/3), 1])
    #lyapunov(20000, 0.01, [0.5*2*np.pi, 0.5*2*np.pi, 0.5*2*np.pi], [1, np.sqrt(2/3), np.sqrt(1/3), 1])

    plt.show()


