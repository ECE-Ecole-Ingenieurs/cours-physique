# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


prenom = 'titi'
# prenom.upper()
print(f'{prenom}')
toto = type('prenom')
print(f'{toto}')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# fonction associée à la loi horaire
def z(t, g, h):
    return - 0.5 * g * t * t + h

# fonction associée à l'energie cinétique'
def Ec(t, g):
    return 1/2 * g**2 * t**2

# fonction associée à l'energie potentielle'
def Ep(t, g, h):
    return -1/2 * g *g * t*t + h*g

# fonction associée à l'énergie mécanique par unité de masse
def Em(t,g,h) :
    return np.add(Ec(t,g),Ep(t,g,h))


# fonction qui calcule la trajectoire d'un point soumis à son poids avec une vitesse vo
def Traj(x, vo_norme, alpha, g, h) :
    return - 1/2 * g * x**2 / ( vo_norme * math.cos(alpha)) **2 + x * math.tan(alpha) + h

# paramètres physiques
g = 9.81  # accélération de la pesanteur
h1 = 1.0  # hauteur initiale en m
h2 = 5.0  # hauteur initiale en m
# h3 = 10.0  # hauteur initiale en m

# tracé des trajectoires
t_min = 0.0  # instant initial en s
t_max = 1.0  # instant final en s
n_t = 10  # nombre de points de calculs

# tableau des instants
tab_t1 = np.linspace(t_min, t_max, n_t)
# tab_t2 = np.linspace(t_min, t_max, n_t)
# tab_t3 = np.linspace(t_min, t_max, n_t)

# tableau des abscisses
x_min = 0.0
x_max = 1.0
n_x = 10
tab_x = np.linspace(x_min, x_max, n_x)
# vo vitesse intiale
vo_abs = 5
vo_ord = 5
vo_norme = math.sqrt(vo_abs**2 + vo_ord**2)
print(vo_norme)


# tableau des z associés
tab_z1 = z(tab_t1, g, h1)
tab_z2 = z(tab_t1, g, h2)
# tab_z3 = z(tab_t3, g, h3)

# tableaux des Energies associées
tab_Ec = Ec(tab_t1, g)
tab_Ep = Ep(tab_t1, g, h1)
tab_Em = Em(tab_t1, g, h1)



# Saisie ecran alpha
# alpha = input('Quel angle alpha ? (sans cast)')
alpha = 30
print(alpha)

# trajectoire de M lancé avec vitesse vo et angle alpha
tab_trajz4 = Traj(tab_x, vo_norme, alpha, g, h1)

# tracé de tab_z en fonction de tab_t
# option 'r-' : tracé en rouge (r)
# en reliant les points (-)
plt.figure(1)
plt.plot(tab_t1, tab_z1, 'ro-')
plt.plot(tab_t1,tab_z2,'bo-')
# plt.plot(tab_t3,tab_z3,'r-')
# affichage de la courbe

plt.xlabel('Temps (en seconde)')
plt.ylabel('Position de $M$ (en mètre)')
plt.title("Chute libre sans frottement et sans vitesse initiale")
plt.text(0.7, 0.8, r'$h = 5$ mètres')
plt.text(0.7, 0.6, r'$t_{max} = 1$ seconde')
plt.legend(loc='upper right')
plt.show()

plt.figure(2)
plt.plot(tab_t1, tab_Ec, 'r-',label="énergie cinétique par unité de masse")
plt.plot(tab_t1, tab_Ep, 'b-',label="énergie potentielle par unité de masse")
plt.plot(tab_t1, tab_Em, 'ko-',label="énergie mécanique par unité de masse")
plt.xlabel('Temps (en seconde)')
plt.ylabel('Energies')
plt.legend(loc='upper right')
plt.show()


plt.figure(3)
plt.plot(tab_t1, tab_trajz4, 'r-',label="trajectoire de M lancé avec vo et angle alpha")
plt.xlabel('abscisse du point M')
plt.ylabel('cote du point M')
plt.legend(loc='upper right')
plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/