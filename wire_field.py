import solvefields
import matplotlib.pyplot as plt
import numpy as np
import math

plt.style.use('bmh')

ROTATIONS = 1


def get_pos(solution):
    return [solution[1], solution[2], solution[3]]


def percentage_difference(pos_ana, pos_num):
    return [100 * 2 * abs(pos_ana[0] - pos_num[0]) / (pos_ana[0] + pos_num[0]),
            100 * 2 * abs(pos_ana[1] - pos_num[1]) / (pos_ana[1] + pos_num[1]),
            0
            ]


def circumference(x: list):
    return 2 * math.pi * np.sqrt(x[0] ** 2 + x[1] ** 2)


def calc_error(start_pos, solution):
    circ = circumference(start_pos)
    index = -1
    end = [solution[1][index], solution[2][index], solution[3][index]]
    p_diff = percentage_difference(start_pos, end)

    return p_diff


def generate_starts(y=[1, 3], z=[0, 3]):
    begin = []
    for i in np.arange(0, 3, 1):
        for j in np.arange(1, 3, 0.5):
            begin.append([0, j, i])
    return begin


def get_step_lengths(solution):
    t = solution.s
    lengths = []

    for i in range(len(solution.s)):
        try:
            lengths.append(solution.s[i + 1] - solution.s[i])
        except IndexError:
            break

    del t[-1]

    return lengths, t


def vary_steps(rot=ROTATIONS):
    start = [10, 0, 0]
    # steps = np.linspace(0.001, 2, 400)
    steps = np.logspace(-3, 0, 500)
    path_length = rot * circumference(start)
    space = []

    for step in steps:
        line = solvefields.wire_field(0, path_length, step, start)
        end = [line.x[-1], line.y[-1], line.z[-1]]

        print(step)

        # get difference in start and end
        gap = np.array(start) - np.array(end)
        space.append(gap.dot(gap))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(steps, space)
    ax.set_xscale('log')
    ax.set_xlabel('step size')
    ax.set_ylabel('distance')
    ax.grid()

    # fig = plt.figure()
    # ax2 = fig.add_subplot(111)
    # circle = plt.Circle((0, 0), 1, color='black', fill=False)
    # ax2.plot(start[0], start[1], marker='x', color='b')
    # ax2.plot(end[0], end[1], marker='x', color='r')

    # ax2.add_artist(circle)
    # ax2.plot(line.x, line.y, color='purple')#, linewidth=0.1)
    # ax2.set_xlabel('x')
    # ax2.set_ylabel('y')

    # ax2.grid()


def one_loop(rot=ROTATIONS):
    r = 0.5
    start = [r, 0, 0]
    step = 0.01
    path_length = rot * circumference(start)
    line = solvefields.wire_field(0, path_length, step, start)
    end = [line.x[-1], line.y[-1], line.z[-1]]

    fig = plt.figure()
    ax2 = fig.add_subplot(111)
    circle = plt.Circle((0, 0), r, color='black', fill=False)
    ax2.plot(start[0], start[1], marker='x', color='b')
    ax2.plot(end[0], end[1], marker='x', color='r')

    ax2.add_artist(circle)
    ax2.plot(line.x, line.y, color='purple', linewidth=0.1)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')

    ax2.grid()


def plot_step_lengths(rot=ROTATIONS):
    start = [1, 0, 0]
    step = 0.1
    path_length = rot * circumference(start)
    line = solvefields.wire_field(0, path_length, step, start)

    steps, s = get_step_lengths(line)
    print(steps)
    print(s)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(s, steps, color='green')
    ax.set_xlabel('path length')
    ax.set_ylabel('step length')
    ax.grid()


def compare_methods(rot=ROTATIONS):
    r = 1000
    start = [r, 0, 0]
    step = 0.1
    path_length = rot * circumference(start)
    line_rkf = solvefields.wire_field(0, path_length, step, start)
    # line_euler = solvefields.wire_field_euler(0, path_length, step, start)
    line_rk4 = solvefields.wire_field_rk4(0, path_length, step, start)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(r, 0, marker='x', color='black')
    circle = plt.Circle((0, 0), r, color='black', fill=False)
    ax.add_artist(circle)

    ax.plot(line_rkf.x, line_rkf.y, color='red', label='rkf', linewidth=0.2)
    # ax.plot(line_euler.x, line_euler.y, color='blue', label='euler')
    ax.plot(line_rk4.y, line_rk4.y, color='green', label='rk4', linewidth=0.2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()
    plt.legend()

    print('rkf final --> x:{}   y:{}'.format(line_rkf.x[-1], line_rkf.y[-1]))
    print('rk4 final --> x:{}   y:{}'.format(line_rk4.x[-1], line_rk4.y[-1]))


if __name__ == '__main__':
    vary_steps(10)
    # one_loop(1000)
    # plot_step_lengths(1)
    # compare_methods(100)

    plt.show()




