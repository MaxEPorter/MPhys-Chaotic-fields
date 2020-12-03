import numpy as np
import chaoticfields as chaos
import matplotlib.pyplot as plt
import usefulthings as use

plt.style.use('seaborn-whitegrid')


def var_abc():

    f = chaos.line_variance(5, 10000, 0.1, use.begin_std_chaotic, use.std_param_abc, 'abc')

    s = np.log10(np.array(f[0]))
    var = np.log10(np.array(f[1]))

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(s, var, color='dodgerblue')
    ax.set_xlabel(r'$\log_{10} s$')
    ax.set_ylabel(r'$\log_{10} \sigma^2$')

    a = [i for i in s if i > 2.08]
    index = len(s) - len(a)
    b = var[index:]

    try:
        fitted = use.lin_fit(a, b)
        ax.plot(a, fitted['fit'], color='black', label='{:.4f} +- {:.4f}'.format(fitted['p'][0], fitted['perror'][0]))
        ax.legend()
    except:
        print('fit didnt work')


def var_double():
    f = chaos.line_variance(5, 10000, 0.1, use.begin_std_chaotic, use.std_param_double, 'double')

    s = np.log10(np.array(f[0]))
    var = np.log10(np.array(f[1]))

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(s, var, color='dodgerblue')
    ax.set_xlabel(r'$\log_{10} s$')
    ax.set_ylabel(r'$\log_{10} \sigma^2$')

    a = [i for i in s if i > 1.86]
    index = len(s) - len(a)
    b = var[index:]

    try:
        fitted = use.lin_fit(a, b)
        ax.plot(a, fitted['fit'], color='black', label='{:.4f} +- {:.4f}'.format(fitted['p'][0], fitted['perror'][0]))
        ax.legend()
    except:
        print('fit didnt work')


if __name__ == '__main__':
    #var_abc()
    var_double()


    plt.show()
