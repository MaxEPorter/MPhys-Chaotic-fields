import matplotlib.pyplot as plt
import numpy as np
import chaoticfields as chaos
import usefulthings as use

#plt.style.use('bmh')
plt.style.use('ggplot')

def traj_split(end, step, ini, param, z0):

    """

    x = chaos.trajectory_split(end, step, ini, param, z0)

    fig = plt.figure()
    ax = fig.add_subplot(121)
    ox = fig.add_subplot(122)
    ax.plot(x[0], x[1], color='green')
    ox.plot(x[0], x[2], color='blue')

    try:
        p = np.polyfit(x[0], x[2], deg=1)
        fit = np.polyval(p, x[0])
        ox.plot(x[0], fit, color='black', label='{}'.format(p[0]))
        print(p)
        ax.legend()
    except:
        print('fit didnt work')
    """

    refline = chaos.abc_field(0, end, step, ini, param)
    divline = chaos.abc_field(0, end, step, [ini[0] + z0, ini[1], ini[2]], param)
    dis = []

    for i in range(len(refline.s)):

        mag = np.power(refline.x[i] - divline.x[i], 2) + np.power(refline.y[i] - divline.y[i], 2) + np.power(refline.z[i] - divline.z[i], 2)
        dis.append(np.sqrt(mag))

    log = np.log(np.array(dis))

    fig = plt.figure()

    ax1 = fig.add_subplot(231)
    ax1.plot(refline.s, refline.x, 'r')
    ax1.plot(divline.s, divline.x, 'b')
    ax1.set_xlabel('s')
    ax1.set_ylabel('x')

    ax2 = fig.add_subplot(232)
    ax2.plot(refline.s, refline.y, 'r')
    ax2.plot(divline.s, divline.y, 'b')
    ax2.set_xlabel('s')
    ax2.set_ylabel('y')

    ax3 = fig.add_subplot(233)
    ax3.plot(refline.s, refline.z, 'r')
    ax3.plot(divline.s, divline.z, 'b')
    ax3.set_xlabel('s')
    ax3.set_ylabel('z')

    ax4 = fig.add_subplot(234)
    ax4.plot(refline.s, dis)
    ax4.set_xlabel('s')
    ax4.set_ylabel(r'$\delta x$')

    ax5 = fig.add_subplot(235)
    ax5.plot(refline.s, log)
    ax5.set_xlabel('s')
    ax5.set_ylabel(r'$\log(\delta x)$')
    try:
        p = np.polyfit(refline.s, log, deg=1)
        fit = np.polyval(p, refline.s)
        ax5.plot(refline.s, fit, color='black', label='{}'.format(p[0]))
        print(p)
        ax5.legend()
    except:
        print('fit didnt work')

    fig.text(.7, .25,
              'A = {}\nB = {}\nC = {}\n$\lambda$ = {}'.format(*param),
              fontsize=16,
              bbox={'facecolor': 'grey',
                    'alpha': 0.3, 'pad': 5})


def lyapunov(end, step, ini, param):

    x = chaos.lyapunov(end, step, ini, param)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.scatter(x[0], x[1], color='green')
    ax.set_xlabel('s')
    ax.set_ylabel('$\lambda$')


def lyapunov_regression(end, step, ini, param):

    z0 = 0.0000001
    lyapunov_distance = 100
    n_points = 400

    reference = chaos.abc_field(0, end, step, ini, param)

    n_steps = int(end/step)
    index = np.linspace(0, n_steps-1, n_points)
    s = np.linspace(0, end, n_points)

    lams = []

    for i in index:

        refline = chaos.abc_field(0, lyapunov_distance, step, ini, param)
        divline = chaos.abc_field(0, lyapunov_distance, step, [ini[0] + z0, ini[1], ini[2]], param)
        ini = [reference.x[int(i)], reference.y[int(i)], reference.z[int(i)]]

        log = chaos.line_distance(refline, divline)

        p = np.polyfit(refline.s, log, deg=1)
        lams.append(p[0])

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(s, lams, color='green')
    ax.set_xlabel('s')
    ax.set_ylabel(r'$\lambda$')


if __name__ == '__main__':
    traj_split(50, 0.1, use.begin_4, use.std_param_abc, 0.0001)
    #lyapunov(10000, 0.1, use.begin_centre, use.std_param_abc)
    #lyapunov_regression(5000, 0.1, use.begin_centre, use.std_param_abc)

    plt.show()
