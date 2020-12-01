import chaoticfields as chaos
import numpy as np
import matplotlib.pyplot as plt
import usefulthings as use

plt.style.use('seaborn-whitegrid')


def compare_accuracy():
    start = 0
    end = 600
    step = 0.1
    ini = use.begin_centre
    param = use.std_param_abc

    line_rkf = chaos.abc_field(start, end, step, ini, param)
    line_euler = chaos.abc_field_euler(start, end, step, ini, param)
    line_rk4 = chaos.abc_field_rk4(start, end, step, ini, param)

    fig = plt.figure()
    ax = fig.add_subplot(211)

    ax.plot(line_rkf.s, line_rkf.x, color='dodgerblue', label='Runge Kutta Fehlberg, order 7')
    ax.plot(line_rk4.s, line_rk4.x, color='orangered', label='RK4, order 4')
    ax.plot(line_euler.s, line_euler.x, color='mediumseagreen', label='Euler, order 1')
    ax.set_xlabel('s')
    ax.set_ylabel('x')
    ax.set_xlim(0,end)

    ax.legend()

    ox = fig.add_subplot(212)

    end = 600
    step_length = [0.01, 0.05, 0.1, 0.5]
    colors = ['dodgerblue', 'orangered', 'mediumseagreen', 'mediumorchid']

    for i, c in zip(step_length, colors):
        line = chaos.abc_field(start, end, i, ini, param)
        ox.plot(line.s, line.x, color=c, label='step length {}'.format(i))

    ox.set_xlabel('s')
    ox.set_ylabel('x')
    ox.set_xlim(0, end)
    ox.legend()



if __name__ == '__main__':
    # compare_accuracy()


    plt.show()