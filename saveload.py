import json
import solvefields

def save(sol, fname):

    tosave = {
        'field': sol.field,
        'method': sol.method,
        'step': sol.step,
        'start': sol.start,
        'params': sol.params,
        's': sol.s,
        'x': sol.x,
        'y': sol.y,
        'z': sol.z
    }

    with open('saves/{}.json'.format(fname), 'w') as outfile:
        json.dump(tosave, outfile, indent=4)


def load(fname):

    with open('saves/{}.json'.format(fname), 'r') as infile:
        data = json.load(infile)

    sol = solvefields.Solution
    sol.s = data['s']
    sol.x = data['x']
    sol.y = data['y']
    sol.z = data['z']
    sol.method = data['method']
    sol.field = data['field']
    sol.step = data['step']
    sol.params = data['params']
    sol.start = data['start']

    return sol


if __name__ == '__main__':
    # test it works
    sol = solvefields.abc_field(0, 100, 0.01, [1, 2, 3], [4, 5, 6, 7])
    print(sol.field)

    save(sol, 'test')
    l = load('test')

    print(l.field)
    print(l.s)
