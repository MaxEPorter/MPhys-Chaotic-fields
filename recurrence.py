import chaoticfields as chaos
import matplotlib.pyplot as plt
import numpy as np
import usefulthings as use

plt.style.use('seaborn-whitegrid')


def rec():

    start = 0
    end = 100000
    step = 0.1

    r = chaos.recurrence(end, step, [0.9*2*np.pi, 0.5*2*np.pi, 0], use.std_param_abc, [0.5, 0.55, 0.5], 0.1, 10)
    plt.hist(r, bins=80)
    plt.xlabel(r'$\tau$')
    plt.ylabel('frequency')


if __name__ == '__main__':
    rec()

    plt.show()