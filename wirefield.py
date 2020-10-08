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

    return p, fin


# (WIRE FIELD mu_0*I/2pi=1)
STEP_LENGTH = 0.001
START = 0
STOP = 20

steps = np.arange(start=START, stop=STOP, step=STEP_LENGTH)

wire_field = field_lines.MagneticField([
    lambda pos: (1/(pos[0]**2+pos[1]**2))*(-pos[1]),
    lambda pos: (1/(pos[0]**2+pos[1]**2))*(pos[0]),
    lambda pos: 0])

ini = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 1, 1], [1, 1, 2], [1, 1, 3]]

fig = plt.figure()

lines_RK = field_lines.generate_lines(steps, ini, wire_field)
lines_DOP = field_lines.generate_lines(steps, ini, wire_field, method='DOP853')

ax = fig.add_subplot(111, projection='3d')
for line_RK, line_DOP, begin in zip(lines_RK, lines_DOP, ini):

    print('start = ({}, {})'.format(begin[0], begin[1]))

    plt.plot(line_RK.y[0], line_RK.y[1], line_RK.y[2], color='blue')
    plt.plot(line_DOP.y[0], line_DOP.y[1], line_DOP.y[2], color='red')

    err_RK, f_RK = cal_err(begin, line_RK)
    err_DOP, f_DOP = cal_err(begin, line_DOP)

    ax.scatter(f_RK[0], f_RK[1], f_RK[2], color='blue')
    ax.scatter(f_DOP[0], f_DOP[1], f_DOP[2], color='red')
    print('RK end   = ({}, {})'.format(f_RK[0], f_RK[1]))
    print('x = {:.3f}%   y = {:.3f}%'.format(err_RK[0], err_RK[1]))

    print('DOP end   = ({}, {})'.format(f_DOP[0], f_DOP[1]))
    print('x = {:.3f}%   y = {:.3f}%'.format(err_DOP[0], err_DOP[1]))

    ax.scatter(begin[0], begin[1], begin[2], color='black')


u = []
v = []
w = []
for pos in ini:
    u.append(wire_field.bx([pos[0], pos[1], pos[2]], *wire_field.params))
    v.append(wire_field.by([pos[0], pos[1], pos[2]], *wire_field.params))
    w.append(wire_field.bz([pos[0], pos[1], pos[2]], *wire_field.params))
ini = np.array(ini)

u_norm = []
v_norm = []
for a, b in zip(u, v):
    mag = np.sqrt(a**2 + b**2)
    u_norm.append(a/mag)
    v_norm.append(b/mag)


ax.quiver(ini[:, 0], ini[:, 1], ini[:, 2], u_norm, v_norm, w, pivot='middle', color='black')
print(w)

arrow = field_lines.arrow_plot_3d(wire_field, xrange=[-5, 5], yrange=[-5, 5], zrange=[-5, 5], n=9)
arrow.plot([0, 0], [0, 0], [-5, 5], color='black')

"""
print("____ DOP853 _____")
# ax = fig.add_subplot(111, projection='3d')
for line, begin in zip(lines_DOP, ini):
    plt.plot(line.y[0], line.y[1], line.y[2], color='red')

    err, f = cal_err(begin, line)
    ax.scatter(f[0], f[1], f[2], 'red')
    ax.scatter(begin[0], begin[1], begin[2], color='black')
"""

plt.show()
