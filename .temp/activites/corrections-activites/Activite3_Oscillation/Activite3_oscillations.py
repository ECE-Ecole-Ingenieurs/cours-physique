# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

L = 1.0e-3 # Inductance en Henry
C = 1e-06 # Condensateur en Farad
resistances = [1, 10, 22, 47, 68]    # Résistance en Ohms

Uc0 = 5.0   # Tension initiale aux bornes du condensateur en V
dUc0 = 0.0

# Discrétisation du temps
t_min = 0.0  # Instant initial en s
t_max = 0.001 # Instant final en s
n_t = 1000000    # Nombre de points de calculs
delta_t = (t_max - t_min) / n_t

# tableau des instants (abscisse des graphs)
tab_t = np.linspace(t_min, t_max, n_t)
tab_Uc = np.zeros(n_t)
tab_dUc = np.zeros(n_t)

tab_Uc[0] = Uc0
tab_dUc[0] = dUc0

plt.figure(1)

for R in resistances:
    for index in range(n_t - 1):
        tab_Uc[index+1] = tab_Uc[index] + delta_t * tab_dUc[index]
        tab_dUc[index+1] = tab_dUc[index] - delta_t * \
                           (R * tab_dUc[index] / L + tab_Uc[index] / (L*C))
    

    plt.plot(tab_t, tab_Uc, label=R)  # label="h = " + str(h) + " m")


plt.xlabel('Temps (en s)')
plt.ylabel('tension de $uc$  en fonction de  t (en Volts)')
plt.title("Oscillations amorties par resistance")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.legend(loc=4)
plt.show()