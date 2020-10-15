import numpy as np
import solvefields
import matplotlib.pyplot as plt

# PARAMS
s_start = 0
s_end = 1000
step_length = 0.01  
x_ini = [1, 2, 1]  # initial x, y, z positions
params = [1, 2, 2, 1]  # a, b, c, lambda

abc = solvefields.abc_field(s_start, s_end, step_length, x_ini, params)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(abc[1], abc[2], abc[3])
plt.show()

