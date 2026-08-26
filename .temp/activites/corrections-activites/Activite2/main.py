# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:43:26 2024

@author: cebianchi
"""

# This is a sample Python script.

# importation de numpy
# alias np
import numpy as np

# importation de math
import math

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from matplotlib import pyplot as plt


# fonction associée à la methode d'euler pour une chute avec frottement fluide sans vitesse initiale
def Euler_exp(t_max, t_min, n_t, vo, tau, g):
    # création d'un tableau vide
    # des vitesses
    # à (n_t + 1) éléments
    tab_v = np.zeros(n_t)
    # affectation de la vitesse initiale # au premier élement du tableau tab_v[0] = v0
    # calcul de delta_t
    delta_t = (t_max - t_min) / n_t
    # boucle de calcul
    # des vitesses approchées
    for i in range(n_t - 1):
        tab_v[i + 1] = (1 - delta_t / tau) * tab_v[i] + g * delta_t
    return tab_v

def Euler_Turb(t_max, t_min, n_t, vo, tau, g):
    # création d'un tableau vide
    # des vitesses
    # à (n_t + 1) éléments
    tab_v_turb = np.zeros(n_t)
    # affectation de la vitesse initiale # au premier élement du tableau tab_v[0] = v0
    # calcul de delta_t
    delta_t = (t_max - t_min) / n_t
    # boucle de calcul
    # des vitesses approchées
    for i in range(n_t - 1):
        tab_v_turb[i + 1] = tab_v_turb[i] + g * delta_t - tab_v_turb[i] * tab_v_turb[i] * delta_t / tau
    return tab_v_turb

def Vit(tab_t, tau, g):
    return g * tau * (1.0 - np.exp(- tab_t / tau))


print('toto')
# paramètres physiques
g = 9.81  # accélération de la pesanteur
h = 5.0  # hauteur initiale en m

# tracé des trajectoires
t_min = 0.0  # instant initial en s
t_max = 50.0  # instant final en s
n_t = 100  # nombre de points de calculs
vo = 0.0  # vitesse initiale en m/s
m = 1  # masse de l'objet
lamb = 0.1  # coeff de frottement
tau = m / lamb

# tableau des instants (abscisse des graphs)
tab_t = np.linspace(t_min, t_max, n_t)

tab_v = Euler_exp(t_max, t_min, n_t, vo, tau, g)
tab_vit_exacte = Vit(tab_t, tau, g)

tab_v_Turb = Euler_Turb(t_max, t_min, n_t, vo, tau, g)

# tracé de tab_v en fonction de tab_t
# option 'r-' : tracé en rouge (r)
# en reliant les points (-)
plt.figure(1)
plt.plot(tab_t, tab_v, 'r-')
plt.plot(tab_t, tab_vit_exacte, 'b--')
# affichage de la courbe

plt.xlabel('Temps (en seconde)')
plt.ylabel('Vitesse de $M$ (en mètre/seconde)')
plt.title("Chute libre avec frottements fluides et sans vitesse initiale")
plt.text(0.7 * t_max, 10.0, r'$h = ' + str(h) + '$m')
plt.text(0.7 * t_max, 5.0, r'$t_{max} = ' + str(t_max) + '$ s')
plt.text(0.7 * t_max, 15.0, r'$m = ' + str(m) + '$ kg')
plt.text(0.7 * t_max, 20.0, r'$\lambda = ' + str(lamb) + '$ kg/s')  # h = 10.0 # hauteur initiale
plt.show()

# tracé de tab_v avec turbulence en fonction de tab_t
# option 'r-' : tracé en rouge (r)
# en reliant les points (-)
plt.figure(2)
plt.plot(tab_t, tab_v_Turb, 'r-')
# affichage de la courbe

plt.xlabel('Temps (en seconde)')
plt.ylabel('Vitesse de $M$ (en mètre/seconde)')
plt.title("Chute libre en régime turbulent")
plt.text(0.7 * t_max, 10.0, r'$h = ' + str(h) + '$m')
plt.text(0.7 * t_max, 5.0, r'$t_{max} = ' + str(t_max) + '$ s')
plt.text(0.7 * t_max, 15.0, r'$m = ' + str(m) + '$ kg')
plt.text(0.7 * t_max, 20.0, r'$\lambda = ' + str(lamb) + '$ kg/s')  # h = 10.0 # hauteur initiale
plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
