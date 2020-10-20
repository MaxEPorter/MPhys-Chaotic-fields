import solvefields
import numpy as np
import matplotlib.pyplot as plt


def find_order():

    start = [1, 0, 0]
    steps = np.logspace(-3, 3, 1000)
    path = 10

    expected_end = np.exp(-path)
    print(expected_end)
    gaps_rkf = []
    gaps_euler = []
    gaps_rk4 = []

    for s in steps:

        rkf = solvefields.exp_field(0, path, s, start)
        #euler = solvefields.uniform_field_euler(0, path, s, start, field)
        #rk4 = solvefields.uniform_field_rk4(0, path, s, start, field)

        gaps_rkf.append(abs(rkf.x[-1] - expected_end))
        #gaps_euler.append(abs(euler.x[-1] - expected_end))
        #gaps_rk4.append(abs((rk4.x[-1] - expected_end)))

    fig = plt.figure()
    ax = fig.add_subplot()

    print(steps)
    steps = np.log10(steps)
    gaps_rkf = np.log10(np.array(gaps_rkf))
    #gaps_euler = np.log10(np.array(gaps_euler))
    #gaps_rk4 = np.log10(np.array(gaps_rk4))

    try:
        p = np.polyfit(steps, gaps_rkf, deg=1)
        fit = np.polyval(p, steps)
        ax.plot(steps, fit, color='black')
        print(p)
    except:
        pass

    ax.plot(steps, gaps_rkf, color='purple')
    #ax.plot(steps, gaps_euler, color='blue')
    #ax.plot(steps, gaps_rk4, color='red')

    fig2 = plt.figure()
    ax2 = fig2.add_subplot()

    ax2.plot(rkf.s, rkf.x)



if __name__ == '__main__':
    find_order()

    plt.show()