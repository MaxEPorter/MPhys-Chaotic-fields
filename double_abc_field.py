import solvefields
import matplotlib.pyplot as plt


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