import numpy as np
import matplotlib.pyplot as plt
import chaoticfields as chaos
import usefulthings as use

plt.style.use('seaborn-whitegrid')


def dist():

    sol = chaos.coord_frequency('double', 10000000, 0.1, [0.9*2*np.pi, 0.5*2*np.pi, 0], use.std_param_double, 100000)


    fig = plt.figure()

    """
    x = fig.add_subplot(311)
    y = fig.add_subplot(312)
    z = fig.add_subplot(313)

    x.hist(sol[0], bins=150)
    y.hist(sol[1], bins=150)
    z.hist(sol[2], bins=150)

    x.set_xlabel('xsum')
    y.set_xlabel('ysum')
    z.set_zlabel('zsum')

    x.set_ylabel('frequency')
    x.set_ylabel('frequency')
    x.set_ylabel('frequency')
    """

    ax = fig.add_subplot()
    ax.hist(sol[0], bins=300, edgecolor='dodgerblue', histtype='step', label='x')
    ax.hist(sol[1], bins=300, edgecolor='mediumseagreen', histtype='step', label='y')
    ax.hist(sol[2], bins=300, edgecolor='firebrick', histtype='step', label='z')
    ax.set_xlabel('sum')
    ax.set_ylabel('frequency')

    ax.legend()


if __name__ == '__main__':
    dist()

    plt.show()
