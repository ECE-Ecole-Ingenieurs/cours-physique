---
title: Dynamique du point matériel — Oscillations et moments
authors:
  - coralie-thieulin
keywords:
  - mouvement oscillant
  - ressort
  - pendule
  - produit vectoriel
  - moment cinétique
  - équation différentielle
abstract: |
  Ce chapitre est la suite de la dynamique. Il est consacré aux systèmes
  oscillants (pendules et systèmes masse-ressort), ainsi qu'aux mouvements
  circulaires. Les méthodes de résolution sont les mêmes que celles vues au
  chapitre précédent, mais deux nouveautés apparaissent : la résolution des
  équations différentielles du second ordre, et la résolution d'un problème de
  dynamique de mouvement circulaire à l'aide des moments.

  Nous introduisons pour cela le produit vectoriel, la notion de moment d'une
  grandeur physique, le moment cinétique et le moment de force, avant
  d'énoncer le théorème du moment cinétique — une alternative au PFD, valable
  uniquement pour les mouvements circulaires autour d'un point fixe.
---

## Introduction

Ce chapitre est la suite de la dynamique. Il est consacré aux systèmes
oscillants (pendules et systèmes masse-ressort), ainsi qu'aux mouvements
circulaires.

Les méthodes de résolution sont les mêmes que celles vues au chapitre
précédent. Néanmoins, il y a deux nouveautés : la résolution des équations
différentielles du second ordre, et la résolution d'un problème de dynamique
de mouvement circulaire à l'aide des moments.

Ce chapitre est organisé comme le précédent : on voit en exemple plusieurs
situations pour chacun des systèmes (qu'il faudra travailler, car ce sont des
applications), puis des exercices spécifiques sont aussi vus.

## Mouvements oscillants

**Situation** : on considère un corps de masse $m$ assimilé à un point
matériel $M$. Le point $M$ est en mouvement oscillatoire. On associe le
repère cartésien au référentiel. On va avoir deux types de mouvement
oscillatoire : les systèmes oscillants rectilignes et les systèmes oscillants
circulaires.

### Le ressort linéaire

Le système oscillant linéaire par excellence est le système avec un ressort.
La masse $M$ est accrochée à un ressort de raideur $k$, de masse négligeable,
de longueur au repos (longueur à vide) $l_0$.

À l'instant $t = 0$, la masse est écartée de la position d'équilibre et
lâchée avec ou sans vitesse initiale. On peut considérer ou non des
frottements. Il y a deux situations différentes : le mouvement est vertical
ou horizontal.

:::::{prf:example} Mouvement oscillant horizontal
:label: ex-ressort-horizontal
Soit une masse accrochée à un ressort de constante de raideur $k$, de masse
négligeable, de longueur au repos (longueur à vide) $l_0$. On suppose le
ressort linéaire.

:::{figure} /media/ch5-ressort-horizontal.png
:label: fig-ressort-horizontal
:align: center
:width: 45%

Masse $M$ accrochée à un ressort horizontal, de longueur $l$ à l'instant $t$.
:::

**Question** : établir l'équation différentielle du mouvement et sa solution
générale $x(t)$, avec et sans frottements solides.

::::{dropdown} Corrigé
**Sans frottements**

**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$,
$\overrightarrow{R}$ la réaction du support et la force de rappel du ressort
$\overrightarrow{F}_{\text{ressort} \rightarrow M}$.

On prend le repère cartésien afin de résoudre le problème. Le PFD nous
donne :

$$
\overrightarrow{F}_{\text{ressort} \rightarrow M} + \overrightarrow{R} + \overrightarrow{P} = m\overrightarrow{a}(M)_{/R}
$$

Dans la base $(O, \overrightarrow{u_x}, \overrightarrow{u_y})$ :
$\overrightarrow{P} = -mg\overrightarrow{u_y}$ ;
$\overrightarrow{R} = R\overrightarrow{u_y}$ ;
$\overrightarrow{F}_{\text{ressort} \rightarrow M} = -k(l - l_0)\overrightarrow{u_x}$.
Soit :

$$
\begin{cases}
-k(l - l_0) = ma \\
-mg + R = 0
\end{cases}
\Leftrightarrow
\begin{cases}
-\dfrac{k}{m}(l - l_0) = a \\
R = mg
\end{cases}
$$

car l'accélération n'a de composante que suivant $Ox$ (le mouvement est
linéaire suivant cet axe). On a alors de manière évidente :
$-\dfrac{k}{m}(l - l_0) = \ddot{x}$.

Si on ne connaît pas $l_0$, on peut exprimer l'accélération ci-dessus en
fonction de $l_e$, la longueur à l'équilibre. En effet, par définition (voir
le [chapitre sur la statique du point matériel](#statique-loi-1)) :
$-\dfrac{k}{m}(l_e - l_0) = 0$. Ainsi :

$$
-\frac{k}{m}(l - l_0) = \ddot{x}
\Leftrightarrow -\frac{k}{m}(l - l_0 + l_e - l_e) = \ddot{x}
\Leftrightarrow -\frac{k}{m}(l - l_e) + \frac{k}{m}(l_e - l_0) = \ddot{x}
\Leftrightarrow -\frac{k}{m}(l - l_e) = \ddot{x}
$$

En faisant le changement de variable $X(t) = l - l_e = x - x_e$, on a
$\dot{X}(t) = \dot{x}$ et $\ddot{X}(t) = \ddot{x}$. Alors :

$$
-\frac{k}{m}X(t) = \ddot{X}(t)
$$

C'est une **équation différentielle du second ordre**, de la forme
$\ddot{X} + \omega_0^2 X = 0$.

:::{prf:algorithm} Résoudre une équation différentielle du second ordre
:label: algo-edo-second-ordre
La solution de l'équation $\ddot{X} + \omega_0^2 X = 0$ est de la forme :

$$
X(t) = A\cos(\omega_0 t) + B\sin(\omega_0 t)
$$

Les paramètres $A$ et $B$ sont à déterminer avec les conditions initiales.
Puisqu'il y a deux paramètres, il faut utiliser deux conditions initiales :
la première sur la position $X(0)$, la seconde sur la vitesse $\dot{X}(0)$.
Il y a quatre cas différents :

| Conditions initiales | Solution |
|---|---|
| $X(0) = X_0$ et $\dot{X}(0) = 0$ | $X(t) = X_0\cos(\omega_0 t)$ |
| $X(0) = 0$ et $\dot{X}(0) = V_0$ | $X(t) = \dfrac{V_0}{\omega_0}\sin(\omega_0 t)$ |
| $X(0) = 0$ et $\dot{X}(0) = 0$ | $X(t) = 0$ |
| $X(0) = X_0$ et $\dot{X}(0) = V_0$ | $X(t) = X_0\cos(\omega_0 t) + \dfrac{V_0}{\omega_0}\sin(\omega_0 t)$ |
:::

Reprenons le cas de notre ressort. On a, de manière générale :

$$
x(t) = A\cos\left( \sqrt{\frac{k}{m}}t \right) + B\sin\left( \sqrt{\frac{k}{m}}t \right) + x_e
$$

**Avec frottements solides**

Le seul changement est qu'il y a une force de frottement solide en plus,
selon l'axe des $x$, telle que $\overrightarrow{f_s} = f_s\overrightarrow{u_x}$
(cette force est opposée au mouvement, elle est donc toujours de sens inverse
à $\overrightarrow{F}_{\text{ressort} \rightarrow M}$).

En appliquant le PFD, on obtient facilement :

$$
\begin{cases}
f_s - k(l - l_0) = ma \\
-mg + R = 0
\end{cases}
\Leftrightarrow
\begin{cases}
\mu g - \dfrac{k}{m}(l - l_0) = a \\
R = mg
\end{cases}
$$

car $f_s = \mu R$, avec $\mu$ le coefficient de frottement solide. Au final,
on obtient facilement l'équation différentielle suivante (en utilisant la
condition d'équilibre) :

$$
\ddot{X}(t) + \frac{k}{m}X(t) = 0
$$

:::{note}
C'est la même équation différentielle que sans frottements. Cela vient du
fait que la position d'équilibre inclut les frottements — c'est cette
position qui est différente, pas le mouvement d'oscillation autour.
:::
::::
:::::

:::::{prf:example} Mouvement oscillant vertical
:label: ex-ressort-vertical
:::{figure} /media/ch5-ressort-vertical.png
:label: fig-ressort-vertical
:align: center
:width: 30%

Masse $M$ accrochée à un ressort vertical, de longueur $l$ à l'instant $t$.
:::

Soit une masse accrochée à un ressort de constante de raideur $k$, de masse
négligeable, de longueur au repos (longueur à vide) $l_0$. On suppose le
ressort linéaire.

**Question** : établir l'équation différentielle du mouvement, avec et sans
frottements fluides, et comparer au cas horizontal.

::::{dropdown} Corrigé
**Sans frottements**

**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$,
et la force de rappel du ressort $\overrightarrow{F}_{\text{ressort} \rightarrow M}$.

On prend le repère cartésien afin de résoudre le problème. Le PFD nous
donne :

$$
\overrightarrow{F}_{\text{ressort} \rightarrow M} + \overrightarrow{P} = m\overrightarrow{a}(M)_{/R}
$$

Dans la base $(O, \overrightarrow{u_x}, \overrightarrow{u_y})$, et d'après le
schéma : $\overrightarrow{P} = mg\overrightarrow{u_x}$ et
$\overrightarrow{F}_{\text{ressort} \rightarrow M} = -k(l - l_0)\overrightarrow{u_x}$.
Soit : $mg - k(l - l_0) = m\ddot{x}$, car l'accélération n'a de composante
que suivant $Ox$ (le mouvement est linéaire suivant cet axe). Ce qui donne :

$$
\ddot{x} + \frac{k}{m}(l - l_0) = g
$$

On doit exprimer l'accélération ci-dessus en fonction de $l_e$, la longueur
à l'équilibre. Par définition (voir le [chapitre sur la statique du point
matériel](#statique-loi-1)) : $g - \dfrac{k}{m}(l_e - l_0) = 0$. Ainsi, en
faisant le changement de variable $X(t) = l - l_e = x - x_e$ :

$$
\ddot{X}(t) + \frac{k}{m}X(t) = 0
$$

C'est une équation différentielle du second ordre, comme nous l'avons vue
pour le ressort horizontal.

:::{note}
C'est exactement la même équation différentielle que dans le cas horizontal !
Les solutions sont donc les mêmes : physiquement, cela vient du fait que la
position d'équilibre inclut le poids dans le cas vertical.
:::

**Avec frottements fluides**

:::{attention}
Dans le cas vertical, les frottements ne sont pas solides (il n'y a pas de
support) : ils sont dus, dans le cas le plus fréquent, aux frottements de
l'air.
:::

**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$,
la force de rappel du ressort $\overrightarrow{F}_{\text{ressort} \rightarrow M}$
et $\overrightarrow{f} = -\alpha\overrightarrow{v}(M)$, la force de
frottement fluide.

Le PFD nous donne :

$$
\overrightarrow{f} + \overrightarrow{F}_{\text{ressort} \rightarrow M} + \overrightarrow{P} = m\overrightarrow{a}(M)_{/R}
$$

Dans la base $(O, \overrightarrow{u_x}, \overrightarrow{u_y})$ :
$\overrightarrow{P} = mg\overrightarrow{u_x}$ ;
$\overrightarrow{F}_{\text{ressort} \rightarrow M} = -k(l - l_0)\overrightarrow{u_x}$
et $\overrightarrow{f} = -\alpha\dot{x}\,\overrightarrow{u_x}$. Soit :
$-\alpha\dot{x} + mg - k(l - l_0) = m\ddot{x}$, ce qui donne :

$$
\ddot{x} + \frac{\alpha}{m}\dot{x} + \frac{k}{m}(l - l_0) = g
$$

En exprimant l'accélération en fonction de $l_e$ (comme précédemment) et en
faisant le changement de variable $X(t) = l - l_e = x - x_e$, on obtient :

$$
\ddot{X} + \frac{\alpha}{m}\dot{X} + \frac{k}{m}X = 0
$$

:::{note}
La résolution de cette équation différentielle sera vue au semestre 2.
:::
::::
:::::

### Le pendule

Le système oscillant circulaire par excellence est le pendule. Le pendule est
un système où la masse $M$ est accrochée à un fil sans masse, toujours tendu,
de longueur $OM = l$. À l'instant $t = 0$, le pendule possède un angle
$\theta_0$ avec la verticale, avec ou sans vitesse initiale. On peut
considérer ou non les frottements fluides (essentiellement dus à l'air).

:::::{prf:example} Le pendule simple
:label: ex-pendule-simple
**Question** : établir l'équation du mouvement du pendule et sa solution pour
les petits angles, avec et sans frottements fluides.

::::{dropdown} Corrigé
**Sans frottements**

**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$ et
$\overrightarrow{T}$ la tension du fil.

On prend le repère polaire afin de résoudre le problème. Le PFD nous donne :

$$
\overrightarrow{T} + \overrightarrow{P} = m\overrightarrow{a}(M)_{/R}
$$

Dans la base $(O, \overrightarrow{u_r}, \overrightarrow{u_\theta})$ :
$\overrightarrow{P} = mg\cos\theta\,\overrightarrow{u_r} - mg\sin\theta\,\overrightarrow{u_\theta}$
et $\overrightarrow{T} = -T\overrightarrow{u_r}$.

En effectuant une étude cinématique, on obtient que l'accélération s'écrit :

$$
\overrightarrow{a}(M/R) = -l\dot{\theta}^2\overrightarrow{u_r} + l\ddot{\theta}\overrightarrow{u_\theta}
$$

On a alors :

$$
-T\overrightarrow{u_r} + mg\cos\theta\,\overrightarrow{u_r} - mg\sin\theta\,\overrightarrow{u_\theta}
= -ml\dot{\theta}^2\overrightarrow{u_r} + ml\ddot{\theta}\overrightarrow{u_\theta}
$$

Soit :

$$
\begin{cases}
-T + mg\cos\theta = -ml\dot{\theta}^2 \\
-mg\sin\theta = ml\ddot{\theta}
\end{cases}
\Leftrightarrow
\begin{cases}
-T + g\cos\theta + l\dot{\theta}^2 = 0 \\
l\ddot{\theta} + g\sin\theta = 0
\end{cases}
$$

La première équation lie le carré de la vitesse angulaire à l'angle et à la
tension du fil. La seconde est l'**équation du mouvement** :
$l\ddot{\theta} + g\sin\theta = 0$.

:::{attention}
Cette équation ne peut pas être résolue analytiquement pour tous les angles.
Par contre, pour les petits angles, oui ! Si $\theta \ll 1$, alors
$\sin\theta \sim \theta$, et l'équation du mouvement devient :
$l\ddot{\theta} + g\theta = 0$ — une équation différentielle du second ordre.
:::

Reprenons notre problème et appliquons cela à notre pendule. L'équation du
second ordre était $l\ddot{\theta} + g\theta = 0$, soit
$\ddot{\theta} + \dfrac{g}{l}\theta = 0$, soit
$\ddot{\theta} + \omega_0^2\theta = 0$ avec $\omega_0^2 = \dfrac{g}{l}$.

La solution générale est donc
$\theta(t) = A\cos\left( \sqrt{\dfrac{g}{l}}t \right) + B\sin\left( \sqrt{\dfrac{g}{l}}t \right)$,
et donc, suivant le cas étudié (conditions initiales de l'énoncé) :

- si $\theta(0) = \theta_0$ et $\dot{\theta}(0) = 0$, alors
  $\theta(t) = \theta_0\cos(\omega_0 t)$ ;
- si $\theta(0) = \theta_0$ et $\dot{\theta}(0) = V_0$, alors
  $\theta(t) = \theta_0\cos(\omega_0 t) + \dfrac{V_0}{\omega_0}\sin(\omega_0 t)$.

**Avec frottements fluides**

**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$,
$\overrightarrow{T}$ la tension du fil et $\overrightarrow{f} = -\alpha\overrightarrow{v}(M)$,
la force de frottement fluide.

On prend le repère polaire afin de résoudre le problème. Le PFD nous donne :

$$
\overrightarrow{f} + \overrightarrow{T} + \overrightarrow{P} = m\overrightarrow{a}(M)_{/R}
$$

Dans la base $(O, \overrightarrow{u_r}, \overrightarrow{u_\theta})$ :
$\overrightarrow{P} = mg\cos\theta\,\overrightarrow{u_r} - mg\sin\theta\,\overrightarrow{u_\theta}$,
$\overrightarrow{T} = -T\overrightarrow{u_r}$ et
$\overrightarrow{f} = -\alpha\left( v_r\overrightarrow{u_r} + v_\theta\overrightarrow{u_\theta} \right)$.

En effectuant une étude cinématique, on obtient que la vitesse et
l'accélération s'écrivent :

$$
\overrightarrow{v}(M) = l\dot{\theta}\,\overrightarrow{u_\theta}
\qquad
\overrightarrow{a}(M) = -l\dot{\theta}^2\overrightarrow{u_r} + l\ddot{\theta}\overrightarrow{u_\theta}
$$

L'équation du mouvement devient $-\alpha l\dot{\theta} - mg\sin\theta = ml\ddot{\theta}$,
soit :

$$
\ddot{\theta} + \frac{\alpha}{m}\dot{\theta} + \frac{g}{l}\sin\theta = 0
$$

De nouveau, cette équation n'a pas de solution analytique pour tous les
angles. Pour les petits angles ($\theta \ll 1$, donc $\sin\theta \sim \theta$),
l'équation du mouvement devient :

$$
\ddot{\theta} + \frac{\alpha}{m}\dot{\theta} + \frac{g}{l}\theta = 0
$$

:::{note}
La résolution de cette équation différentielle sera vue au semestre 2, comme
pour le ressort.
:::
::::
:::::

## Théorème du moment cinétique

Le théorème du moment cinétique est très utile dans les problèmes
circulaires. Il sert à résoudre le problème comme on peut le faire avec la
seconde loi de Newton (PFD) : c'est une autre manière de faire. Il découle
directement du PFD (la démonstration est triviale).

:::{attention}
Il n'est valable que pour les mouvements circulaires !
:::

Commençons par définir ce qu'est le moment d'une grandeur
physique.

### Préambule : notion de produit vectoriel

:::{prf:definition} Produit vectoriel
:label: def-produit-vectoriel
Le produit vectoriel de deux vecteurs $\overrightarrow{u}$ et
$\overrightarrow{v}$ est un vecteur noté
$\overrightarrow{c} = \overrightarrow{u} \wedge \overrightarrow{v}$. Le
vecteur résultant $\overrightarrow{c}$ est tel que :

- sa direction est perpendiculaire aux vecteurs $\overrightarrow{u}$ et
  $\overrightarrow{v}$ ;
- sa norme est
  $\left\| \overrightarrow{u} \right\| \left\| \overrightarrow{v} \right\| \left| \sin\left( \overrightarrow{u}, \overrightarrow{v} \right) \right|$ ;
- son sens est donné par la règle du trièdre direct.

De plus, on a :

- $\overrightarrow{u} \wedge \overrightarrow{v} = -\overrightarrow{v} \wedge \overrightarrow{u}$ ;
- $\overrightarrow{u} \wedge \overrightarrow{v} = \overrightarrow{0} \Leftrightarrow \overrightarrow{u}$
  et $\overrightarrow{v}$ sont colinéaires.
:::

**Méthode 1 — Méthode du gamma**

Soient deux vecteurs
$\overrightarrow{u} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}$ et
$\overrightarrow{v} = \begin{pmatrix} d \\ e \\ f \end{pmatrix}$, exprimés
dans une BOND quelconque $(\overrightarrow{i}, \overrightarrow{j}, \overrightarrow{k})$.

La méthode du « gamma » permet de calculer le produit vectoriel
$\overrightarrow{u} \wedge \overrightarrow{v}$ simplement et rapidement : pour
connaître le résultat selon $\overrightarrow{i}$, on écrit les deux vecteurs
en colonne et l'on barre les composantes selon $\overrightarrow{i}$ (on
procède de même pour $\overrightarrow{j}$ et $\overrightarrow{k}$). Ainsi, on
obtient :

$$
\overrightarrow{u} \wedge \overrightarrow{v} = \begin{pmatrix} bf - ce \\ cd - af \\ ae - bd \end{pmatrix}
$$

**Méthode 2 — Méthode de calcul rapide pour une BOND**

Le produit vectoriel entre deux vecteurs unitaires d'une BOND donne, au signe
près, le troisième vecteur de la base. Pour retrouver facilement les
résultats, il suffit d'écrire sur son brouillon la base deux fois. Par
exemple, pour la base cartésienne, on écrit :
$\overrightarrow{e_x}\ \overrightarrow{e_y}\ \overrightarrow{e_z}\ \overrightarrow{e_x}\ \overrightarrow{e_y}\ \overrightarrow{e_z}$.

Ensuite, il suffit de suivre le sens du produit vectoriel recherché :

- si je cherche $\overrightarrow{e_x} \wedge \overrightarrow{e_y}$, je me
  déplace vers la droite (sens direct), donc le résultat est $+\overrightarrow{e_z}$ ;
- si je cherche $\overrightarrow{e_y} \wedge \overrightarrow{e_x}$, je me
  déplace vers la gauche (sens indirect), donc le résultat est $-\overrightarrow{e_z}$.

### La notion de moment

:::{prf:definition} Moment d'une grandeur physique
:label: def-moment
Le moment d'une grandeur physique $\overrightarrow{A}$ représente la
capacité de cette grandeur à faire tourner un système autour d'un point. Dans
le cas de la mécanique du point matériel, tous les moments représentent donc
la capacité des grandeurs à faire tourner le point matériel (la masse $m$)
autour d'un point fixe.

**Un moment est forcément un vecteur** (il est dirigé selon l'axe de
rotation) et il est toujours calculé en un point. Le moment d'une grandeur
s'exprime par :

$$
\overrightarrow{M_O}\left( \overrightarrow{A} \right) = \overrightarrow{OM} \wedge \overrightarrow{A}
$$

Le point $O$ est le point de calcul, c'est le point fixe autour duquel tourne
le point $M$. Le point $M$ est le point matériel dont le mouvement est
étudié. La grandeur $\overrightarrow{A}$ est la grandeur physique qui
s'applique sur $M$.
:::

Un moment est très lié au phénomène de balancier. On appelle souvent le point
$O$ le **pivot**, la distance $OM$ le **levier**, et le point $M$ le **point
d'application**.

### Le moment cinétique

Le moment cinétique est le moment de la quantité de mouvement (exemple : le
spin de l'électron).

:::{prf:definition} Moment cinétique
:label: def-moment-cinetique
La {term}`quantité de mouvement` en référentiel galiléen d'un point matériel
s'exprime par $\overrightarrow{p}(M) = m\overrightarrow{v}(M)_{/R}$. Son
moment, noté $\overrightarrow{L_O}\left( \overrightarrow{p} \right)$ avec $O$
le point autour duquel tourne le point $M$, est le **moment cinétique** en
$O$ :

$$
\overrightarrow{L_O}\left( \overrightarrow{p} \right) = \overrightarrow{OM} \wedge m\overrightarrow{v}(M)
$$
:::

De manière pragmatique, puisque le mouvement est circulaire, vous devez
savoir retrouver la vitesse en coordonnées cylindriques (ou polaires) très
rapidement (comme dans le cas du pendule) : c'est de la cinématique.

### Le moment de force

Le moment de force est le moment d'une force appliquée sur le point $M$. Le
théorème du moment cinétique relie le moment cinétique et le moment des
forces qui s'appliquent au point $M$.

:::{prf:definition} Moment de force
:label: def-moment-force
Le moment d'une force est noté $\overrightarrow{M_O}\left( \overrightarrow{F} \right)$,
avec $O$ le point autour duquel tourne le point $M$. On a, pour chacune des
forces s'appliquant sur un point matériel $M$ animé d'un mouvement circulaire
autour d'un point $O$ fixe, le moment de force en $O$ suivant :

$$
\overrightarrow{M_O}\left( \overrightarrow{F} \right) = \overrightarrow{OM} \wedge \overrightarrow{F}
$$
:::

Chacune des forces appliquées au point $M$ possède un moment distinct,
calculé au point $O$.

### Le théorème du moment cinétique

:::{prf:theorem} Théorème du moment cinétique
:label: theoreme-moment-cinetique
La dérivée par rapport au temps du moment cinétique, calculé en un point $O$
fixe dans le référentiel d'étude et autour duquel tourne un point matériel
$M$, est égale à la somme des moments des forces calculés en $O$
s'appliquant sur $M$ :

$$
\frac{d\overrightarrow{L_O}\left( \overrightarrow{p} \right)}{dt} = \sum \overrightarrow{M_O}\left( \overrightarrow{F}_{\rightarrow M} \right)
$$
:::

En exprimant, grâce à leur définition, les grandeurs dans la relation
précédente, on a :

$$
\frac{d}{dt}\left( \overrightarrow{OM} \wedge m\overrightarrow{v}(M) \right) = \sum \overrightarrow{OM} \wedge \overrightarrow{F}
\qquad \text{ou} \qquad
m\frac{d}{dt}\left( \overrightarrow{OM} \wedge \overrightarrow{v}(M) \right) = \overrightarrow{OM} \wedge \sum \overrightarrow{F}
$$

:::{note}
Si vous ne vous trompez pas, les produits vectoriels sont tous uniquement
suivant un seul axe, et c'est le même pour tous.
:::

## Bilan du chapitre

Dans ce chapitre, nous avons vu comment résoudre des problèmes de mouvements
oscillants, circulaires ou rectilignes, à l'aide de la seconde loi de Newton.
Nous avons regardé la méthodologie à appliquer à travers des exemples et des
exercices pour chaque cas : il faut bien revoir les coordonnées polaires et
cylindriques ({term}`vitesse instantanée`, {term}`accélération`) ainsi que
les forces de rappel des ressorts.

Il y a cependant deux nouveautés dans ce chapitre :

- l'équation différentielle du second ordre ;
- le théorème du moment cinétique. C'est une autre manière de déterminer
  l'équation du mouvement (sans utiliser le PFD). Il faut bien maîtriser et
  revoir le produit vectoriel pour pouvoir l'appliquer efficacement, ainsi
  que la cinématique en coordonnées polaires et cylindriques.

:::{attention}
Ce théorème n'est valable, en mécanique du point matériel, que pour un
mouvement circulaire autour d'un point fixe.
:::
