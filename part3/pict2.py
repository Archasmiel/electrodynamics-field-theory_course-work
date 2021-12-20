import matplotlib.pyplot as plt
import numpy as np

K = 76.53
z = np.linspace(0, 6, 1000)
P = 0.1*np.log(np.exp(-2*K*z))
v = -30
idx = np.argwhere(np.diff(np.sign(v-P))).flatten()
fig, v = plt.subplots(figsize=(12, 7))
v.plot(z, P, color='blue')
v.axhline(-30, ls='--', color='r', lw=1)
v.grid(ls=':', color='k')
v.axvline(z[idx[0]], ls='--', color='r', lw=1)
v.set_xlabel('z, cм', fontsize=16)
v.set_ylabel('Р, дБ', fontsize=16)
print(z[idx[0]])
plt.show()