import solvefields
import matplotlib.pyplot as plt
import numpy as np
import imageio
import matplotlib.animation


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
    params = [1, 2, 3, 0.5]
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
    lam = np.linspace(0.25, 0.5, 50)

    path_start = 0
    path_length = 600
    step_length = 0.1

    ini = [1, 2, 4]
    ims = []

    for i in lam:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.set_xlim3d([-200, 400])
        ax.set_xlabel('X')

        ax.set_ylim3d([-200, 200])
        ax.set_ylabel('Y')

        ax.set_zlim3d([-200, 200])
        ax.set_zlabel('Z')

        line = solvefields.abc_field(path_start, path_length, step_length, ini, [1, 2, 3, i])
        ax.plot(line.x, line.y, line.z, color='purple')
        fig.savefig('temp.png')
        plt.close()

        ims.append(imageio.imread('temp.png'))

    imageio.mimsave('test.gif', ims, fps=10)


def plot_one(ss, se, size, ini, param):
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


if __name__ == '__main__':
    # compare_methods()
    #compare_step()
    # ini_gifs()
    lambda_gifs()

    plt.show()
