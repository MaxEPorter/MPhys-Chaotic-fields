import chaoticfields as chaos
import matplotlib.pyplot as plt
import numpy as np
import usefulthings as use
import abc_field
import double_abc_field

plt.style.use('seaborn-whitegrid')

"""
RECURRENCE LENGTH
chaos.recurrence(
    string method
    double end
    double step
    array<3> ini
    vector params
    array<3> sphere pos
    double sphere rad
    int n
returns vector of recurrence lengths
"""


def rec():

    end = 100000
    step = 0.1
    ini = [0.9*2*np.pi, 0.5*2*np.pi, 0]
    spherepos = [0.5, 0.55, 0.5]
    sphererad = 0.2
    n = 10

    r = chaos.recurrence('abc', end, step, ini, use.std_param_abc, spherepos, sphererad, n)
    q = chaos.recurrence('double', end, step, ini, use.std_param_double, spherepos, sphererad, n)

    rhist = np.histogram(r, bins=300)
    qhist = np.histogram(q, bins=300)

    abc = [0]
    double = [0]
    count = 0
    for i, j in zip(reversed(rhist[0]), reversed(qhist[0])):
        print(i)
        abc.append(abc[count] + i)
        double.append(double[count] + j)
        count += 1

    abc.reverse()
    double.reverse()

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(rhist[1], abc, color='dodgerblue', label='abc')
    ax.plot(qhist[1], double, color='mediumseagreen', label='double')
    ax.set_yscale('log')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('cumulative frequency')
    ax.legend()

    #abc_field.plot_one(0, end, step, [0.9*2*np.pi, 0.5*2*np.pi, 0], use.std_param_abc)
    #double_abc_field.plot_one(0, end, step, [0.9*2*np.pi, 0.5*2*np.pi, 0], use.std_param_double)


def change_params():

    end = 10000
    step = 0.1
    ini = [0.9*2*np.pi, 0.5*2*np.pi, 0]
    spherepos = [0.5, 0.55, 0.5]
    sphererad = 0.2
    n = 10
    params = [[1, i, np.sqrt(2/3), i*np.sqrt(2/3), np.sqrt(1/3), i*np.sqrt(1/3), 1, -0.5] for i in np.linspace(0, 1, 5)]

    fig = plt.figure()
    ax = fig.add_subplot()

    for i, col in zip(params, np.linspace(0, 1, 5)):
        r = chaos.recurrence('double', end, step, ini, i, spherepos, sphererad, n)

        rhist = np.histogram(r, bins=300)

        y = [0]
        count = 0
        for j in reversed(rhist[0]):
            y.append(y[count] + j)
            count += 1

        y.reverse()

        ax.plot(rhist[1], y, color=[0, col, 0.3], label='k = {}'.format(col))

    ax.set_yscale('log')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('cumulative frequency')
    ax.legend()


if __name__ == '__main__':
    #rec()
    change_params()

    plt.show()
