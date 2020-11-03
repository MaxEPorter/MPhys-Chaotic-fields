import json
import solvefields
import numpy as np


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
        json.dump(tosave, outfile)


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


def save_history(start, end, step, ini, param, note):
    with open('saves/history.json', 'r') as file:
        data = json.load(file)
        id = data['abc'][-1]['id'] + 1
        data['abc'].append({
            'id': id,
            'note': note,
            'start': start,
            'end': end,
            'step': step,
            'ini': ini,
            'param': param
        })

    with open('saves/history.json', 'w') as file:
        json.dump(data, file, indent=4)


def read_history(field, id):
    with open('saves/history.json', 'r') as file:
        data = json.load(file)
        for i in data[field]:
            if i['id'] == id:
                return i



if __name__ == '__main__':
    # test it works
    #save_history(0, 1000, 0.1, [0.3*2*np.pi, 0.2*2*np.pi, 0.2*2*np.pi], [1, 2, 3, 4], 'frequent regular vortices in xy plane')
    print(read_history('abc', 0)['note'])
