import numpy as np

begin_centre = [0.5*2*np.pi, 0.5*2*np.pi, 0.5*2*np.pi]
begin_1 = [0.1*2*np.pi, 0.1*2*np.pi, 0.1*2*np.pi]
begin_2 = [0.2*2*np.pi, 0.2*2*np.pi, 0.2*2*np.pi]
begin_3 = [0.3*2*np.pi, 0.3*2*np.pi, 0.3*2*np.pi]
begin_4 = [0.4*2*np.pi, 0.4*2*np.pi, 0.4*2*np.pi]
begin_5 = [0.5*2*np.pi, 0.5*2*np.pi, 0.5*2*np.pi]
begin_6 = [0.6*2*np.pi, 0.6*2*np.pi, 0.6*2*np.pi]

begin_std_chaotic = [0.6*2*np.pi, 0.5*2*np.pi, 0*2*np.pi]

std_param_abc = [1, np.sqrt(2/3), np.sqrt(1/3), 1]
std_param_double = [1, 1, np.sqrt(2/3), np.sqrt(2/3), np.sqrt(1/3), np.sqrt(1/3), 1, -0.5]
std_param_abc_double_form = [1, 0, np.sqrt(2/3), 0, np.sqrt(1/3), 0, 1, 0]


def lin_fit(x, y):

    fitted = np.polyfit(x, y, deg=1, cov=True)
    p = fitted[0]
    cov = fitted[1]
    df = len(x) - 2
    chisqrd = 0

    for i, j in zip(x, y):
        c = pow((j - np.polyval(p, i)), 2)
        chisqrd += c

    redchisqrd = chisqrd / df

    # note the scaling factor of * (len(x) - numberOfParameters - 2)/chisqrd.
    # This is to account for an offset introduced by numpy.polyfit
    cov = cov * (len(x) - 2 - 2) / chisqrd

    perror = np.sqrt(np.diag(cov))  # diagonals of covariance matrix

    fit = np.polyval(p, x)

    print('redchisqrd: {}\np: {}\nperror: {}'.format(redchisqrd, p, perror))

    return {'fit': fit, 'p': p, 'perror': perror, 'redchisqrd': redchisqrd}
