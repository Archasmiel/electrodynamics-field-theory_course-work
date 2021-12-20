import matplotlib.pyplot as plt
import numpy as np

f_kr = 2*3.15 * 10**9

print(f_kr*np.sqrt(4/3)/10**9)
print(np.sqrt(3/4))
print(np.sqrt(4/3))


c = 3e8
fkr = 3.15
fkr2 = 2 * fkr
f1 = 3.64
f2 = 2 * f1
f = np.linspace(0, 10, 1000)
vf = c/np.sqrt(1-(fkr/f)**2)
vf2 = c/np.sqrt(1-(fkr2/f)**2)
fig, v = plt.subplots(figsize=(12, 7))
v.plot(f, vf, lw=2, color='darkblue')
v.plot(f, vf2, lw=2, color='blue')
v.axhline(2*c, ls='--', color='r', lw=1)
v.axhline(c, ls='--', color='r', lw=1)
v.axvline(fkr, ls='--', color='r', lw=1)
v.axvline(fkr2, ls='--', color='r', lw=1)
v.axvline(f1, ls='--', color='r', lw=1)
v.axvline(f2, ls='--', color='r', lw=1)
v.set_xlim(0, 10)
v.set_ylim(0, 1.5e9)
v.grid(ls=':', color='k')
v.set_xlabel('f, ГГц', fontsize=16)
v.set_ylabel('$v_ф$, м/с', fontsize=16)
v.text(0.1, 0.32e9, 'c', fontsize=16, color='r')
v.text(0.1, 0.62e9, '2c', fontsize=16, color='r')
v.text(1.8, 0.1e9, 'f$^{10}_{кp}$', fontsize=14, color='r')
v.text(2.45, 0.1e9, 'f$^{10}_{2c}$', fontsize=14, color='r')
v.text(4.2, 0.1e9, 'f$^{20}_{кp}$', fontsize=14, color='r')
v.text(4.85, 0.1e9, 'f$^{20}_{2c}$', fontsize=14, color='r')
plt.show()
