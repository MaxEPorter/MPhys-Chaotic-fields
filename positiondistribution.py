import numpy as np
import matplotlib.pyplot as plt
import chaoticfields as chaos
import usefulthings as use

plt.style.use('seaborn-whitegrid')

"""
FIND DISTRIBUTION OF COORDINATE SUMS 
chaos.coord_frequency(
    string method,
    double path_length,
    double step_size,
    array<3> ini,
    vector params,
    double number_of_segments)

returns array<3> of vector of x,y,z sum of each segment 

"""


def dist():

    sol = chaos.coord_frequency('double', 10000000, 0.1, [0.9*2*np.pi, 0.5*2*np.pi, 0], use.std_param_double, 100000)

    fig = plt.figure()

    ax = fig.add_subplot()
    ax.hist(sol[0], bins=300, edgecolor='dodgerblue', histtype='step', label='x')
    ax.hist(sol[1], bins=300, edgecolor='mediumseagreen', histtype='step', label='y')
    ax.hist(sol[2], bins=300, edgecolor='firebrick', histtype='step', label='z')
    ax.set_xlabel('sum')
    ax.set_ylabel('frequency')

    ax.legend()


def change_params():

    fig = plt.figure()
    ax = fig.add_subplot()

    for i in np.linspace(0, 1, 5):

        sol = chaos.coord_frequency('double', 10000000, 0.1, [0.9*2*np.pi, 0.5*2*np.pi, 0], use.k_param(i), 100000)
        ax.hist(sol[0], bins=200, edgecolor=[i, 1-i, i], histtype='step', label='k = {}'.format(i))

    ax.set_xlabel('x sum')
    ax.set_ylabel('frequency')
    ax.legend()


if __name__ == '__main__':
    #dist()
    change_params()

    plt.show()
