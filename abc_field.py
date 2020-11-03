import solvefields
import matplotlib.pyplot as plt
import numpy as np
import imageio
import time
import saveload

#plt.style.use('seaborn-whitegrid')
#plt.style.use('Solarize_Light2')
plt.style.use('bmh')
#plt.style.use('ggplot')
#plt.style.use('dark_background')

def compare_methods():
    start = [1.3, 2.1, 4.3]
    params = [3, np.sqrt(2 / 3), np.sqrt(1 / 3), 1]

    path_start = 0
    path_length = 1000
    step_length = 0.01

    line_rkf = solvefields.abc_field(path_start, path_length, step_length, start, params)
    line_euler = solvefields.abc_field_euler(path_start, path_length, step_length, start, params)
    line_rk4 = solvefields.abc_field_rk4(path_start, path_length, step_length, start, params)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(line_rkf.x, line_rkf.y, line_rkf.z, color='purple')
    # ax.plot(line_rk4[1], line_rk4[2], line_rk4[3], color='red')
    # ax.plot(line_euler[1], line_euler[2], line_euler[3], color='blue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.grid()
    ax.legend()


def compare_step():
    start = [1, 2, 4]
    params = [1, 2, 3, 0.27]
    path_start = 0
    path_length = 600
    step_length = [0.001, 0.01, 0.1, 1]

    traj = plt.figure('trajectory 3d')
    flat = plt.figure('traj 1d')
    flat.suptitle('Result of varying step length')

    ax = traj.add_subplot(111, projection='3d')

    x = flat.add_subplot(221)
    y = flat.add_subplot(222)
    z = flat.add_subplot(223)

    ax.plot(start[0], start[1], start[2], marker='x', color='black')

    for l in step_length:
        line = solvefields.abc_field(path_start, path_length, l, start, params)
        ax.plot(line.x, line.y, line.z, label='{}'.format(l))
        x.plot(line.s, line.x, label='{} step'.format(l))
        y.plot(line.s, line.y, label='{} step'.format(l))
        z.plot(line.s, line.z, label='{} step'.format(l))

    flat.text(.6, .25,
              'start = {}\npath length = {}\nA = {}\nB = {}\nC = {}\n$\lambda$ = {}'.format(start, path_length,
                                                                                            *params),
              fontsize=16,
              bbox={'facecolor': 'grey',
                    'alpha': 0.3, 'pad': 5})

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.grid()
    ax.legend()

    x.set_xlabel('s')
    x.set_ylabel('x')
    x.grid()
    x.legend()

    y.set_xlabel('s')
    y.set_ylabel('y')
    y.grid()
    y.legend()

    z.set_xlabel('s')
    z.set_ylabel('z')
    z.grid()
    z.legend()


def animate_abc(i, s_start, s_length, step, start, params):
    l = solvefields.abc_field(s_start, s_length, step, start[i], params)
    return


def ini_gifs():
    params = [3, np.sqrt(2 / 3), np.sqrt(1 / 3), 1]

    path_start = 0
    path_length = 1000
    step_length = 0.1

    ini = [[i, 1, 1] for i in np.linspace(4, 8, 100)]
    ims = []

    for i in ini:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.set_xlim3d([0, 1000])
        ax.set_xlabel('X')

        ax.set_ylim3d([-5, 5])
        ax.set_ylabel('Y')

        ax.set_zlim3d([-5, 5])
        ax.set_zlabel('Z')

        line = solvefields.abc_field(path_start, path_length, step_length, i, params)
        ax.plot(line.x, line.y, line.z, color='purple')
        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=10)


def lambda_gifs():
    lam = np.linspace(0.25, 0.28, 100)

    path_start = 0
    path_length = 300
    step_length = 0.1

    ini = [1, 2, 4]
    ims = []

    for i in lam:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title(round(i, 4), fontsize=18, fontweight='light')

        ax.set_xlim3d([-70, 70])
        ax.set_xlabel('X')

        ax.set_ylim3d([-20, 20])
        ax.set_ylabel('Y')

        ax.set_zlim3d([0, 400])
        ax.set_zlabel('Z')

        line = solvefields.abc_field(path_start, path_length, step_length, ini, [1, 2, 3, i])
        ax.plot(line.x, line.y, line.z, color='purple')
        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=10)


def plot_one(ss, se, size, ini, param):
    print('expected time = {}'.format(estimate_duration(se/size)))
    t0 = time.time()
    line = solvefields.abc_field(ss, se, size, ini, param)

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

    t1 = time.time()
    print('time taken = {}'.format(t1-t0))


def plot_one_periodic(ss, se, size, ini, param):
    print('expected time = {}'.format(estimate_duration(se/size)))
    t0 = time.time()
    line = solvefields.abc_field(ss, se, size, ini, param)
    lx = solvefields.periodic_projection(line.x)
    ly = solvefields.periodic_projection(line.y)
    lz = solvefields.periodic_projection(line.z)

    fig = plt.figure()
    traj = fig.add_subplot(projection='3d')

    traj.plot(ini[0], ini[1], ini[2], color='black', marker='x')
    traj.plot(lx, ly, lz, color='purple', linewidth=0.1)
    traj.set_xlabel('x')
    traj.set_ylabel('y')
    traj.set_zlabel('z')

    fog = plt.figure()

    x = fog.add_subplot(221)
    x.plot(line.s, lx, color='green')
    x.set_xlabel('s')
    x.set_ylabel('x')

    y = fog.add_subplot(222)
    y.plot(line.s, ly, color='green')
    y.set_xlabel('s')
    y.set_ylabel('y')

    z = fog.add_subplot(223)
    z.plot(line.s, lz, color='green')
    z.set_xlabel('s')
    z.set_ylabel('z')

    t1 = time.time()
    print('time taken = {}'.format(t1-t0))


def multi_plot():
    ini = [[i, j, k] for i in np.linspace(-1, 1, 2) for j in np.linspace(-1, 1, 2) for k in np.linspace(-1, 1, 2)]
    lines = []
    for i in ini:
        lines.append(solvefields.abc_field(0, 1000, 0.01, i, [1, np.sqrt(1/3), np.sqrt(2/3), 1]))

    fig = plt.figure()
    x = fig.add_subplot(222)
    y = fig.add_subplot(223)
    z = fig.add_subplot(224)

    for line in lines:
        x.plot(line.s, line.x)
        z.plot(line.s, line.z)
        y.plot(line.s, line.y)

    x.set_xlabel('s')
    x.set_ylabel('x')

    y.set_xlabel('s')
    y.set_ylabel('y')

    z.set_xlabel('s')
    z.set_ylabel('z')


def times():
    start = 0
    ends = np.linspace(0, 10000, 1000)
    step = 0.1
    ini = [0.2, 3.2, 1.7]
    param = [1, 1, 1, 1]

    n_steps = ends/step

    t = []
    for i in ends:
        t0 = time.time()

        solvefields.abc_field(start, i, step, ini, param)

        t1 = time.time()
        t.append(t1 - t0)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(n_steps, t, color='indigo')
    ax.set_xlabel('number of steps')
    ax.set_ylabel('duration (s)')
    fig.text(.7, .25, 'A = {}\nB = {}\nC = {}\n$\lambda$ = {}'.format(*param),
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


def dobre_zero_c(n=1):
    # TESTING KNOWN SOLUTION OF ABC WITH C=0
    # SOLUTION DOBRE ABC FLOW PAGE 360
    start = 0
    end = 20
    step = 0.1
    a = np.linspace(0, 2 * np.pi, n)
    ini = [[i, j, k] for i in a for j in a for k in a]
    param = [1, 1, 0, 1]

    print(ini)

    print('expected time = {}s'.format(estimate_duration(n**3*end/step)))

    plot_one(start, 600, step, [1, 2, 1], param)

    fig = plt.figure()
    ax = fig.add_subplot()

    for i in ini:
        line = solvefields.abc_field(start, end, step, i, param)
        x = solvefields.periodic_projection(line.x)
        z = solvefields.periodic_projection(line.z)

        ax.scatter(x, z, s=0.1)

    ax.set_xlabel(r'x/2$\pi$')
    ax.set_ylabel(r'y/2$\pi$')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    #multi_projection(start, end, step, n=n, p=param)


def multi_projection(s=0, e=30000, st=0.1, n=1, p=[1, 2, 1, 1]):

    a = np.linspace(0, 2 * np.pi, n)
    ini = [[i, j, k] for i in a for j in a for k in a]
    print('positions = {}'.format(ini))
    start = s
    end = e
    step = st

    param = p
    print('estimated time = {}'.format(estimate_duration(n**3*end / step)))

    t0 = time.time()

    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)

    c = np.linspace(0, 1, n)

    for begin in ini:
        line = solvefields.abc_field(start, end, step, begin, param)
        x = solvefields.periodic_projection(line.x)
        y = solvefields.periodic_projection(line.y)
        z = solvefields.periodic_projection(line.z)

        ax1.scatter(x, y, s=0.1)
        ax2.scatter(x, z, s=0.1)
        ax3.scatter(y, z, s=0.1)

    v = [param[1] * np.sin(i) + param[0] * np.cos(j) for i, j in zip(line.x, line.z)]

    #ax1.set_title('x = 0-2$\pi$')
    ax1.set_xlabel(r'x/2$\pi$')
    ax1.set_ylabel(r'y/2$\pi$')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    #ax2.set_title('y = 0-2$\pi$')
    ax2.set_xlabel(r'x/2$\pi$')
    ax2.set_ylabel(r'z/2$\pi$')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    #ax3.set_title('z = 0-2$\pi$')
    ax3.set_xlabel(r'y/2$\pi$')
    ax3.set_ylabel(r'z/2$\pi$')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    t1 = time.time()
    print('time taken = {}'.format(t1-t0))


def one_projection(e=3000, st=0.1, i=[1., 1., 1.], p=[1., 2., 1., 1.]):
    start = 0
    end = e
    step = st
    ini = i
    param = p
    print('estimated time = {}'.format(estimate_duration(end / step)))

    t0 = time.time()

    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)

    line = solvefields.abc_field(start, end, step, ini, param)
    x = solvefields.periodic_projection(line.x)
    y = solvefields.periodic_projection(line.y)
    z = solvefields.periodic_projection(line.z)

    ax1.scatter(x, y, s=0.1, color='mediumpurple')
    ax2.scatter(x, z, s=0.1, color='mediumseagreen')
    ax3.scatter(y, z, s=0.1, color='steelblue')

    begin = solvefields.periodic_projection(ini)
    ax1.scatter(begin[0], begin[1], marker='x', color='black', s=20)
    ax2.scatter(begin[0], begin[2], marker='x', color='black', s=20)
    ax3.scatter(begin[1], begin[2], marker='x', color='black', s=20)

    # v = [param[1] * np.sin(i) + param[0] * np.cos(j) for i, j in zip(line.x, line.z)]

    #ax1.set_title('x = 0-2$\pi$')
    ax1.set_xlabel(r'x/2$\pi$')
    ax1.set_ylabel(r'y/2$\pi$')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    #ax2.set_title('y = 0-2$\pi$')
    ax2.set_xlabel(r'x/2$\pi$')
    ax2.set_ylabel(r'z/2$\pi$')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    #ax3.set_title('z = 0-2$\pi$')
    ax3.set_xlabel(r'y/2$\pi$')
    ax3.set_ylabel(r'z/2$\pi$')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    fig.text(.7, .25, 'A = {:.3f}\nB = {:.3f}\nC = {:.3f}\n$\lambda$ = {:.3f}'.format(*param),
             fontsize=22,
             bbox={'facecolor': 'grey', 'alpha': 0.3, 'pad': 5})

    t1 = time.time()
    print('time taken = {}'.format(t1-t0))


def test_projection():
    length = 1000
    ini = [0.5*2*np.pi, 0.2*2*np.pi, 0.2*2*np.pi]
    param = [1, 2, 1, 1]

    plot_one(0, length, 0.1, ini, param)
    one_projection(length, 0.1, ini, param)

    #saveload.save_history(0, length, 0.1, ini, param, 'field linear in 2 dimensions, with complicated periodic motion in y')


def projection_gif_ini():
    n = 30
    start = 0
    end = 100
    step = 0.1
    ini = [[i, 0.5*2*np.pi, 0.5*2*np.pi] for i in np.linspace(0, 2*np.pi, n)]
    param = [1, 1, 1, 1]

    print('expected time = {}'.format(estimate_duration(n * end/step)))
    t0 = time.time()

    ims = []
    for i in ini:

        fig = plt.figure()
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)

        line = solvefields.abc_field(start, end, step, i, param)
        x = solvefields.periodic_projection(line.x)
        y = solvefields.periodic_projection(line.y)
        z = solvefields.periodic_projection(line.z)

        ax1.scatter(x, y, s=0.1, color='mediumpurple')
        ax2.scatter(x, z, s=0.1, color='mediumseagreen')
        ax3.scatter(y, z, s=0.1, color='steelblue')

        begin = solvefields.periodic_projection(i)
        ax1.scatter(begin[0], begin[1], marker='x', color='black', s=20)
        ax2.scatter(begin[0], begin[2], marker='x', color='black', s=20)
        ax3.scatter(begin[1], begin[2], marker='x', color='black', s=20)

        # v = [param[1] * np.sin(i) + param[0] * np.cos(j) for i, j in zip(line.x, line.z)]

        # ax1.set_title('x = 0-2$\pi$')
        ax1.set_xlabel(r'x/2$\pi$')
        ax1.set_ylabel(r'y/2$\pi$')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)

        # ax2.set_title('y = 0-2$\pi$')
        ax2.set_xlabel(r'x/2$\pi$')
        ax2.set_ylabel(r'z/2$\pi$')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        # ax3.set_title('z = 0-2$\pi$')
        ax3.set_xlabel(r'y/2$\pi$')
        ax3.set_ylabel(r'z/2$\pi$')
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)

        fig.text(.6, .2, 'A = {:.3f}\nB = {:.3f}\nC = {:.3f}\n$\lambda$ = {:.3f}'.format(*param),
                 fontsize=14,
                 bbox={'facecolor': 'grey', 'alpha': 0.3, 'pad': 5})

        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=10)

    t1 = time.time()
    print('time taken = {}'.format(t1-t0))


def projection_one_plane_ini():
    n = 90
    start = 0
    end = 500
    step = 0.1
    ini = [[i, 0.5 * 2 * np.pi, 0.5 * 2 * np.pi] for i in np.linspace(0, 2 * np.pi, n)]
    param = [1, 5, 1, 1]
    color = [(0.8, 0.6, i, 1) for i in np.linspace(0.5, 0.8, n)]

    print('expected time = {}'.format(estimate_duration(n * end / step)))
    t0 = time.time()

    ims = []
    for i, c in zip(ini, color):
        fig = plt.figure()
        ax1 = fig.add_subplot()

        line = solvefields.abc_field(start, end, step, i, param)
        x = solvefields.periodic_projection(line.x)
        y = solvefields.periodic_projection(line.y)
        z = solvefields.periodic_projection(line.z)

        ax1.scatter(y, z, s=0.5, color=c)#'springgreen')

        begin = solvefields.periodic_projection(i)
        ax1.scatter(begin[0], begin[1], marker='x', color='black', s=20)

        # v = [param[1] * np.sin(i) + param[0] * np.cos(j) for i, j in zip(line.x, line.z)]

        # ax1.set_title('x = 0-2$\pi$')
        ax1.set_xlabel(r'x/2$\pi$')
        ax1.set_ylabel(r'y/2$\pi$')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)

        fig.text(.6, .2, 'A = {:.3f}\nB = {:.3f}\nC = {:.3f}\n$\lambda$ = {:.3f}'.format(*param),
                 fontsize=14,
                 bbox={'facecolor': 'grey', 'alpha': 0.3, 'pad': 5})

        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=10)

    t1 = time.time()
    print('time taken = {}'.format(t1 - t0))


def projection_gif_param():
    n = 30
    start = 0
    end = 1000
    step = 0.1
    ini = [0.2*2*np.pi, 0.2*2*np.pi, 0.5*2*np.pi]
    param = [[1, 1, 1, i] for i in np.linspace(0, 10, n)]

    print('expected time = {}'.format(estimate_duration(n * end/step)))
    t0 = time.time()

    ims = []
    for i in param:

        fig = plt.figure()
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)

        line = solvefields.abc_field(start, end, step, ini, i)
        x = solvefields.periodic_projection(line.x)
        y = solvefields.periodic_projection(line.y)
        z = solvefields.periodic_projection(line.z)

        ax1.scatter(x, y, s=0.1, color='magenta')
        ax2.scatter(x, z, s=0.1, color='mediumseagreen')
        ax3.scatter(y, z, s=0.1, color='dodgerblue')

        begin = solvefields.periodic_projection(ini)
        ax1.scatter(begin[0], begin[1], marker='x', color='black', s=20)
        ax2.scatter(begin[0], begin[2], marker='x', color='black', s=20)
        ax3.scatter(begin[1], begin[2], marker='x', color='black', s=20)

        # v = [param[1] * np.sin(i) + param[0] * np.cos(j) for i, j in zip(line.x, line.z)]

        # ax1.set_title('x = 0-2$\pi$')
        ax1.set_xlabel(r'x/2$\pi$')
        ax1.set_ylabel(r'y/2$\pi$')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)

        # ax2.set_title('y = 0-2$\pi$')
        ax2.set_xlabel(r'x/2$\pi$')
        ax2.set_ylabel(r'z/2$\pi$')
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)

        # ax3.set_title('z = 0-2$\pi$')
        ax3.set_xlabel(r'y/2$\pi$')
        ax3.set_ylabel(r'z/2$\pi$')
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)

        fig.text(.6, .2, 'A = {:.3f}\nB = {:.3f}\nC = {:.3f}\n$\lambda$ = {:.3f}'.format(*i),
                 fontsize=14,
                 bbox={'facecolor': 'grey', 'alpha': 0.3, 'pad': 5})

        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=10)

    t1 = time.time()
    print('time taken = {}'.format(t1-t0))


def estimate_duration(n_steps):
    m = 6.608e-6
    return m*n_steps


if __name__ == '__main__':
    # compare_methods()
    # compare_step()
    # ini_gifs()
    # lambda_gifs()
    # multi_plot()
    # times()
    # dobre_zero_c()
    # projection()
    #plot_one(0, 10000, 0.1, [0.3*2*np.pi, 0.2*2*np.pi, 0.2*2*np.pi], [1, 2, 1, 1])
    plot_one_periodic(0, 10000, 0.1, [0.3*2*np.pi, 0.2*2*np.pi, 0.2*2*np.pi], [1, 2, 3, 4])

    # multi_projection(s=0, e=3000, st=0.1, n=5, p=[1, 2, 1, 1])
    #test_projection()
    #projection_gif()
    #projection_one_plane_ini()
    #projection_gif_param()
    # dobre_zero_c(9)


    plt.show()
