import matplotlib.pyplot as plt
import numpy as np
import chaoticfields as chaos
import usefulthings as use


def traj_split(end, step, ini, param, z0):

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


def lyapunov(end, step, ini, param):

    lyapunov_distance = 30
    lyapunov_steps = lyapunov_distance / step

    max_steps = end / step
    n_points = max_steps / lyapunov_steps
    print(n_points)

    x = chaos.lyapunov(end, step, ini, param)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.scatter(x[0], x[1], color='green')
    ax.set_xlabel('s')
    ax.set_ylabel('$\lambda$')


def lyapunov_reg(end, step, ini, param):

    z0 = 0.0000001
    lyapunov_distance = 20

    ref = chaos.abc_field(0, end, step, ini, param)

    n_steps = len(ref.s)
    index = np.arange(0, n_steps, lyapunov_distance/step)

    s = []
    lams = []

    for i in index:

        x = chaos.trajectory_split(lyapunov_distance, step, [ref.x[int(i)], ref.y[int(i)], ref.z[int(i)]], param, z0)
        #traj_split(lyapunov_distance, step, [ref.x[int(i)], ref.y[int(i)], ref.z[int(i)]], param, z0)
        p = np.polyfit(x[0], x[2], deg=1)
        lams.append(p[0])
        s.append(ref.s[int(i)])

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(s, lams, color='green')


if __name__ == '__main__':
    #traj_split(0.1, 0.001, use.begin_3, use.std_param_abc, 0.000001)
    # lyapunov(3000, 0.001, use.begin_centre, use.std_param_abc)
    lyapunov_reg(500, 0.0001, use.begin_centre, use.std_param_abc)

    plt.show()
