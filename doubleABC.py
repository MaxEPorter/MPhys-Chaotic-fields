import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import chaoticfields as chaos
import usefulthings as use

mpl.rcParams.update(mpl.rcParamsDefault)
plt.style.use('seaborn-whitegrid')
#plt.rcParams.update({'font.size': 22})


class DoubleABC:
    def __init__(self, a1, a2, b1, b2, c1, c2, lam1, lam2):
        self.param = [a1, a2, b1, b2, c1, c2, lam1, lam2]

    def plot_traj(self, ini, length, step):
        line = chaos.double_abc_field(0, length, step, ini, self.param)

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot(line.x, line.y, line.z, color='dodgerblue')
        ax.scatter(ini[0], ini[1], ini[2], color='black', marker='x')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')


if __name__ == '__main__':
    # test
    abc = DoubleABC(*use.std_param_abc_double_form)
    #abc.plot_traj(use.begin_centre, 10000, 0.1)
    abc.plot_traj([1, 1, 1], 100, 0.1)
    abc.plot_traj([1 + 2*np.pi, 1 + 2*np.pi, 1 + 2*np.pi], 100, 0.1)

    plt.show()
