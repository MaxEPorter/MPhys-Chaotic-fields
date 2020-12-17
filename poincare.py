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
plt.rcParams["font.family"] = "serif"

"""
POINCARE PLOTS
choas.poincare(
    double start,
    double path_length,
    double step_size,
    array<3> ini,
    vector params,
    string plane x,y,z,
    double plane_value)
returns array<vector, 2> of x,y points crossing plane    
"""


def poincare_one_line(method, start, end, step, ini, param, plane, planevalue):

    abc_field.plot_one(start, end, step, ini, param)

    fog = plt.figure()
    ax = fog.add_subplot()
    xy = chaos.abc_poincare(method, start, end, step, ini, param, plane, planevalue)

    ax.scatter(xy[0], xy[1], color='dodgerblue', s=0.1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.set_xlabel(r'$\frac{x}{2 \pi}$')
    ax.set_ylabel(r'$\frac{z}{2 \pi}$')


def multi_line(method, start, end, step, n, param, plane, planevalue):

    ini = [[i, j, k] for i in np.linspace(0, 2*np.pi, n) for j in np.linspace(0, 2*np.pi, n) for k in np.linspace(0, 2*np.pi, n)]

    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot()

    for i in ini:
        points = chaos.abc_poincare(method, start, end, step, i, param, plane, planevalue)
        ax.scatter(points[0], points[1], s=0.02)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    if plane == 'z':
        xl = r'$\frac{x}{2 \pi}$'
        yl = r'$\frac{y}{2 \pi}$'
    elif plane == 'y':
        xl = r'$\frac{x}{2 \pi}$'
        yl = r'$\frac{z}{2 \pi}$'
    elif plane == 'x':
        xl = r'$\frac{y}{2 \pi}$'
        yl = r'$\frac{z}{2 \pi}$'
    else:
        xl = '?'
        yl = '?'

    ax.set_xlabel(xl, fontsize=16)
    ax.set_ylabel(yl, fontsize=16)

    if method == 'abc':
        ax.text(.83, .83, 'A = {:.2f} \nB = {:.2f} \nC = {:.2f} \n$\lambda$ = {:.2f}'.format(*param),
                fontsize=14,
                bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 5})

    plt.savefig('test.png')


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
    n = 40
    lines = 6
    start = 0
    end = 10000
    step = 0.1
    ini = [[i, j, k] for i in np.linspace(0, 2*np.pi, lines) for j in np.linspace(0, 2*np.pi, lines) for k in np.linspace(0, 2*np.pi, lines)]
    param = [1, 0.3*1, np.sqrt(2/3), 0, np.sqrt(1/3), 0, 1, -0.5]
    plane = [i for i in np.linspace(0, 0.999, n)]

    ims = []
    for i in plane:

        fig = plt.figure()
        ax = fig.add_subplot()

        for j in ini:
            points = chaos.abc_poincare('double', start, end, step, j, param, "z", i)
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
    n = 30
    lines = 6
    start = 0
    end = 10000
    step = 0.1
    ini = [[i, j, k] for i in np.linspace(0, 2*np.pi, lines) for j in np.linspace(0, 2*np.pi, lines) for k in np.linspace(0, 2*np.pi, lines)]
    params = [[1, k, np.sqrt(2/3), k*np.sqrt(2/3), np.sqrt(1/3), k*np.sqrt(1/3), 1, -0.5] for k in np.linspace(0, 0.3, n)]
    plane = 0

    ims = []
    for i in params:

        fig = plt.figure()
        ax = fig.add_subplot()

        for j in ini:
            points = chaos.abc_poincare('double', start, end, step, j, i, "z", plane)
            ax.scatter(points[0], points[1], s=0.05)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_xlabel(r'$\frac{x}{2 \pi}$')
            ax.set_ylabel(r'$\frac{y}{2 \pi}$')
            ax.set_title('k = {:.3f}'.format(i[1]))

        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=5)


if __name__ == '__main__':

    # poincare_one_line('abc', 0, 10000, 0.1, use.phase_pos(0.6, 0.4, 0), [1, 1, 1, 1], "z", 0)
    multi_line('double', 0, 10000, 0.1, 8, use.k_param(0.33), 'z', 0)
    # poincare_multi_gif_plane()
    # poincare_gif()
    # poincare_multi_gif_param()

    plt.show()

