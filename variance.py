import numpy as np
import chaoticfields as chaos
import matplotlib.pyplot as plt


def var_abc():

    f = chaos.line_variance(5, 10000, 0.1, [1, np.sqrt(1/3), np.sqrt(2/3), 1], 'abc')

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
    f = chaos.line_variance(5, 10000, 0.1, [1, 1, np.sqrt(1/3), np.sqrt(1/3), np.sqrt(2/3), np.sqrt(2/3), 1, -0.5], 'double')

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
    var_abc()

    plt.show()