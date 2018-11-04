import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='ticks')


def mandelbrot_set(x_min, x_max, y_min, y_max, precision, maxiter, horizon=2.0):
    Y, X = np.mgrid[y_min:y_max:precision, x_min:x_max:precision]  # get coordinate arrays of set
    C = X + Y * 1j  # transform the points in arrays into complex numbers
    Z = np.zeros(C.shape, np.complex64)  # array of set values
    N = np.zeros(C.shape, dtype=int)  # array of number of iterations before divergence
    for _ in range(maxiter):
        I = np.less(abs(Z), horizon)  # check which values have not diverged beyond horizon
        N[I] += 1  # increment points until divergence
        Z[I] = Z[I] ** 2 + C[I]
    N[N == maxiter] = 0
    return Z, N


x_min = -1.5
x_max = 0.5
y_min = -1
y_max = 1
precision = 0.001
maxiter = 100
Z, N = mandelbrot_set(x_min, x_max, y_min, y_max, precision, maxiter)

dpi = 72
width = 10
height = 10
fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

plt.imshow(N)
plt.show()
