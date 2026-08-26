# Objectif

Certains composants électroniques sont dits **linéaires**, c’est-à-dire
qu’on peut exprimer la relation entre le courant qui les traverse et la
tension à leurs bornes par une fonction affine. C’est le cas notamment
des **résistances** et des **sources idéales** de courant et de tension.

Si un circuit ne contient que des composants linéaires, alors il est
possible de le représenter par des équations **sous forme matricielle**
$`\mathbf{AX = B}`$**.** Le vecteur $`X`$, inconnu, contiendra les
courants et potentiels du circuit. Les matrices A et B contiennent des
constantes que l’on peut déduire du circuit et des valeurs des
composants.

Une fois ces matrices construites, on peut trouver la solution exacte de
$`X`$ en **inversant A (pivot de Gauss)** pour calculer
$`X = A^{- 1}B`$. On peut aussi calculer $`X`$ avec la **méthode de
Cramer**.\
On obtient ainsi les valeurs des courants et potentiels du circuit.

# Travail préliminaire

Soient :

- une matrice $`A = \begin{pmatrix}
  a_{1,1} & \cdots & a_{1,n} \\
   \vdots & \ddots & \vdots \\
  a_{m,1} & \ldots & a_{m,n}
  \end{pmatrix}`$ de dimension $`(m,n)\`$;

- un vecteur $`B = \begin{pmatrix}
  b_{1} \\
   \vdots \\
  b_{n}
  \end{pmatrix}`$ de dimension $`(n,1)`$.

Le produit matriciel $`C = AB`$ sera le vecteur de dimension $`(m,1)`$
dont les coefficients sont donnés par :

``` math
c_{i} = \sum_{k = 1}^{n}{a_{i,k}b_{k}}
```

C’est-à-dire $`C = \begin{pmatrix}
{a_{1,1}b}_{1} + \cdots + {a_{1,n}b}_{n} \\
 \vdots \\
{a_{m,1}b}_{1} + \cdots + {a_{m,n}b}_{n}
\end{pmatrix}`$.

## Question  :

Définir une fonction Python qui prend en paramètre une matrice $`A`$ et
un vecteur $`B`$ (de dimensions qu’on peut supposer concordantes) et qui
renvoie le produit matriciel des deux.

Les objets doivent être des arrays NumPy. Vous pouvez passer par deux
boucles for imbriquées.

# Mise en équation du problème

Le vecteur $`X`$ contient les inconnues de notre système d’équation. Ce
sont les courants à travers chacun des $`c\`$composants, notés $`i_{1}`$
à $`i_{c}`$, ainsi que les potentiels des $`n`$ nets de notre système,
notés $`v_{1}`$ à $`v_{n}`$. $`X`$ est donc de taille $`m = n + c`$.

$`X = \begin{pmatrix}
i_{1} \\
i_{2} \\
 \vdots \\
i_{c - 1} \\
i_{c} \\
v_{1} \\
v_{2} \\
 \vdots \\
v_{n - 1} \\
v_{n}
\end{pmatrix}`$ $`A = \begin{pmatrix}
a_{1,1} & \cdots & a_{1,m} \\
 \vdots & \ddots & \vdots \\
a_{m,1} & \ldots & a_{m,m}
\end{pmatrix}`$ $`B = \begin{pmatrix}
b_{1} \\
b_{2} \\
 \vdots \\
b_{m - 1} \\
b_{m}
\end{pmatrix}`$

> L’équation matricielle $`AX = B`$ est équivalente à un système de
> $`m`$ équations linéaires :
>
> ``` math
> \left\{ \begin{array}{r}
> a_{1,1}i_{1} + a_{1,2}i_{2} + \ldots + a_{1,m - 1}u_{n - 1} + a_{1,m}u_{n} = b_{1} \\
>  \vdots \\
> a_{m,1}i_{1} + a_{m,2}i_{2} + \ldots + a_{m,m - 1}u_{n - 1} + a_{m,m}u_{n} = b_{m}
> \end{array} \right.\ 
> ```

Les $`c\`$premières lignes de la matrice peuvent être remplies en
utilisant des informations sur le composant en question :

- si c’est une **résistance**, la **loi d’Ohm** permet d’établir une
  relation entre la différence de potentiel à ses bornes et le courant i
  qui la traverse ;

- si c’est une **source de tension**, alors la différence de potentiel à
  ses bornes est égale à une **constante**, qui est la valeur de la
  source ;

- si c’est une **source de courant**, alors le courant qui la traverse
  est égale à une **constante**, qui est la valeur de la source.

> Les $`n\`$dernières lignes de la matrice peuvent être remplies en
> utilisant la **loi des nœuds**, la somme des courants entrants dans un
> nœud est toujours égale à la somme des courants sortants.

Soit le circuit linéaire suivant :

<img src="media/media/image1.png"
style="width:3.9717in;height:2.37004in" />

Il s’agit d’un circuit à 4 composants et 3 nœuds. On peut ignorer le
nœud GND, dont on connait déjà le potentiel, fixé par convention à 0 V.
On a alors $`c = 4`$, $`n = 2`$, et $`m = 6`$.

``` math
X = \begin{pmatrix}
i_{1} \\
i_{2} \\
i_{3} \\
i_{4} \\
v_{1} \\
v_{2}
\end{pmatrix}
```

## Question 2 :

En utilisant les formules du cours (lois de Kirchhoff, associations de
résistances, pont diviseur de tension et de courant, …), simplifier le
circuit pour calculer les courants dans chaque branche et les potentiels
$`v_{1}`$ et $`v_{2}`$.

Dans la suite des questions, on va chercher à calculer la valeur de
$`X`$ par une analyse nodale, pour comparer avec les résultats de cours
obtenus à la question 2.

## Question  :

D’après la loi d’Ohm, on sait que la différence de tension
$`v_{1} - v_{2}`$ aux bornes de la résistance $`R_{2}`$ vaut
$`{R_{2}i}_{2}`$. On peut donc écrire l’équation suivante :

``` math
v_{1} - v_{2} = {R_{2}i}_{2}\  \Longleftrightarrow {- 1000i_{2} + v}_{1} - v_{2} = 0
```

Cela peut se transcrire dans la matrice $`A`$ et le vecteur $`B`$ par la
ligne suivante :

$`A = \begin{pmatrix}
 \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
0 & - 1000 & 0 & 0 & 1 & - 1 \\
 \vdots & \vdots & \vdots & \vdots & \vdots & \vdots 
\end{pmatrix}`$ $`B = \begin{pmatrix}
 \vdots \\
0 \\
 \vdots 
\end{pmatrix}`$

Ainsi, en faisant $`AX = B`$, on retrouve bien l’équation
$`{- 1000i_{2} + v}_{1} - v_{2} = 0`$.

Compléter la matrice $`A`$ et le vecteur $`B`$ avec les lignes
correspondants aux composants E1, R3 et R4.

## Question  :

D’après la loi des nœuds, on sait que la somme des courants entrant dans
le nœud $`v_{1}`$ est égale à la somme des courants en sortie. On a
donc :

``` math
i_{1} = i_{2}\  \Longleftrightarrow {i_{1} - i}_{2} = 0
```

Cela peut se transcrire dans la matrice $`A`$ et le vecteur $`B`$ par la
ligne suivante :

$`A = \begin{pmatrix}
 \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
1 & - 1 & 0 & 0 & 0 & 0 \\
 \vdots & \vdots & \vdots & \vdots & \vdots & \vdots 
\end{pmatrix}`$ $`B = \begin{pmatrix}
 \vdots \\
0 \\
 \vdots 
\end{pmatrix}`$

Ainsi, en faisant $`AX = B`$, on retrouve bien l’équation
$`{i_{1} - i}_{2} = 0`$

Compléter la matrice $`A`$ et le vecteur $`B`$ avec la ligne
correspondant au potentiel $`v_{2}`$.

À ce stade, vous devriez avoir une matrice $`A`$ complète de taille
6 x 6 est un vecteur $`B`$ complet de taille 6 x 1.

# Travail à effectuer

## Question  :

Rentrer la matrice $`A`$ et le vecteur $`B`$ calculés précédemment dans
Python sous forme d’array NumPy.

Créer une nouvelle matrice NumPy $`G`$ composée de la matrice $`A`$
concaténée avec une matrice identité de même taille. C’est la matrice
qui servira de support au pivot de Gauss.

``` math
G = \begin{pmatrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,m} & 1 & 0 & \cdots & 0 \\
a_{2,1} & a_{2,2} & \cdots & a_{2,m} & 0 & 1 & \cdots & 0 \\
 \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\
a_{m,1} & a_{m,1} & \cdots & a_{m,m} & 0 & 0 & \cdots & 1
\end{pmatrix}
```

## Question  :

En Python, parcourir les $`m`$ premières colonnes de $`G`$ (qui
correspondent à la matrice $`A`$). Vous pouvez parcourir les colonnes en
itérant sur la transposée, notée G.T dans NumPy.

Dans chaque colonne, lister les valeurs qui peuvent servir de pivot,
c’est-à-dire qui respectent les deux critères suivants :

- valeur non nulle ;

- numéro de ligne supérieur ou égal au numéro de la colonne.

<u>Exemple :</u> Dans la matrice G donné en exemple ci-dessous, les
pivots possibles sont encadrés.

``` math
G = \begin{pmatrix}
\boxed{3} & 2 & 1 & 2 & 1 & 0 & \cdots & 0 \\
0 & \boxed{- 1} & 2 & - 4 & 0 & 1 & \cdots & 0 \\
\boxed{2} & 0 & 0 & 3 & \vdots & \vdots & \ddots & \vdots \\
\boxed{- 5} & \boxed{3} & \boxed{2} & \boxed{6} & 0 & 0 & \cdots & 1
\end{pmatrix}
```

## Question 7 :

Pour chaque colonne :

- choisir le pivot comme étant la première des valeurs respectant les
  critères de la question 6 ;

- échanger la ligne du pivot avec la ligne de même numéro que la
  colonne ;

- diviser la ligne du pivot par la valeur du pivot pour faire apparaître
  un 1 à l’emplacement du pivot ;

- faire apparaître des 0 dans les lignes situées sous le pivot en
  ajoutant à ces lignes des multiples de la ligne du pivot.

Toutes les opérations doivent bien se faire sur la matrice G entière,
impactant ainsi également la matrice identité à droite.

De plus, lorsque l’on cherche un pivot pour une nouvelle colonne, il
faut bien le faire en tenant compte des modifications apportées par le
travail sur la colonne précédente.

À ce stade, vous devez obtenir sur la partie gauche de G une matrice
triangulaire supérieure, avec uniquement des 1 sur la diagonale.

## Question 8 :

Parcourir les colonnes dans l’ordre inverse et, pour chaque colonne,
faire apparaître des 0 dans les lignes situées au-dessus de la diagonale
en ajoutant à ces lignes des multiples de la ligne du pivot.

La partie gauche de la matrice G doit désormais être la matrice
identité, et la partie droite doit contenir l’inverse de A.

## Question  :

Calculer la solution de $`X`$ en calculant le produit matriciel
$`X = A^{- 1}B`$ avec votre fonction définie à la question 1.

Comparer les valeurs obtenues à celles calculées analytiquement à la
question 2.
