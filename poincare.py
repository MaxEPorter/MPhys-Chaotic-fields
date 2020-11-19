import chaoticfields as chaos
import saveload
import abc_field
import double_abc_field
import usefulthings as use

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


def multi_line(start, end, step, n, param):

    ini = [[i, j, k] for i in np.linspace(0, 2*np.pi, n) for j in np.linspace(0, 2*np.pi, n) for k in np.linspace(0, 2*np.pi, n)]

    fig = plt.figure()
    ax = fig.add_subplot()

    for i in ini:
        points = chaos.abc_poincare(start, end, step, i, param, "z", 0)
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


def poincare_multi_gif_plane():
    n = 30
    lines = 5
    start = 0
    end = 1000
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


def poincare_multi_gif_param():
    n = 20
    lines = 8
    start = 0
    end = 10000
    step = 0.1
    ini = [[i, j, k] for i in np.linspace(0, 2*np.pi, lines) for j in np.linspace(0, 2*np.pi, lines) for k in np.linspace(0, 2*np.pi, lines)]
    params = [[i, np.sqrt(2/3), np.sqrt(1/3), 1] for i in np.linspace(0, 0.1, n)]
    plane = 0

    ims = []
    for i in params:

        fig = plt.figure()
        ax = fig.add_subplot()

        for j in ini:
            points = chaos.abc_poincare(start, end, step, j, i, "z", plane)
            ax.scatter(points[0], points[1], s=0.05)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_xlabel(r'$\frac{x}{2 \pi}$')
            ax.set_ylabel(r'$\frac{y}{2 \pi}$')
            ax.set_title('A = {:.3f}'.format(i[0]))

        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=2)



if __name__ == '__main__':

    # poincare_one_line(0, 10000, 0.1, [0.4*2*np.pi, 0.4*2*np.pi, 0.4*2*np.pi], [1, np.sqrt(2/3), np.sqrt(1/3), 1])
    #multi_line(0, 1000, 0.1, 10, [0, np.sqrt(2/3), np.sqrt(1/3), 1])
    # poincare_multi_gif()
    # poincare_gif()
    poincare_multi_gif_param()




    plt.show()

