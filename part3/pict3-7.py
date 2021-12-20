import numpy as np
import matplotlib.pyplot as plt

Fs = 30
a = 47.6
b = 22.1
L = 82.1
K = 2 * np.pi / L
l = 63.4
Zc = 120 * np.pi
x = np.linspace(0, a, Fs)
z = np.linspace(0, L, Fs)
y = np.linspace(0, b, Fs)
Ex = np.zeros((x.size, z.size))
Ey = np.zeros((x.size, z.size))
Ez = np.zeros((x.size, z.size))
Hx = np.zeros((x.size, z.size))
Hz = np.zeros((x.size, z.size))
Hy = np.zeros((x.size, z.size))
Px = np.zeros((x.size, z.size))
Py = np.zeros((x.size, z.size))
Pz = np.zeros((x.size, z.size))
for i in range(0, len(x)):
    for j in range(0, len(z)):
        Ey[i, j] = Zc * (2 * a / l) * np.sin(np.pi * x[i] / a) * np.cos(-K * z[j])
        Hx[i, j] = -(2 * a / L) * np.sin(np.pi * x[i] / a) * np.cos(-K * z[j])
        Hz[i, j] = -np.cos(np.pi * x[i] / a) * np.sin(-K * z[j])
        Px[i, j] = Ey[i, j] * Hz[i, j] - Ez[i, j] * Hy[i, j]
        Py[i, j] = Ez[i, j] * Hx[i, j] - Ex[i, j] * Hz[i, j]
        Pz[i, j] = Ex[i, j] * Hy[i, j] - Ey[i, j] * Hx[i, j]
x1, y1 = np.meshgrid(x, y)
z2, x2 = np.meshgrid(z, x)
z3, y3 = np.meshgrid(z, y)
figure, v = plt.subplots(figsize=(15, 10))
plt.quiver(x1, y1, Ex, Ey, color='red')
plt.quiver(x1, y1, Hx, Hy, color='green')
v.set_xlabel('x, мм', fontsize=16)
v.set_ylabel('y, мм', fontsize=16)
figure, v = plt.subplots(figsize=(15, 10))
plt.quiver(z2, x2, Hz, Hx, color='dodgerblue')
plt.quiver(z2, x2, Ez, Ex, color='b')
v.set_xlabel('z, мм', fontsize=16)
v.set_ylabel('x, мм', fontsize=16)
figure, v = plt.subplots(figsize=(15, 10))
plt.quiver(z3, y3, Ez, Ey, color='r')
plt.quiver(z3, y3, Hz, Hy, color='g')
v.set_xlabel('z, мм', fontsize=16)
v.set_ylabel('y, мм', fontsize=16)
figure, v = plt.subplots(figsize=(15, 10))
plt.quiver(z3, y3, Pz, Py, color='blueviolet')
v.set_xlabel('z, мм', fontsize=16)
v.set_ylabel('x, мм', fontsize=16)
figure, v = plt.subplots(figsize=(15, 10))
plt.quiver(z2, x2, -Hx, Hz, color='coral')
v.set_xlabel('z, мм', fontsize=16)
v.set_ylabel('x, мм', fontsize=16)
plt.show()
