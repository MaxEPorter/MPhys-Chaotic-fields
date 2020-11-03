import solvefields
import matplotlib.pyplot as plt
import numpy as np
import time


def times():
    start = 0
    ends = np.linspace(0, 1000, 1000)
    step = 0.1
    ini = [0.2, 3.2, 1.7]
    param = [1, 1, 1, 1, 1, 1, 1, 1]

    n_steps = ends/step

    t = []
    for i in ends:
        t0 = time.time()

        solvefields.double_abc_field(start, i, step, ini, param)

        t1 = time.time()
        t.append(t1 - t0)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(n_steps, t, color='indigo', s=0.4)
    ax.set_xlabel('number of steps')
    ax.set_ylabel('duration (s)')
    fig.text(.7, .25, '$A_1$ = {}\n$A_2$ = {}\n$B_1$ = {}\n$B_2$ = {}\n$C_1$ = {}\n$C_2$ = {}\n$\lambda_+$ = {}\n$\lambda_-$ = {}'.format(*param),
             fontsize=12,
             bbox={'facecolor': 'grey', 'alpha': 0.3, 'pad': 5})

    try:
        p = np.polyfit(n_steps, t, deg=1)
        fit = np.polyval(p, n_steps)
        m = p[0]*1e6
        c = p[1]*1e6
        ax.plot(n_steps, fit, color='black', linestyle='--', label='gradient = {:f} $ \mu s/step$\nintercept = {:f} $\mu s$'.format(m, c))
        print(p)
        ax.legend()
    except:
        print('fit didnt work')


def estimate_duration(n_steps):
    m = 6.608e-6
    return m*n_steps


def plot_one(ss, se, size, ini, param):
    line = solvefields.double_abc_field(ss, se, size, ini, param)

    fig = plt.figure()
    traj = fig.add_subplot(221, projection='3d')

    traj.plot(ini[0], ini[1], ini[2], color='black', marker='x')
    traj.plot(line.x, line.y, line.z, color='purple')
    traj.set_xlabel('x')
    traj.set_ylabel('y')
    traj.set_zlabel('z')

    x = fig.add_subplot(222)
    x.plot(line.s, line.x, color='green')
    x.set_xlabel('s')
    x.set_ylabel('x')

    y = fig.add_subplot(223)
    y.plot(line.s, line.y, color='green')
    y.set_xlabel('s')
    y.set_ylabel('y')

    z = fig.add_subplot(224)
    z.plot(line.s, line.z, color='green')
    z.set_xlabel('s')
    z.set_ylabel('z')


def plot_one_periodic(ss, se, size, ini, param):
    lw = 0.1

    print('expected time = {}'.format(estimate_duration(se/size)))
    t0 = time.time()
    line = solvefields.double_abc_field(ss, se, size, ini, param)
    lx = solvefields.periodic_projection(line.x)
    ly = solvefields.periodic_projection(line.y)
    lz = solvefields.periodic_projection(line.z)

    fig = plt.figure()

    traj = fig.add_subplot(121, projection='3d')
    traj.plot(ini[0], ini[1], ini[2], color='black', marker='x')
    traj.plot(line.x, line.y, line.z, color='green', linewidth=lw)
    traj.set_xlabel('x')
    traj.set_ylabel('y')
    traj.set_zlabel('z')

    traj_per = fig.add_subplot(122, projection='3d')
    traj_per.plot(ini[0], ini[1], ini[2], color='black', marker='x')
    traj_per.plot(lx, ly, lz, color='blue', linewidth=lw)
    traj_per.set_xlabel('$x/2\pi$')
    traj_per.set_ylabel('$y/2\pi$')
    traj_per.set_zlabel('$z/2\pi$')

    fog = plt.figure()

    x = fog.add_subplot(231)
    x.scatter(line.s, lx, color='green', s=lw)
    x.set_xlabel('s')
    x.set_ylabel('x')

    y = fog.add_subplot(232)
    y.scatter(line.s, ly, color='green', s=lw)
    y.set_xlabel('s')
    y.set_ylabel('y')

    z = fog.add_subplot(233)
    z.scatter(line.s, lz, color='green', s=lw)
    z.set_xlabel('s')
    z.set_ylabel('z')

    xy = fog.add_subplot(234)
    xy.scatter(lx, ly, color='blue', s=lw)
    xy.set_xlabel('$x/2\pi$')
    xy.set_ylabel('$y/2\pi$')

    xz = fog.add_subplot(235)
    xz.scatter(lx, lz, color='blue', s=lw)
    xz.set_xlabel('$x/2\pi$')
    xz.set_ylabel('$z/2\pi$')

    yz = fog.add_subplot(236)
    yz.scatter(ly, lz, color='blue', s=lw)
    yz.set_xlabel('$y/2\pi$')
    yz.set_ylabel('$z/2\pi$')

    t1 = time.time()
    print('time taken = {}'.format(t1-t0))


if __name__ == '__main__':
    times()
    plt.show()
