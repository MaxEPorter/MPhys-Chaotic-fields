import numpy as np
import math
import matplotlib.pyplot as plt
import field_lines


def percen_diff(pos_ana, pos_num):
    return [100*2*abs(pos_ana[0] - pos_num[0])/(pos_ana[0] + pos_num[0]),
            100*2*abs(pos_ana[1] - pos_num[1])/(pos_ana[1] + pos_num[1]),
            100*2*abs(pos_ana[2] - pos_num[2])/(pos_ana[2] + pos_num[2])]


def cal_err(be, sol):
    r = np.sqrt(np.power(be[0], 2) + np.power(be[1], 2))
    index = int(2*math.pi*r/STEP_LENGTH)
    fin = [sol.y[0][index], sol.y[1][index], sol.y[2][index]]
    p = percen_diff(be, fin)
    for i in range(len(p)):
        p[i] = p[i] / (2*math.pi*r)

    print('start = ({}, {})'.format(be[0], be[1]))
    print('end   = ({}, {})'.format(fin[0], fin[1]))
    print('x = {:.3f}%   y = {:.3f}%'.format(p[0], p[1]))
    return p, fin


# (WIRE FIELD mu_0*I/2pi=1)
STEP_LENGTH = 0.001
START = 0
STOP = 20

steps = np.arange(start=START, stop=STOP, step=STEP_LENGTH)
# steps = np.linspace(0, 14.2, 100000)
wire_field = field_lines.MagneticField([
    lambda pos: (1/(pos[0]**2+pos[1]**2))*(-pos[1]),
    lambda pos: (1/(pos[0]**2+pos[1]**2))*(pos[0]),
    lambda pos: 0])
ini = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 1, 1], [1, 1, 2], [1, 1, 3]]

fig = plt.figure()

lines_RK = field_lines.generate_lines(steps, ini, wire_field)
lines_DOP = field_lines.generate_lines(steps, ini, wire_field, method='DOP853')

ax = fig.add_subplot(111, projection='3d')
for line, begin in zip(lines_RK, ini):
    plt.plot(line.y[0], line.y[1], line.y[2], color='blue')

    err, f = cal_err(begin, line)
    ax.scatter(f[0], f[1], f[2], color='blue')
    ax.scatter(begin[0], begin[1], begin[2], color='black')


print("____ DOP853 _____")
# ax = fig.add_subplot(111, projection='3d')
for line, begin in zip(lines_DOP, ini):
    plt.plot(line.y[0], line.y[1], line.y[2], color='red')

    err, f = cal_err(begin, line)
    ax.scatter(f[0], f[1], f[2], 'red')
    ax.scatter(begin[0], begin[1], begin[2], color='black')


plt.show()
