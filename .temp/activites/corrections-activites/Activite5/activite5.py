#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:15:24 2024

@author: bfonton
"""

import numpy as np

# QUESTION 1

def produit_matriciel(A, B):

    m = A.shape[0]
    n = A.shape[1]
    C = np.zeros(n)

    for i in range(0, m):
        sum = 0
        for j in range(0, n):
            sum += A[i][j]*B[j]
        C[i] = sum

    return C

# QUESTION 5

A = np.array([[0, 0, 0, 0, 1, 0],
              [0, -1000, 0, 0, 1, -1],
              [0, 0, -5000, 0, 0, 1],
              [0, 0, 0, -10000, 0, 1],
              [1, -1, 0, 0, 0, 0],
              [0, 1, -1, -1, 0, 0]])

B = np.array([2.5, 0, 0, 0, 0, 0])

# On récupère la taille de la matrice A
m = A.shape[0]

# On adjoint à A une matrice identité de même taille
G = np.concatenate((A, np.eye(m)), axis=1)

# QUESTION 6

# On parcourt les m premières colonnes de la matrice
# en itérant sur la transposée
for pivot_column, column in enumerate(G.T[:m]):

    # On liste les éléments non nuls de la colonne
    # dans les lignes de numéro supérieur ou égal
    # au numéro de colonne
    nonzero = column[pivot_column:].nonzero()[0]

# QUESTION 7

    if nonzero.size != 0:
        # S'il reste des éléments non nuls,
        # alors on prend le premier comme pivot
        pivot_line = nonzero[0]+pivot_column
        pivot = G[pivot_line, pivot_column]

    else:
        # S'il ne reste que des éléments nuls,
        # alors c'est que la matrice n'est pas inversible
        print("Matrice non inversible")
        break

    # On échange la ligne du pivot avec la ligne
    # de même numéro que la colonne en cours de traitement
    G[[pivot_column, pivot_line]] = G[[pivot_line, pivot_column]]
    pivot_line = pivot_column

    # On divise la ligne du pivot par la valeur du pivot
    G[pivot_line] = G[pivot_line] / pivot

    # On parcourt la colonne sous le pivot pour faire apparaître des 0
    for index in range(pivot_column+1, m):

        # On soustrait un multiple de la ligne du pivot
        # pour faire apparaître un 0
        G[index] = G[index] - G[index][pivot_column] * G[pivot_line]

# QUESTION 8

# On parcourt les colonnes à l'envers
for column in range(m-1, -1, -1):

    # On parcourt la colonne au-dessus du pivot
    for line in range(column):

        # On soustrait un multiple de la ligne du pivot
        # pour faire apparaître un 0
        G[line] = G[line] - G[line][column] * G[column]

# QUESTION 9

# On récupère les m dernières colonnes de notre matrice,
# c'est là que se trouve l'inverse de A
inverted = G[:, m:]

X = produit_matriciel(inverted, B)

# COMPARAISON AVEC FONCTIONS NUMPY

inverted_numpy = np.linalg.inv(A)
X_numpy = np.matmul(inverted_numpy, B)
