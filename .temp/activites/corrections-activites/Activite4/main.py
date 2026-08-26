
# Créé par Samira, le 29/05/2023 en Python 3.7
from math import*
import numpy as np
import matplotlib.pyplot as plt

# fonction associée à la loi horaire
def z(w,lamb):
    return ((F/m)/np.sqrt((omega_0**2-w**2)**2+(lamb**2*w**2)/m**2))

# paramètres physiques
m = 1.5*10**3 #masse de la voiture kg
omega_0 = 30 #pulsation propre  rad/s
F = 300 #Oscillation forcée N

# tracé des trajectoires
omega_min = 0 # instant initial en rad/s
omega_max = 50 # instant final en rad/s
n_p = 500 # nombre de points de calculs

# tableau des instants
tab_p = np.linspace(omega_min,omega_max,n_p)

# tableau des z associés
lamb1 = 1.5*10**4 #coeff d'amortissement kg/s
tab_z1 = z(tab_p,lamb1)

# tableau des z associés
lamb2 = 3*10**4 #coeff d'amortissement kg/s
tab_z2 = z(tab_p,lamb2)

# tableau des z associés
lamb3 = 5*10**4 #coeff d'amortissement kg/s
tab_z3 = z(tab_p,lamb3)

# tracé de tab_z en fonction de tab_p
# option 'r-' : tracé en rouge (r)
# en reliant les points (-)
plt.plot(tab_p,tab_z1,'r-',label=int(lamb1))
plt.plot(tab_p,tab_z2,'g-',label=int(lamb2))
plt.plot(tab_p,tab_z3,'b-',label=int(lamb3))

# affichage de la courbe
plt.xlabel('Pulsation en rad/s')
plt.ylabel('amplitude de $M$ (en mètre)')
plt.title("Amortissement en fonction de omega")
plt.text(0.7,4.8,r'$h = 5$ mètres')
plt.text(0.7,4.4,r'$t_{max} = 1$ rad/s')
plt.xlim(omega_min,omega_max)
plt.legend()
plt.show()