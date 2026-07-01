---
title: Cinématique du point matériel
authors:
  - coralie-thieulin
keywords:
  - cinématique
  - trajectoire
  - vitesse
  - accélération
  - coordonnées cartésiennes
  - coordonnées cylindriques
  - mouvement circulaire
abstract: |
  Dans ce chapitre, nous étudions le mouvement d'un point matériel dans un 
  référentiel galiléen, sans nous préoccuper de ses causes. C'est la cinématique,
  une approche purement géométrique et mathématique qui décrit le mouvement sans 
  encore l'expliquer.

  Après avoir posé les systèmes de coordonnées cartésiennes et cylindriques,
  nous définissons rigoureusement les vecteurs position, vitesse instantanée
  et accélération, puis nous les exprimons dans chacun de ces systèmes. Le
  chapitre se conclut par l'étude des mouvements usuels : rectiligne uniforme,
  uniformément accéléré, sinusoïdal, circulaire uniforme, ainsi que le cas d'un
  mouvement composé (rectiligne + circulaire).
---

## Introduction

Si on veut parler de vitesse ou d'accélération, il est essentiel de définir un
**référentiel**, c'est-à-dire de préciser _par rapport à quoi_ on mesure cette
vitesse et cette accélération. Ce chapitre est purement mathématique.

::::{note} Rappel — Les trois lois de Newton

Si l'on regarde les [trois lois de Newton](#lois-newton) établies au chapitre
précedent :

**Première loi** (principe d'inertie) :

:::{math}
:enumerated: false
\overrightarrow{F} = \overrightarrow{0} \quad \Leftrightarrow \quad
\overrightarrow{v}(M)_{/R} = \overrightarrow{cste}
:::

où $\overrightarrow{F}$ représente la résultante des forces extérieures
s'appliquant sur le système.

**Deuxième loi** (principe fondamental de la dynamique) :

:::{math}
:enumerated: false
\overrightarrow{F} = m \left( \frac{d\overrightarrow{v}(M)}{dt} \right)_{\!/R}
:::

**Troisième loi** (action–réaction) :

:::{math}
:enumerated: false
\overrightarrow{F}_{1/2} = -\,\overrightarrow{F}_{2/1}
\qquad \text{et} \qquad
\left\| \overrightarrow{F}_{1/2} \right\| = \left\| \overrightarrow{F}_{2/1} \right\|
:::
::::

On voit que la vitesse et sa variation interviennent dans les deux premières
lois. Nous allons donc regarder dans ce chapitre exclusivement les termes
concernant la vitesse.

On rappelle ici que nous étudions la mécanique du **{term}`point matériel`** :
un point matériel est un système dont la position d'ensemble peut être définie à
l'aide de trois coordonnées seulement. Rappelons que ce concept est un modèle
qui représente convenablement le comportement d'un solide animé d'un mouvement
de translation.

## Relativité du mouvement

L'étude du mouvement d'un point matériel implique nécessairement la présence
simultanée du point et d'un **observateur** qui analyse le mouvement de ce
point. L'observateur est le pilier de l'étude de ce mouvement car, en fonction
de sa position par rapport à l'objet en mouvement, ses conclusions quant à la
nature du mouvement changeront.

:::{prf:example} La bille dans le train
:label: ex-bille-train
Dans un train qui se déplace à vitesse constante, un passager qui lâche
verticalement une bille conclut que la bille a un mouvement **rectiligne**. La
personne qui est sur le quai et qui observe la même action conclut que le
mouvement n'est **pas rectiligne**. Pourtant, il s'agit bien de la même bille !
:::

Un mouvement est donc toujours lié à un observateur : il est dit **relatif**.

Avant de commencer tout problème de mécanique, il sera donc essentiel de définir
un **{term}`référentiel`** dans lequel l'observateur est fixe. Par exemple, dans le cas
du train cité plus haut, on pourra choisir le train comme référentiel ou bien le
référentiel terrestre.

Ensuite, pour caractériser le mouvement de l'objet, l'observateur a besoin de se
repérer dans l'espace : il doit pouvoir déterminer la position de l'objet au
cours du temps. En d'autres termes, il doit pouvoir répondre aux questions
« Où ? » et « Quand ? ».

Où ?
: L'observateur doit choisir un **{term}`repère` d'espace** défini par une **origine**
  (fixe dans le référentiel) et des **axes de référence** (liés au référentiel).
  Pour un référentiel donné, il existe une infinité de repères possibles (la
  réciproque est fausse).

Quand ?
: Il faut ajouter un **repère temporel**. En mécanique classique (ou
  newtonienne), on postule que le repère de temps est le même pour tous les
  référentiels et que le temps s'écoule de la même manière dans les référentiels
  en mouvement les uns par rapport aux autres (ce n'est plus le cas en mécanique
  relativiste).

Enfin, dans tout problème de mécanique, on sera amené à définir des grandeurs
vectorielles telles que les vecteurs position, vitesse et accélération. Il
faudra donc faire un choix de **{term}`systèmes de coordonnées <système de coordonnées>`** adaptées à la
géométrie du problème, et utiliser la **base** correspondante qui pourra être
**fixe ou mobile** dans le référentiel choisi (ceci aura des conséquences sur la
dérivation des vecteurs de la base).

## Systèmes de coordonnées

En physique, selon la physionomie du problème étudié, on choisit entre trois
systèmes de coordonnées qui sont des **bases orthonormées directes (BOND)**.

### Coordonnées cartésiennes

Les coordonnées cartésiennes sont les plus faciles à manipuler. Un point $M$ de
l'espace est repéré par trois coordonnées $\left( x_M , y_M , z_M \right)$ où
$x_M,\ y_M,\ z_M \in \mathbb{R}^3$.

Le repère est muni de trois vecteurs unitaires
$\left( \overrightarrow{e_x}, \overrightarrow{e_y}, \overrightarrow{e_z} \right)$
qui lui confèrent son orientation. On définit le **vecteur position**
$\overrightarrow{OM}$ tel que :

$$
\overrightarrow{OM} = x_M\,\overrightarrow{e_x} + y_M\,\overrightarrow{e_y} + z_M\,\overrightarrow{e_z}
$$

:::{figure} /media/ch1-coord-cartesiennes.png
:label: fig-coord-cartesiennes
:align: center
:width: 50%

Coordonnées cartésiennes du point $M(x_M, y_M, z_M)$ et base associée
$\left( \overrightarrow{e_x}, \overrightarrow{e_y}, \overrightarrow{e_z} \right)$.
:::

:::{note}
Cette base est **fixe** dans le référentiel d'étude.
:::

### Coordonnées cylindriques

Dans ce système de coordonnées, un point $M$ de l'espace est repéré par :

- un **rayon** $r_M > 0$ ;
- un **angle** $\theta \in \left[ 0 ; 2\pi \right[$ (angle entre l'axe $Ox$ et
  la projection du rayon $OM$ sur le plan $xOy$) ;
- une **hauteur** $z \in \mathbb{R}$ par rapport au plan $xOy$.

On définit aussi trois vecteurs unitaires
$\left( \overrightarrow{e_r}, \overrightarrow{e_\theta}, \overrightarrow{e_z} \right)$
que l'on place généralement au point $M$ ou en son projeté sur le plan $xOy$. Le
vecteur position s'écrit :

$$
\overrightarrow{OM} = r_M\,\overrightarrow{e_r} + z_M\,\overrightarrow{e_z}
$$

:::{figure} /media/ch1-coord-cylindriques.png
:label: fig-coord-cylindriques
:align: center
:width: 50%

Coordonnées cylindriques du point $M$ : rayon $r_M$, angle $\theta_M$ et
base mobile $\left( \overrightarrow{e_r}, \overrightarrow{e_\theta}, \overrightarrow{e_z} \right)$.
:::

:::{attention}
Cette base est « attachée » au point $M$ et **bouge en même temps que ce
dernier** : on dit que la base cylindrique est une **base mobile**. Ses vecteurs
ne sont donc pas constants dans le temps, ce qui sera crucial lors des
dérivations.
:::

## Trajectoire d'un point matériel

:::{prf:definition} Trajectoire
:label: def-trajectoire
La courbe représentant l'ensemble des positions $M(t)$ d'un point matériel
définit sa **trajectoire** pendant l'intervalle de temps considéré.
:::

Dans un référentiel d'étude galiléen
$R(O, \overrightarrow{u}, \overrightarrow{v}, \overrightarrow{w})$, les positions
$M(t)$ sont les vecteurs position successifs du point $M$, soit
$\overrightarrow{OM}(t)$, exprimés dans le système de coordonnées choisi pour
caractériser le mouvement.

### Équations horaires

De la trajectoire, les **équations horaires** du mouvement du point $M$ peuvent
être déduites. L'inverse est aussi vrai : des équations horaires, on peut déduire
la trajectoire du mouvement du point $M$.

En coordonnées cartésiennes, le vecteur position d'un point $M(x, y, z)$ est
donné par :

$$
\overrightarrow{OM} = x\,\overrightarrow{u_x} + y\,\overrightarrow{u_y} + z\,\overrightarrow{u_z}
$$

Lorsque le point $M$ est en mouvement, on a donc :

$$
\overrightarrow{OM}(t) = x(t)\,\overrightarrow{u_x} + y(t)\,\overrightarrow{u_y} + z(t)\,\overrightarrow{u_z}
$$

et l'ensemble de ces vecteurs aux différents temps permet de tracer la
trajectoire. Les trois coordonnées sont des fonctions du temps : ce sont les
**équations horaires** du mouvement du point $M$ :

$$
\begin{cases}
x(t) = \ldots \\
y(t) = \ldots \\
z(t) = \ldots
\end{cases}
$$

En combinant ces fonctions, on peut trouver l'équation décrivant la trajectoire.

### Équations horaires de mouvements particuliers

#### Mouvement circulaire dans le plan

Lorsque le point $M$ décrit un cercle (mouvement plan en 2D), il est plus facile
de décrire le vecteur position en coordonnées polaires, soit
$\overrightarrow{OM}(t) = r(t)\,\overrightarrow{u_r}$.

Or, en projetant $\overrightarrow{u_r}$ sur $\overrightarrow{u_x}$ et sur
$\overrightarrow{u_y}$, on obtient facilement :

$$
\overrightarrow{u_r} = \cos\theta(t)\,\overrightarrow{u_x} + \sin\theta(t)\,\overrightarrow{u_y}
$$

On a alors :

$$
\overrightarrow{OM}(t) = r(t)\cos\theta(t)\,\overrightarrow{u_x} + r(t)\sin\theta(t)\,\overrightarrow{u_y}
$$

On en déduit les équations du point $M$ :

$$
\begin{cases}
x(t) = r(t)\cos\theta(t) \\
y(t) = r(t)\sin\theta(t)
\end{cases}
$$

Si $r(t) = r = \text{cte}$ (cas du **mouvement circulaire**), on obtient :

$$
\begin{cases}
x(t) = r\cos\theta(t) \\
y(t) = r\sin\theta(t)
\end{cases}
$$

#### Mouvement cylindrique

De même, on peut montrer que pour un mouvement cylindrique (3D), les équations
du point $M$ sont :

$$
\begin{cases}
x(t) = r(t)\cos\theta(t) \\
y(t) = r(t)\sin\theta(t) \\
z(t) = h(t)
\end{cases}
$$

:::{prf:example} Déterminer une trajectoire à partir d'équations horaires
:label: ex-trajectoire-cercle
Soit un point matériel $M$ en mouvement dans le référentiel
$R(O ; \overrightarrow{u_x}, \overrightarrow{u_y})$ selon les équations horaires
suivantes :

$$
M(t) = \begin{cases}
x(t) = 4\cos\theta(t) \\
y(t) = 4\sin\theta(t)
\end{cases}
$$

**Déterminez la trajectoire du point $M$ ainsi que son mouvement.**

On remarque que :

$$
x^2(t) + y^2(t) = \big(4\cos\theta(t)\big)^2 + \big(4\sin\theta(t)\big)^2
= 4^2\left( \cos^2\theta(t) + \sin^2\theta(t) \right) = 4^2
$$

On a alors $x^2(t) + y^2(t) = 4^2$ : c'est l'équation d'un **cercle** de centre
$O$ de coordonnées $(0,0)$ et de rayon $4$.

D'après ses équations horaires, le point $M$ décrit donc un cercle de centre $O$
et son mouvement est **circulaire** (translation circulaire).
:::

## Notion de vitesse d'un point matériel

Il existe plusieurs vitesses.

:::{prf:example} Vitesse moyenne ou vitesse instantanée ?
:label: ex-vitesse-moy-instantanee
Vous prenez votre voiture et parcourez $6\ \text{km}$ en $10\ \text{min}$. Vous
aurez alors parcouru ces $6\ \text{km}$ à la **vitesse moyenne** de :

$$
v_{\text{moy}} = \frac{6}{10} = 0{,}6\ \text{km/min} = 36\ \text{km/h}
$$

Par contre, si au bout des $10\ \text{min}$ un policier vous arrête en vous
disant que vous rouliez à $90\ \text{km/h}$, vous ne pouvez pas lui répondre que
_c'est impossible car vous n'avez fait que 6 km en 10 minutes_.

Il y a donc **deux vitesses différentes** : la vitesse énoncée par le policier
n'est pas une vitesse moyenne, mais une vitesse sur l'instant — une **vitesse
instantanée**.
:::

### Vitesse moyenne

Soit $M$ la position d'un point matériel à l'instant $t$, et $M'$ la position de
ce même point matériel à l'instant $t + dt$.

:::{figure} /media/ch1-vitesse-moyenne.png
:label: fig-vitesse-moyenne
:align: center
:width: 45%

Trajectoire du point $M$ entre les instants $t$ et $t + dt$ : le vecteur
$\overrightarrow{v_{\text{moy}}}$ est porté par la corde $MM'$.
:::

:::{prf:definition} Vecteur déplacement et vitesse moyenne
:label: def-vitesse-moyenne
Le vecteur $\overrightarrow{MM'}$ est appelé **vecteur déplacement**, à ne pas
confondre avec le vecteur position.

On définit la **vitesse moyenne vectorielle** de $M$ pendant l'intervalle de
temps $(t, t + dt)$ telle que :

$$
\overrightarrow{v_{\text{moy}}} = \frac{\overrightarrow{MM'}}{dt}
$$
:::

Cette vitesse est indépendante du chemin parcouru : elle dépend exclusivement de
la distance entre le point de départ et le point d'arrivée (en ligne droite) et
du temps mis pour aller d'un point à l'autre.

### Vitesse instantanée

Si on fait tendre le temps de parcours vers $0$, soit $dt \rightarrow 0$, alors
on a $\overrightarrow{v}(t) = \lim\limits_{dt \rightarrow 0} \overrightarrow{v_{\text{moy}}}$.

Or :

$$
\overrightarrow{MM'} = \overrightarrow{MO} + \overrightarrow{OM'}
= \overrightarrow{OM'} - \overrightarrow{OM}
= \overrightarrow{OM}(t + dt) - \overrightarrow{OM}(t)
$$

Donc :

$$
\lim_{dt \rightarrow 0} \overrightarrow{v_{\text{moy}}}
= \lim_{dt \rightarrow 0} \frac{\overrightarrow{MM'}}{dt}
= \lim_{dt \rightarrow 0} \frac{\overrightarrow{OM}(t + dt) - \overrightarrow{OM}(t)}{dt}
= \frac{d\overrightarrow{OM}}{dt}
$$

Les mouvements étant relatifs, on doit définir cette vitesse instantanée par
rapport à un référentiel.

:::{prf:definition} Vitesse instantanée
:label: def-vitesse-instantanee
Soit $O$ un point fixe du référentiel $R$ d'étude. La **vitesse instantanée** du
point $M$ par rapport au référentiel $R$ s'écrit :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) = \left( \frac{d\overrightarrow{OM}}{dt} \right)_{\!/R}
$$

L'unité de la vitesse est le mètre par seconde ($\mathrm{m\cdot s^{-1}}$).
:::

Le terme $\dfrac{d\overrightarrow{OM}}{dt}$ représente la dérivée du vecteur
position $\overrightarrow{OM}$ en fonction du temps $t$.

:::{note} Les différentes notations de la dérivée
Il existe différentes notations pour exprimer la dérivée d'une fonction $f$ en
un point :

- **Notation de Lagrange** : $f'(a)$ — surtout utilisée en mathématiques ;
- **Notation de Leibniz** : $\dfrac{df}{dx}(a)$ ou $\left.\dfrac{df}{dx}\right|_{x = a}$
  — la plus utilisée en physique ;
- **Notation de Newton** : $\dot{f}(a)$ — très utilisée en mécanique pour
  désigner une dérivée **par rapport au temps**.
:::

### Calcul de la vitesse dans un référentiel galiléen

Pour l'ensemble des calculs de cette partie, le référentiel d'étude est
$R(O, \overrightarrow{u_x}, \overrightarrow{u_y}, \overrightarrow{u_z})$, où
$(\overrightarrow{u_x}, \overrightarrow{u_y}, \overrightarrow{u_z})$ est la base
cartésienne.

#### Expression de la vitesse en coordonnées cartésiennes

Le vecteur position d'un point $M$ quelconque s'écrit en coordonnées
cartésiennes :

$$
\overrightarrow{OM} = x\,\overrightarrow{u_x} + y\,\overrightarrow{u_y} + z\,\overrightarrow{u_z}
$$

Comme
$\overrightarrow{v}\!\left( \frac{M}{R} \right) = \left( \dfrac{d\overrightarrow{OM}}{dt} \right)_{\!/R}$,
il vient :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) =
\frac{dx}{dt}\overrightarrow{u_x} + x\left( \frac{d\overrightarrow{u_x}}{dt} \right)_{\!/R}
+ \frac{dy}{dt}\overrightarrow{u_y} + y\left( \frac{d\overrightarrow{u_y}}{dt} \right)_{\!/R}
+ \frac{dz}{dt}\overrightarrow{u_z} + z\left( \frac{d\overrightarrow{u_z}}{dt} \right)_{\!/R}
$$

Or, ces vecteurs de base ne varient pas au cours du temps (ce sont les vecteurs
de la base liée au référentiel) :

$$
\left( \frac{d\overrightarrow{u_x}}{dt} \right)_{\!/R} =
\left( \frac{d\overrightarrow{u_y}}{dt} \right)_{\!/R} =
\left( \frac{d\overrightarrow{u_z}}{dt} \right)_{\!/R} = \overrightarrow{0}
$$

D'où :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) =
\frac{dx}{dt}\overrightarrow{u_x} + \frac{dy}{dt}\overrightarrow{u_y} + \frac{dz}{dt}\overrightarrow{u_z}
= \dot{x}\,\overrightarrow{u_x} + \dot{y}\,\overrightarrow{u_y} + \dot{z}\,\overrightarrow{u_z}
$$

#### Expression de la vitesse en coordonnées cylindriques

Le vecteur position d'un point $M$ quelconque s'écrit en coordonnées
cylindriques :

$$
\overrightarrow{OM} = r\,\overrightarrow{u_r} + z\,\overrightarrow{u_z}
$$

Alors :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) =
\dot{r}\,\overrightarrow{u_r} + r\left( \frac{d\overrightarrow{u_r}}{dt} \right)_{\!/R}
+ \dot{z}\,\overrightarrow{u_z} + z\left( \frac{d\overrightarrow{u_z}}{dt} \right)_{\!/R}
$$

Or $\left( \dfrac{d\overrightarrow{u_z}}{dt} \right)_{\!/R} = \overrightarrow{0}$
car le vecteur $\overrightarrow{u_z}$ est lié au référentiel d'étude. En revanche,
les vecteurs $\overrightarrow{u_r}$ et $\overrightarrow{u_\theta}$ varient au
cours du temps dans ce référentiel :

$$
\begin{cases}
\left( \dfrac{d\overrightarrow{u_r}}{dt} \right)_{\!/R} = \dfrac{d\theta}{dt}\,\overrightarrow{u_\theta} = \dot{\theta}\,\overrightarrow{u_\theta} \\[2ex]
\left( \dfrac{d\overrightarrow{u_\theta}}{dt} \right)_{\!/R} = -\dfrac{d\theta}{dt}\,\overrightarrow{u_r} = -\dot{\theta}\,\overrightarrow{u_r}
\end{cases}
$$

On obtient alors :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) =
\dot{r}\,\overrightarrow{u_r} + r\dot{\theta}\,\overrightarrow{u_\theta} + \dot{z}\,\overrightarrow{u_z}
$$

::::{dropdown} Démonstration : dérivées des vecteurs de la base polaire
**Méthode 1 — par le calcul** (à savoir refaire)

**a)** Calcul de $\left( \dfrac{d\overrightarrow{u_r}}{dt} \right)_{\!/R}$.

On a $\overrightarrow{u_r} = \cos\theta\,\overrightarrow{u_x} + \sin\theta\,\overrightarrow{u_y}$,
donc :

$$
\left( \frac{d\overrightarrow{u_r}}{dt} \right)_{\!/R} =
-\dot{\theta}\sin\theta\,\overrightarrow{u_x} + \dot{\theta}\cos\theta\,\overrightarrow{u_y}
= \dot{\theta}\left( -\sin\theta\,\overrightarrow{u_x} + \cos\theta\,\overrightarrow{u_y} \right)
$$

Or $\overrightarrow{u_\theta} = -\sin\theta\,\overrightarrow{u_x} + \cos\theta\,\overrightarrow{u_y}$,
on a donc :

$$
\left( \frac{d\overrightarrow{u_r}}{dt} \right)_{\!/R} = \frac{d\theta}{dt}\,\overrightarrow{u_\theta} = \dot{\theta}\,\overrightarrow{u_\theta}
$$

**b)** Calcul de $\left( \dfrac{d\overrightarrow{u_\theta}}{dt} \right)_{\!/R}$.

On a $\overrightarrow{u_\theta} = -\sin\theta\,\overrightarrow{u_x} + \cos\theta\,\overrightarrow{u_y}$,
donc :

$$
\left( \frac{d\overrightarrow{u_\theta}}{dt} \right)_{\!/R} =
-\dot{\theta}\cos\theta\,\overrightarrow{u_x} - \dot{\theta}\sin\theta\,\overrightarrow{u_y}
= -\dot{\theta}\left( \cos\theta\,\overrightarrow{u_x} + \sin\theta\,\overrightarrow{u_y} \right)
$$

Or $\overrightarrow{u_r} = \cos\theta\,\overrightarrow{u_x} + \sin\theta\,\overrightarrow{u_y}$,
on a donc :

$$
\left( \frac{d\overrightarrow{u_\theta}}{dt} \right)_{\!/R} = -\frac{d\theta}{dt}\,\overrightarrow{u_r} = -\dot{\theta}\,\overrightarrow{u_r}
$$

**Méthode 2 — géométrique**

:::{figure} /media/ch1-derivee-base-polaire.png
:label: fig-derivee-base-polaire
:align: center
:width: 55%

Lorsque $d\theta \to 0$, les variations $d\overrightarrow{u_r}$ et
$d\overrightarrow{u_\theta}$ sont portées respectivement par
$\overrightarrow{u_\theta}$ et $-\overrightarrow{u_r}$.
:::

Lorsque $d\theta$ tend vers $0$, on voit sur la figure que
$d\overrightarrow{u_r} = d\theta\,\overrightarrow{u_\theta}$ et
$d\overrightarrow{u_\theta} = -d\theta\,\overrightarrow{u_r}$.

En effet :
$\overrightarrow{u_r}(t + dt) - \overrightarrow{u_r}(t) = d\overrightarrow{u_r}$ ;
$\overrightarrow{u_\theta}(t + dt) - \overrightarrow{u_\theta}(t) = d\overrightarrow{u_\theta}$
et $\sin d\theta = \dfrac{du_r}{1} = \dfrac{du_\theta}{1} \sim d\theta$.

Donc :

$$
\frac{d\overrightarrow{u_r}}{dt} = \frac{d\theta}{dt}\,\overrightarrow{u_\theta} = \dot{\theta}\,\overrightarrow{u_\theta}
\qquad \text{et} \qquad
\frac{d\overrightarrow{u_\theta}}{dt} = -\frac{d\theta}{dt}\,\overrightarrow{u_r} = -\dot{\theta}\,\overrightarrow{u_r}
$$
::::

## Accélération d'un point matériel

### Définition

:::{prf:definition} Accélération
:label: def-acceleration
L'**accélération** traduit les variations de vitesse au cours du temps. Son unité
est le $\mathrm{m\cdot s^{-2}}$ et son expression est :

$$
\overrightarrow{a}\!\left( \frac{M}{R} \right) =
\left( \frac{d\overrightarrow{v}(M/R)}{dt} \right)_{\!/R} =
\left( \frac{d^2\overrightarrow{OM}}{dt^2} \right)_{\!/R}
$$
:::

### Mouvement accéléré ou retardé ?

#### Cas d'une vitesse constante

Si la norme de la vitesse est constante, alors :

$$
\left\| \overrightarrow{v}\!\left( \frac{M}{R} \right) \right\| = \text{cst}
\ \Rightarrow\ \left\| \overrightarrow{v}\!\left( \frac{M}{R} \right) \right\|^2 = \text{cst}
\ \Rightarrow\ \overrightarrow{v}^{\,2}\!\left( \frac{M}{R} \right) = \text{cst}
$$

Donc :

$$
\frac{d\left\| \overrightarrow{v}\!\left( \frac{M}{R} \right) \right\|^2}{dt}
= \frac{d\,\overrightarrow{v}^{\,2}\!\left( \frac{M}{R} \right)}{dt} = 0
$$

Or :

$$
\frac{d\,\overrightarrow{v}^{\,2}\!\left( \frac{M}{R} \right)}{dt}
= 2\,\overrightarrow{v}\!\left( \frac{M}{R} \right) \cdot \frac{d\overrightarrow{v}\!\left( \frac{M}{R} \right)}{dt}
= 2\,\overrightarrow{v}\!\left( \frac{M}{R} \right) \cdot \overrightarrow{a}\!\left( \frac{M}{R} \right)
$$

Donc
$\overrightarrow{v}\!\left( \frac{M}{R} \right) \cdot \overrightarrow{a}\!\left( \frac{M}{R} \right) = 0$.
Commentons ce résultat :

- Soit $\left\| \overrightarrow{a}\!\left( \frac{M}{R} \right) \right\| = 0$ (pas
  d'accélération) $\Rightarrow$ **mouvement rectiligne uniforme** ;
- Soit $\overrightarrow{a} \perp \overrightarrow{v}$ $\Rightarrow$ **mouvement
  circulaire uniforme**, où
  $\overrightarrow{v} = R\,\omega\,\overrightarrow{u_\theta}$ et
  $\omega = \dfrac{d\theta}{dt}$ (vitesse angulaire, en $\mathrm{rad\cdot s^{-1}}$).

#### Cas d'une vitesse variable

- Si $v \nearrow$, alors $v^2 = \overrightarrow{v}^{\,2} \nearrow$, donc
  $\dfrac{d\,\overrightarrow{v}^{\,2}}{dt} = 2\,\overrightarrow{v} \cdot \overrightarrow{a} > 0$
  : le **mouvement est accéléré** ($\overrightarrow{v}$ et $\overrightarrow{a}$
  sont dans le même sens).
- Si $v \searrow$, alors $v^2 = \overrightarrow{v}^{\,2} \searrow$, donc
  $\dfrac{d\,\overrightarrow{v}^{\,2}}{dt} = 2\,\overrightarrow{v} \cdot \overrightarrow{a} < 0$
  : le **mouvement est retardé** ($\overrightarrow{v}$ et $\overrightarrow{a}$
  sont en sens opposés).

:::{figure} /media/ch1-acceleration-signe.gif
:label: fig-acceleration-signe
:align: center
:width: 60%

Signe du produit scalaire $\overrightarrow{v} \cdot \overrightarrow{a}$ selon que
le mobile monte ou descend la pente : **descente** ($\overrightarrow{v} \cdot \overrightarrow{a} > 0$),
**montée** ($\overrightarrow{v} \cdot \overrightarrow{a} < 0$).
:::

:::{important} À retenir
Ce n'est **pas le signe de l'accélération** qui indique le caractère retardé ou
accéléré d'un mouvement, **mais le signe du produit scalaire
$\overrightarrow{v} \cdot \overrightarrow{a}$** !
:::

### Expression de l'accélération en coordonnées cartésiennes

Dans $R(O, \overrightarrow{u_x}, \overrightarrow{u_y}, \overrightarrow{u_z})$
avec la base cartésienne, d'après l'expression de la vitesse, on a
immédiatement :

$$
\overrightarrow{a}\!\left( \frac{M}{R} \right) =
\ddot{x}\,\overrightarrow{u_x} + \ddot{y}\,\overrightarrow{u_y} + \ddot{z}\,\overrightarrow{u_z}
$$

### Expression de l'accélération en coordonnées cylindriques

Comme
$\overrightarrow{v}\!\left( \frac{M}{R} \right) = \dot{r}\,\overrightarrow{u_r} + r\dot{\theta}\,\overrightarrow{u_\theta} + \dot{z}\,\overrightarrow{u_z}$
et
$\overrightarrow{a}\!\left( \frac{M}{R} \right) = \left( \dfrac{d\overrightarrow{v}(M/R)}{dt} \right)_{\!/R}$,
on a :

$$
\overrightarrow{a}\!\left( \frac{M}{R} \right) =
\ddot{r}\,\overrightarrow{u_r} + \dot{r}\left( \frac{d\overrightarrow{u_r}}{dt} \right)_{\!/R}
+ \dot{r}\dot{\theta}\,\overrightarrow{u_\theta} + r\ddot{\theta}\,\overrightarrow{u_\theta}
+ r\dot{\theta}\left( \frac{d\overrightarrow{u_\theta}}{dt} \right)_{\!/R}
+ \ddot{z}\,\overrightarrow{u_z} + \dot{z}\left( \frac{d\overrightarrow{u_z}}{dt} \right)_{\!/R}
$$

Comme
$\left( \dfrac{d\overrightarrow{u_r}}{dt} \right)_{\!/R} = \dot{\theta}\,\overrightarrow{u_\theta}$,
$\left( \dfrac{d\overrightarrow{u_\theta}}{dt} \right)_{\!/R} = -\dot{\theta}\,\overrightarrow{u_r}$
et
$\left( \dfrac{d\overrightarrow{u_z}}{dt} \right)_{\!/R} = \overrightarrow{0}$,
alors :

$$
\overrightarrow{a}\!\left( \frac{M}{R} \right) =
\left( \ddot{r} - r\dot{\theta}^2 \right)\overrightarrow{u_r}
+ \left( 2\dot{r}\dot{\theta} + r\ddot{\theta} \right)\overrightarrow{u_\theta}
+ \ddot{z}\,\overrightarrow{u_z}
$$

### Retrouver les équations horaires à partir de l'accélération

Lorsque vous connaîtrez l'accélération, le but sera de remonter aux équations
horaires afin de connaître la trajectoire (c'est-à-dire le mouvement). Il faut
alors savoir non pas dériver, mais **intégrer**. En effet, nous savons que :

$$
\overrightarrow{a}\!\left( \frac{M}{R} \right) =
\left( \frac{d\overrightarrow{v}(M/R)}{dt} \right)_{\!/R} =
\left( \frac{d^2\overrightarrow{OM}}{dt^2} \right)_{\!/R}
$$

Si
$\overrightarrow{a}\!\left( \frac{M}{R} \right) = a_x(t)\,\overrightarrow{u_x} + a_y(t)\,\overrightarrow{u_y} + a_z(t)\,\overrightarrow{u_z}$
(cas le plus général dans un espace à trois dimensions comme le nôtre), alors :

$$
\begin{pmatrix} a_x(t) \\ a_y(t) \\ a_z(t) \end{pmatrix}
= \begin{pmatrix} \dfrac{dv_x(t)}{dt} \\[1.5ex] \dfrac{dv_y(t)}{dt} \\[1.5ex] \dfrac{dv_z(t)}{dt} \end{pmatrix}
\quad \Leftrightarrow \quad
\begin{cases}
a_x(t) = \dfrac{dv_x(t)}{dt} \\[1.5ex]
a_y(t) = \dfrac{dv_y(t)}{dt} \\[1.5ex]
a_z(t) = \dfrac{dv_z(t)}{dt}
\end{cases}
$$

C'est ici que la notation de Leibniz prend tout son sens, car ces trois
équations peuvent s'écrire :

$$
\begin{cases}
dv_x(t) = a_x(t)\,dt \\
dv_y(t) = a_y(t)\,dt \\
dv_z(t) = a_z(t)\,dt
\end{cases}
$$

On peut alors intégrer chacune des équations afin de déterminer $v_x(t)$,
$v_y(t)$ et $v_z(t)$ :

$$
\begin{cases}
\displaystyle\int_{v_x(0)}^{v_x(t)} dv_x = \int_{0}^{t} a_x(t)\,dt \\[2ex]
\displaystyle\int_{v_y(0)}^{v_y(t)} dv_y = \int_{0}^{t} a_y(t)\,dt \\[2ex]
\displaystyle\int_{v_z(0)}^{v_z(t)} dv_z = \int_{0}^{t} a_z(t)\,dt
\end{cases}
$$

Soit :

$$
\begin{cases}
\big[ v_x(t) \big]_{v_x(0)}^{v_x(t)} = \big[ A_x(t) \big]_{0}^{t} \\[1ex]
\big[ v_y(t) \big]_{v_y(0)}^{v_y(t)} = \big[ A_y(t) \big]_{0}^{t} \\[1ex]
\big[ v_z(t) \big]_{v_z(0)}^{v_z(t)} = \big[ A_z(t) \big]_{0}^{t}
\end{cases}
$$

où les fonctions $A_x(t)$, $A_y(t)$, $A_z(t)$ sont les primitives respectives de
$a_x(t)$, $a_y(t)$, $a_z(t)$, dont l'expression est connue. Ceci donne au final :

$$
\begin{cases}
v_x(t) = A_x(t) + v_x(0) \\
v_y(t) = A_y(t) + v_y(0) \\
v_z(t) = A_z(t) + v_z(0)
\end{cases}
$$

avec $v_x(0)$, $v_y(0)$ et $v_z(0)$ les **vitesses initiales** (vitesses au
départ du mouvement) : ce sont donc des valeurs connues. Alors, comme :

$$
\begin{pmatrix} v_x(t) \\ v_y(t) \\ v_z(t) \end{pmatrix}
= \begin{pmatrix} \dfrac{dx(t)}{dt} \\[1.5ex] \dfrac{dy(t)}{dt} \\[1.5ex] \dfrac{dz(t)}{dt} \end{pmatrix}
\quad \Leftrightarrow \quad
\begin{cases}
dx(t) = v_x(t)\,dt \\
dy(t) = v_y(t)\,dt \\
dz(t) = v_z(t)\,dt
\end{cases}
$$

En intégrant de nouveau, on obtient :

$$
\begin{cases}
x(t) = A_x'(t) + v_x(0)\,t + x(0) \\
y(t) = A_y'(t) + v_y(0)\,t + y(0) \\
z(t) = A_z'(t) + v_z(0)\,t + z(0)
\end{cases}
$$

où les fonctions $A_x'(t)$, $A_y'(t)$ et $A_z'(t)$ sont les primitives
respectives de $A_x(t)$, $A_y(t)$ et $A_z(t)$.

## Étude des mouvements usuels

### Mouvement rectiligne

Un mouvement est **rectiligne** s'il correspond à un déplacement le long d'une
droite fixe dans le référentiel d'étude. Dans ce cas, les vecteurs vitesse et
accélération sont portés par la droite sur laquelle s'effectue le mouvement. On
utilise le système de **coordonnées cartésiennes** pour ce type de mouvement.

#### Mouvement rectiligne uniforme

C'est le mouvement de translation le plus simple : le mouvement du point matériel
est en ligne droite (rectiligne) et l'accélération est nulle (mouvement uniforme,
c'est-à-dire que le vecteur vitesse est constant au cours du temps).

Si l'axe du mouvement est l'axe $Ox$, on a dans le référentiel
$R(O, \overrightarrow{u_x}, \overrightarrow{u_y}, \overrightarrow{u_z})$ :

$$
\overrightarrow{OM} = x\,\overrightarrow{u_x}
$$

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) = \frac{dx}{dt}\overrightarrow{u_x} = v_0\,\overrightarrow{u_x} = \overrightarrow{cste}
$$

Ce qui, en intégrant de l'instant initial à l'instant $t$, donne l'équation
horaire (ici, équation du mouvement du point) :

$$
x(t) = v_0\,t + x(t = 0)
$$

#### Mouvement rectiligne uniformément accéléré

C'est le même mouvement que précédemment, mais cette fois-ci l'accélération n'est
pas nulle : elle est **constante**.

$$
\overrightarrow{a}(M/R) = a_0\,\overrightarrow{u_x} = \frac{dv}{dt}\overrightarrow{u_x}
$$

:::{note}
- Si $a_0 > 0$, alors le mouvement est **accéléré** (la vitesse augmente).
- Si $a_0 < 0$, alors le mouvement est **retardé** (la vitesse diminue).
:::

En intégrant de l'instant initial à l'instant $t$, on trouve l'expression de la
vitesse :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) = \big( a_0\,t + v(t = 0) \big)\overrightarrow{u_x}
\qquad \text{ou} \qquad
v(t) = a_0\,t + v(t = 0)
$$

:::{note}
Comme il n'y a qu'un seul axe, l'accélération et la vitesse n'ont qu'une seule
composante suivant ce même axe : la notation vectorielle peut être abandonnée.
:::

Ce qui, en intégrant de nouveau de l'instant initial à l'instant $t$, donne
l'équation horaire :

$$
x(t) = \frac{1}{2}a_0\,t^2 + v(t = 0)\,t + x(t = 0)
$$

$$
\overrightarrow{OM} = \left( \frac{1}{2}a_0\,t^2 + v(t = 0)\,t + x(t = 0) \right)\overrightarrow{u_x}
$$

#### Mouvement rectiligne sinusoïdal

Un mouvement rectiligne sinusoïdal est un mouvement oscillatoire de pulsation
$\omega\ (\mathrm{rad\cdot s^{-1}})$, de période $T = \dfrac{2\pi}{\omega}\ (\text{s})$,
de fréquence $f = \dfrac{\omega}{2\pi} = \dfrac{1}{T}\ (\text{Hz})$, d'amplitude
$x_m\ (\text{m})$ et de phase $\varphi\ (\text{rad})$, tel que :

$$
x(t) = x_m \cos(\omega t + \varphi)
$$

Le plus souvent, l'équation horaire est donnée et il faut déterminer la vitesse
et l'accélération du point matériel. La vitesse est donnée par :

$$
v(t) = \frac{dx(t)}{dt} = -x_m\,\omega\,\sin(\omega t + \varphi)
$$

En dérivant de nouveau, on trouve l'accélération :

$$
a(t) = \ddot{x}(t) = -x_m\,\omega^2\,\cos(\omega t + \varphi)
$$

:::{note}
Ce sera le cas d'un point matériel attaché à un ressort et astreint à se
déplacer sur une droite.
:::

### Mouvement circulaire

Le mouvement circulaire consiste en un point matériel $M$ décrivant un cercle de
centre $O$, de rayon $R = OM$, à vitesse angulaire
$\omega = \dfrac{d\theta}{dt} = \dot{\theta}$.

:::{attention}
$\omega$ n'est **pas obligatoirement constant** !
:::

Les coordonnées les plus adaptées sont les **coordonnées polaires**. Dans un
référentiel $R(O, \overrightarrow{u_x}, \overrightarrow{u_y}, \overrightarrow{u_z})$,
on a :

$$
\overrightarrow{OM} = R\,\overrightarrow{u_r}
$$

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) = R\dot{\theta}\,\overrightarrow{u_\theta} = R\,\omega(t)\,\overrightarrow{u_\theta}
$$

La vitesse n'a donc qu'une seule composante dans un mouvement circulaire et est
toujours dirigée suivant le vecteur unitaire $\overrightarrow{u_\theta}$, quel
que soit le temps $t$. On dit que le vecteur vitesse est **orthoradial**.

On peut également exprimer l'accélération :

$$
\overrightarrow{a}(M/R) = -R\dot{\theta}^2\,\overrightarrow{u_r} + R\ddot{\theta}\,\overrightarrow{u_\theta}
= -R\omega^2\,\overrightarrow{u_r} + R\dot{\omega}\,\overrightarrow{u_\theta}
$$

:::{figure} /media/ch1-mouvement-circulaire.png
:label: fig-mouvement-circulaire
:align: center
:width: 45%

Mouvement circulaire : la vitesse $\overrightarrow{v}$ est orthoradiale (portée
par $\overrightarrow{u_\theta}$).
:::

Si $\omega = \text{cst}$, le mouvement est **circulaire uniforme**. Dans ce cas :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) = R\,\omega\,\overrightarrow{u_\theta}
$$

La vitesse dans un mouvement circulaire uniforme est de norme constante
(uniforme) quel que soit le temps $t$. L'accélération est alors donnée par :

$$
\overrightarrow{a} = -R\,\omega^2\,\overrightarrow{u_r}
$$

:::{note} Accélération centripète
L'accélération dans un mouvement circulaire uniforme n'est **pas nulle**. On
l'appelle l'**accélération centripète** car elle est toujours portée par
$\overrightarrow{u_r}$ et dirigée vers le point $O$, centre du mouvement.
:::

### Mouvement composé : rectiligne + circulaire

Ce mouvement consiste en un point matériel $M$ décrivant un cercle (rayon $R$, à
la vitesse angulaire $\omega = \dfrac{d\theta}{dt} = \dot{\theta}$) autour du
point $A$, lui-même animé d'un mouvement rectiligne uniforme dans le référentiel
d'étude $R(O, \overrightarrow{u_x}, \overrightarrow{u_y}, \overrightarrow{u_z})$.
On note
$\overrightarrow{v}\!\left( \frac{A}{R} \right) = v_0\,\overrightarrow{u_x}$.

On a :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) =
\left( \frac{d\overrightarrow{OM}}{dt} \right)_{\!/R}
= \left( \frac{d\overrightarrow{OA}}{dt} \right)_{\!/R} + \left( \frac{d\overrightarrow{AM}}{dt} \right)_{\!/R}
= \overrightarrow{v}\!\left( \frac{A}{R} \right) + \left( \frac{d\overrightarrow{AM}}{dt} \right)_{\!/R}
$$

En effet, on a bien, par définition,
$\overrightarrow{v}\!\left( \frac{A}{R} \right) = \left( \dfrac{d\overrightarrow{OA}}{dt} \right)_{\!/R}$.
En revanche, $\left( \dfrac{d\overrightarrow{AM}}{dt} \right)_{\!/R}$ n'est pas
une vitesse car les points $A$ et $M$ sont tous deux mobiles dans le référentiel
d'étude.

Il faut donc changer de référentiel afin de rendre le point $A$ fixe. On définit
alors le référentiel
$R'(A, \overrightarrow{u_x}, \overrightarrow{u_y}, \overrightarrow{u_z})$ : le
repère associé à $R'$ est centré en $A$ (fixe dans $R'$) et possède la même base
que celle de $R$. Ce référentiel $R'$ est dit **en translation** dans $R$.

Pour deux référentiels en translation l'un par rapport à l'autre, on a :

$$
\left( \frac{d\overrightarrow{AM}}{dt} \right)_{\!/R} = \left( \frac{d\overrightarrow{AM}}{dt} \right)_{\!/R'}
$$

Or
$\overrightarrow{v}\!\left( \frac{M}{R'} \right) = \left( \dfrac{d\overrightarrow{AM}}{dt} \right)_{\!/R'} = r\dot{\theta}\,\overrightarrow{u_\theta}$
(même résolution en polaire que dans le cas précédent). On a finalement :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) = \overrightarrow{v}\!\left( \frac{A}{R} \right) + \overrightarrow{v}\!\left( \frac{M}{R'} \right)
$$

Soit :

$$
\overrightarrow{v}\!\left( \frac{M}{R} \right) = v_0\,\overrightarrow{u_x} + r\dot{\theta}\,\overrightarrow{u_\theta}
$$

:::{important} Vitesse d'entraînement et vitesse relative
- La vitesse $\overrightarrow{v}\!\left( \frac{A}{R} \right)$ est appelée la
  **vitesse d'ensemble** ou **vitesse d'entraînement**.
- La vitesse $\overrightarrow{v}\!\left( \frac{M}{R'} \right)$ est appelée la
  **vitesse relative**.
:::

## Bilan du chapitre

Au cours de ce chapitre, nous avons décrit le mouvement d'un point matériel sans
nous préoccuper de ses causes.

- On a :
  $\overrightarrow{v}\!\left( \frac{M}{R} \right) = \left( \dfrac{d\overrightarrow{OM}}{dt} \right)_{\!/R}$
  et
  $\overrightarrow{a}\!\left( \frac{M}{R} \right) = \left( \dfrac{d\overrightarrow{v}(M/R)}{dt} \right)_{\!/R} = \left( \dfrac{d^2\overrightarrow{OM}}{dt^2} \right)_{\!/R}$.
- Il faut bien regarder et définir le référentiel d'étude et les constantes du
  problème (a-t-on $r = \text{cte}$ ? $\dfrac{d\theta}{dt} = \text{cte}$ ? …) puis
  dériver.
- Il ne sert à rien d'apprendre par cœur les expressions de la vitesse et de
  l'accélération en coordonnées polaires et/ou cylindriques, car ces expressions
  dépendent du référentiel d'étude.

:::{important} À retenir
Dans $R(O, \overrightarrow{u_x}, \overrightarrow{u_y}, \overrightarrow{u_z})$, il
faut savoir que :

$$
\begin{cases}
\left( \dfrac{d\overrightarrow{u_r}}{dt} \right)_{\!/R} = \dot{\theta}\,\overrightarrow{u_\theta} \\[2ex]
\left( \dfrac{d\overrightarrow{u_\theta}}{dt} \right)_{\!/R} = -\dot{\theta}\,\overrightarrow{u_r}
\end{cases}
$$
:::
