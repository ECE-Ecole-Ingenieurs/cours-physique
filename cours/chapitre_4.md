---
title: Dynamique du point matériel — Mouvements usuels
authors:
  - coralie-thieulin
keywords:
  - dynamique
  - PFD
  - chute libre
  - balistique
  - plan incliné
  - équation différentielle
abstract: |
  La dynamique est la branche de la mécanique du point matériel qui permet
  d'étudier les changements provoqués par les forces sur les mouvements du
  point matériel en référentiel galiléen. Nous relions ici les forces à la
  vitesse et à l'accélération du point matériel grâce au principe fondamental
  de la dynamique (PFD), c'est la loi centrale de ce chapitre.

  Après avoir posé une méthodologie en neuf étapes, nous l'appliquons à trois
  familles de problèmes classiques : le mouvement rectiligne (sur sol plat ou
  incliné, avec ou sans frottements), la chute libre, et la balistique, en
  distinguant chaque fois le cas sans frottements de l'air du cas avec
  frottements.
---

## Introduction

La dynamique est la branche de la mécanique du point matériel qui permet
d'étudier les changements provoqués par les forces sur les mouvements du
point matériel en référentiel galiléen. Nous allons donc relier les forces à la
vitesse et à l'accélération du point matériel. Pour cela, il faut utiliser
l'ensemble des lois de Newton que nous avons vues depuis le premier chapitre
(lois fondamentales), ainsi que la notion de {term}`référentiel` et de
cinématique. À ce point du cours, la seule loi que nous n'avons pas encore
utilisée est la seconde loi de Newton, qui relie les forces à l'accélération :
c'est la loi centrale pour l'étude dynamique des mouvements d'un point
matériel en référentiel galiléen.

::::{note} Rappel
Dans ce chapitre, on utilisera surtout le principe fondamental de la dynamique
(PFD) :

:::{math}
:enumerated: false
\overrightarrow{F} = m\overrightarrow{a}(M)_{/R}
:::

Pour l'énoncé complet des lois de Newton, voir le chapitre
« [Principes fondamentaux](#lois-newton) ».
::::

Comme nous l'avons déjà vu, la première loi (que l'on doit à Galilée) découle
de fait de la seconde loi. En effet, si la vitesse est constante, la somme des
forces est égale à $\overrightarrow{0}$ d'après cette loi. L'étude dynamique
se résume en apparence à n'utiliser que la seconde loi de Newton, mais il faut
bien garder en tête que ces lois sont toutes présentes (et utilisables,
notamment la troisième…).

## Comment résoudre un problème de dynamique

Pour résoudre un problème de dynamique du point matériel, il y a différentes
étapes à franchir. Elles sont toujours les mêmes.

:::{prf:algorithm} Résoudre un problème de dynamique
:label: algo-dynamique
1. **Identifier le système** : il faut identifier le système qui nous
   intéresse dans le problème. Si celui-ci n'est pas donné, il faut faire un
   dessin du système.
2. **Définir le référentiel d'étude** : bien définir le référentiel d'étude
   par rapport au système afin de pouvoir étudier correctement le mouvement
   du point.
3. **Faire le bilan des forces** : on fait le bilan des forces qui
   s'appliquent sur le point matériel étudié dont on cherche à
   définir/prédire le mouvement. Dans cette étape, il faut identifier les
   forces et les lister.
4. **Choisir un repère d'étude de résolution** : on choisit le repère
   mathématique le plus adapté à la résolution du problème (rappel : celui-ci
   n'est pas forcément le même que le repère associé au référentiel !).
5. **Exprimer les forces dans le repère choisi** : on détermine les
   composantes des forces dans la base orthonormée directe choisie (la plus
   adaptée à la résolution du problème).
6. **Appliquer le PFD** : on applique le principe fondamental de la dynamique
   au système. On obtient une relation vectorielle entre les forces et
   l'accélération.
7. **Projeter sur les axes du repère** : on exprime le PFD sur chacun des
   axes du repère choisi. On obtient, au plus, trois équations reliant les
   composantes des forces aux composantes de l'accélération.
8. **Déterminer les composantes de l'accélération** : à ce point, il faut
   déterminer les composantes de l'accélération (selon quels axes
   l'accélération possède des composantes ?). Ceci se fait en déterminant à
   quel mouvement correspond le problème.
9. **Résoudre le système d'équations** : on résout le système d'équations
   obtenues afin de remonter jusqu'à l'équation du mouvement. Cela se résout
   donc exactement comme un problème de cinématique pur : de l'accélération
   on intègre afin d'obtenir la vitesse, puis, après une nouvelle intégration, la
   position.
:::

Ce programme en plusieurs étapes est toujours à suivre, quel que soit le
problème ou les questions posées.

Nous allons regarder, sous forme d'exemples résolus et d'applications, les
principaux problèmes que l'on rencontre en dynamique du point matériel.

## Mouvement rectiligne (sur sol plat)

C'est le mouvement le plus simple. Néanmoins, il faudra distinguer différents
cas : avec ou sans frottements, avec ou sans force motrice. Commençons par la
forme la plus générale (c'est-à-dire avec frottements et force motrice).

:::::{prf:example} Problème général
:label: ex-rectiligne-sol-plat
**Situation** : on considère un corps de masse $m$ assimilé à un point
matériel $M$ en mouvement sur le sol. La masse est soumise à une force
horizontale motrice. On considère les frottements solides. Le référentiel
d'étude est le référentiel terrestre supposé galiléen.

:::{figure} /media/ch4-rectiligne-sol-plat.png
:label: fig-rectiligne-sol-plat
:align: center
:width: 55%

Bilan des forces sur le point $M$ : poids $\overrightarrow{P}$, réaction
normale $\overrightarrow{R_N}$, frottement $\overrightarrow{f}$ et force
motrice $\overrightarrow{F}$.
:::

**Question** : établir, dans chacun des quatre cas limites (avec/sans
frottements, avec/sans force motrice), l'accélération et l'équation horaire
$x(t)$ du mouvement.

::::{dropdown} Corrigé
**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$ ;
la réaction du sol, que l'on peut décomposer en deux forces —
$\overrightarrow{R_N}$ la réaction normale au sol et $\overrightarrow{f}$ la
force de frottement solide, dirigée selon la direction du sol et opposée au
mouvement ; la force motrice $\overrightarrow{F}$, dirigée dans le sens du
mouvement, parallèlement au sol.

On prend le repère cartésien afin de résoudre le problème. Le PFD nous
donne :

$$
\overrightarrow{R_N} + \overrightarrow{f} + \overrightarrow{P} + \overrightarrow{F} = m\overrightarrow{a}(M)_{/R}
$$

En coordonnées, suivant les axes du repère associé au référentiel d'étude :
$\overrightarrow{P} = -mg\overrightarrow{u_y}$ ;
$\overrightarrow{R_N} = R_N\overrightarrow{u_y}$ ;
$\overrightarrow{f} = -f\overrightarrow{u_x}$ ;
$\overrightarrow{F} = F\overrightarrow{u_x}$. Alors :

$$
R_N\overrightarrow{u_y} - f\overrightarrow{u_x} - mg\overrightarrow{u_y} + F\overrightarrow{u_x}
= ma_x\overrightarrow{u_x} + ma_y\overrightarrow{u_y}
$$

Soit les deux équations :

$$
\begin{cases}
a_x = -\dfrac{f}{m} + \dfrac{F}{m} \\[1ex]
a_y = \dfrac{R_N}{m} - g
\end{cases}
$$

Or le mouvement est rectiligne suivant $(Ox)$ : $a_y = 0$. Donc :

$$
\begin{cases}
a_x = -\dfrac{f}{m} + \dfrac{F}{m} \\[1ex]
0 = \dfrac{R_N}{m} - g
\end{cases}
$$

### Avec frottements et avec force motrice

C'est le cas général.

$$
\begin{cases}
a_x = -\dfrac{f}{m} + \dfrac{F}{m} \\[1ex]
0 = \dfrac{R_N}{m} - g
\end{cases}
\Leftrightarrow
\begin{cases}
a_x = -\dfrac{f + F}{m} \\[1ex]
\mu mg = f
\end{cases}
\Leftrightarrow a_x = -\mu g + \frac{F}{m}
$$

En intégrant entre les instants $0$ et $t$, on a :
$v(t) = \left( -\mu g + \dfrac{F}{m} \right)t + V_0$.

En intégrant de nouveau, on a :
$x(t) = \dfrac{1}{2}\left( -\mu g + \dfrac{F}{m} \right)t^2 + V_0 t + x(t=0)$.

Le mouvement peut être rectiligne uniformément retardé ou accéléré, en
fonction du signe de $-\mu g + \dfrac{F}{m}$.

### Avec frottements et sans force motrice

On a donc $F = 0$. Alors :

$$
\begin{cases}
a_x = -\dfrac{f}{m} \\[1ex]
0 = \dfrac{R_N}{m} - g
\end{cases}
\Leftrightarrow
\begin{cases}
a_x = -\dfrac{f}{m} \\[1ex]
mg = R_N
\end{cases}
$$

et comme $f = \mu R_N$ avec $\mu$ le coefficient de frottement solide, on a
donc :

$$
\begin{cases}
a_x = -\dfrac{f}{m} \\[1ex]
\mu mg = f
\end{cases}
\Leftrightarrow a_x = -\mu g
$$

En intégrant entre les instants $0$ et $t$, on a facilement :
$v(t) = -\mu g t + v(t=0) = -\mu g t + V_0$.

En intégrant de nouveau : $x(t) = -\dfrac{\mu g}{2}t^2 + V_0 t + x(t=0)$.

On a donc un mouvement rectiligne uniformément retardé.

### Sans frottements et avec force motrice

On a donc $f = 0$ et $a_x = +\dfrac{F}{m}$.

En intégrant entre les instants $0$ et $t$, on a : $v(t) = \dfrac{F}{m}t + V_0$.

En intégrant de nouveau : $x(t) = \dfrac{F}{2m}t^2 + V_0 t + x(t=0)$.

C'est un mouvement rectiligne uniformément accéléré.

### Sans frottements et sans force motrice

On a donc $f = 0$ et $F = 0$. Alors :

$$
\begin{cases}
0 = 0 \\
0 = \dfrac{R_N}{m} - g
\end{cases}
$$

donc $\sum \overrightarrow{F} = \overrightarrow{0}$. Alors, d'après le
principe d'inertie, s'il y a mouvement à $t = 0\ \mathrm{s}$ à la vitesse
$\overrightarrow{V_0}$, on a directement : $v(t) = \text{cte} = V_0$.

En intégrant, on a donc : $x(t) = V_0 t + x(t=0)$.

C'est un mouvement rectiligne uniforme.
::::
:::::

## Mouvement rectiligne (sur sol incliné)

C'est le même mouvement que précédemment, mais cette fois-ci le sol fait un
angle avec l'horizontale. On peut distinguer deux cas : avec ou sans
frottements solides.

:::::{prf:example} Sans frottements
:label: ex-incline-sans-frottements
**Situation** : on considère un corps de masse $m$ assimilé à un point
matériel $M$ glissant sur une pente. On ne considère pas les frottements
solides. Le référentiel d'étude est le référentiel terrestre supposé
galiléen.

:::{figure} /media/ch4-incline-sans-frottements.png
:label: fig-incline-sans-frottements
:align: center
:width: 45%

Bilan des forces sur le plan incliné, sans frottements : poids
$\overrightarrow{P}$ et réaction normale $\overrightarrow{R_N}$.
:::

**Question** : déterminer l'accélération et l'équation horaire du mouvement
de $M$ sur la pente.

::::{dropdown} Corrigé
**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$ ;
$\overrightarrow{R_N}$ la réaction normale au sol.

On prend le repère cartésien afin de résoudre le problème. Le PFD nous
donne :

$$
\overrightarrow{R_N} + \overrightarrow{P} = m\overrightarrow{a}(M)_{/R}
$$

Dans la base $(O, \overrightarrow{u_x}, \overrightarrow{u_y})$ :
$\overrightarrow{P} = mg\sin\alpha\,\overrightarrow{u_x} - mg\cos\alpha\,\overrightarrow{u_y}$ ;
$\overrightarrow{R_N} = R_N\overrightarrow{u_y}$. Alors :

$$
\begin{cases}
a_x = g\sin\alpha \\[1ex]
a_y = \dfrac{R_N}{m} - g\cos\alpha
\end{cases}
$$

Or le mouvement est rectiligne suivant $(Ox)$ : $a_y = 0$. Donc :

$$
\begin{cases}
a_x = g\sin\alpha \\[1ex]
0 = \dfrac{R_N}{m} - g\cos\alpha
\end{cases}
\Leftrightarrow
\begin{cases}
a_x = g\sin\alpha \\[1ex]
R_N = mg\cos\alpha
\end{cases}
$$

L'accélération vaut donc $a_x = g\sin\alpha$.

En intégrant entre les instants $0$ et $t$ : $v(t) = (g\sin\alpha)\,t + v(t=0)$.

En intégrant de nouveau :
$x(t) = \dfrac{1}{2}(g\sin\alpha)\,t^2 + v(t=0)\,t + x(t=0)$.

C'est un mouvement rectiligne uniformément accéléré (l'accélération est
effectivement constante).
::::
:::::

:::::{prf:example} Avec frottements
:label: ex-incline-avec-frottements
**Situation** : on considère un corps de masse $m$ assimilé à un point
matériel $M$ glissant sur une pente. On considère les frottements solides. Le
référentiel d'étude est le référentiel terrestre supposé galiléen.

:::{figure} /media/ch4-incline-avec-frottements.png
:label: fig-incline-avec-frottements
:align: center
:width: 45%

Bilan des forces sur le plan incliné, avec frottements : poids
$\overrightarrow{P}$, réaction normale $\overrightarrow{R_N}$ et frottement
$\overrightarrow{f}$.
:::

**Question** : déterminer l'accélération et l'équation horaire du mouvement
de $M$ sur la pente, en tenant compte des frottements solides.

::::{dropdown} Corrigé
**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$ ;
$\overrightarrow{R_N}$ la réaction normale au sol ; $\overrightarrow{f}$ la
force de frottement solide.

On prend le repère cartésien afin de résoudre le problème. Le PFD nous
donne :

$$
\overrightarrow{R_N} + \overrightarrow{P} + \overrightarrow{f} = m\overrightarrow{a}(M)_{/R}
$$

Dans la base $(O, \overrightarrow{u_x}, \overrightarrow{u_y})$ :
$\overrightarrow{P} = mg\sin\alpha\,\overrightarrow{u_x} - mg\cos\alpha\,\overrightarrow{u_y}$ ;
$\overrightarrow{R_N} = R_N\overrightarrow{u_y}$ ; $\overrightarrow{f} = -f\overrightarrow{u_x}$.
Alors :

$$
\begin{cases}
a_x = g\sin\alpha - \dfrac{f}{m} \\[1ex]
a_y = \dfrac{R_N}{m} - g\cos\alpha
\end{cases}
\Leftrightarrow
\begin{cases}
a_x = g\sin\alpha - \dfrac{f}{m} \\[1ex]
\mu g m\cos\alpha = f
\end{cases}
$$

car le mouvement est rectiligne suivant $(Ox)$ ($a_y = 0$) et
$f = \mu R_N$, où $\mu$ est le coefficient de frottement. Donc l'accélération
vaut :

$$
a_x = g\sin\alpha - \mu g\cos\alpha = g\left( \sin\alpha - \mu\cos\alpha \right)
$$

En intégrant entre les instants $0$ et $t$ :
$v(t) = g\left( \sin\alpha - \mu\cos\alpha \right)t + V_0$.

En intégrant de nouveau :
$x(t) = \dfrac{g}{2}\left( \sin\alpha - \mu\cos\alpha \right)t^2 + V_0 t + x(t=0)$.

C'est un mouvement rectiligne uniformément accéléré ou retardé, suivant le
signe de $\sin\alpha - \mu\cos\alpha$.
::::
:::::

## La chute libre

C'est un problème qui a occupé les scientifiques pendant longtemps, jusqu'à
Newton dans les faits. C'est un problème « standard » à résoudre en dynamique
du point matériel. Il s'agit du mouvement d'un corps partant d'une altitude
donnée et lâché sans vitesse initiale. On peut distinguer deux cas : sans et
avec frottement de l'air.

:::::{prf:example} Sans frottements de l'air
:label: ex-chute-libre-sans-frottements
**Situation** : on considère un corps de masse $m$ assimilé à un point
matériel $M$, situé à une hauteur $h_0$ du sol à $t = 0$. La masse est lâchée
**sans vitesse initiale**. On ne considère pas les frottements de l'air. Le
référentiel d'étude est le référentiel terrestre supposé galiléen.

:::{figure} /media/ch4-chute-libre-sans-frottements.png
:label: fig-chute-libre-sans-frottements
:align: center
:width: 35%

Chute libre sans frottements : le point $M(m)$ tombe d'une hauteur $h_0$ sous
l'effet du seul poids $\overrightarrow{P}$.
:::

**Question** : que se passe-t-il lorsque la masse est lâchée ? Déterminer
l'accélération, la vitesse et l'équation horaire $z(t)$ du point $M$, ainsi
que son temps de chute.

::::{dropdown} Corrigé
La masse $m$ va chuter jusqu'au sol. Comme il n'y a pas de frottements, la
masse est soumise uniquement à son poids.

**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$.

On prend le repère cartésien afin de résoudre le problème. Le PFD nous
donne :

$$
\overrightarrow{P} = m\overrightarrow{a}(M)_{/R}
$$

Ici, il est facile d'établir que l'accélération n'a de composante que selon
la verticale. En effet, d'après $\overrightarrow{P} = m\overrightarrow{a}(M)_{/R}$,
le vecteur accélération est colinéaire au vecteur poids. Comme ce dernier est
toujours selon la verticale, $\overrightarrow{a}(M)_{/R}$ est lui aussi
uniquement suivant la verticale. Ce qui donne :

$$
-mg\overrightarrow{u_z} = ma_z\overrightarrow{u_z}
\Leftrightarrow -g\overrightarrow{u_z} = a_z\overrightarrow{u_z}
\Leftrightarrow a_z = -g
$$

En intégrant entre les instants $0$ et $t$, on a facilement : $v(t) = -gt + v(t=0)$.
Or ici $v(t=0) = 0$, donc $v(t) = -gt$.

En intégrant de nouveau entre les instants $0$ et $t$ :
$z(t) = -\dfrac{1}{2}gt^2 + z(t=0)$. Or $z(t=0) = h_0$, donc :

$$
z(t) = -\frac{1}{2}gt^2 + h_0
$$

Le point $M$ est donc animé d'un mouvement rectiligne uniformément accéléré.

On peut calculer facilement le **temps de chute** (c'est-à-dire le temps mis
par la masse pour passer d'une hauteur $h_0$ à $0$) :

$$
0 = -\frac{1}{2}g t_c^2 + h_0
\Leftrightarrow t_c^2 = 2\frac{h_0}{g}
\Leftrightarrow t_c = \sqrt{2\frac{h_0}{g}}
$$

À cet instant : $v(t_c) = g\,t_c = g\sqrt{2\dfrac{h_0}{g}} = \sqrt{2gh_0}$.
::::
:::::

:::::{prf:example} Avec frottements de l'air
:label: ex-chute-libre-avec-frottements
**Énoncé** : on considère un corps de masse $m$ assimilé à un point matériel
$M$, situé à une hauteur $h_0$ du sol à $t = 0$. La masse est lâchée sans
vitesse initiale. On considère les frottements de l'air tels que
$\overrightarrow{f} = -\alpha\overrightarrow{v}$. Le référentiel d'étude est
le référentiel terrestre supposé galiléen.

:::{figure} /media/ch4-chute-libre-avec-frottements.png
:label: fig-chute-libre-avec-frottements
:align: center
:width: 35%

Chute libre avec frottements de l'air : le poids $\overrightarrow{P}$ et le
frottement $\overrightarrow{f}$ s'opposent.
:::

**Question** : que se passe-t-il lorsque la masse est lâchée ? Déterminer la
vitesse $v(t)$ et la position $z(t)$ du point $M$, ainsi que sa vitesse
limite.

::::{dropdown} Corrigé
La masse $m$ va chuter jusqu'au sol.

**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$ et
la force de frottement $\overrightarrow{f} = -\alpha\overrightarrow{v}$.

Le PFD nous donne :

$$
\overrightarrow{P} + \overrightarrow{f} = m\overrightarrow{a}(M)_{/R}
\Leftrightarrow -mg\overrightarrow{u_z} - \alpha v_z\overrightarrow{u_z} = ma_z\overrightarrow{u_z}
$$

On a donc $-mg - \alpha v_z = ma_z$. Or $a_z = \left( \dfrac{dv_z}{dt} \right)_{\!/R}$,
donc :

$$
\frac{dv_z}{dt} + \frac{\alpha}{m}v_z = -g
$$

:::{note}
C'est une équation différentielle du premier ordre. En effet, elle est de la
forme $\dot{X} + \dfrac{1}{\tau}X = A$, avec $A$ et $\tau$ des constantes
données.
:::

:::{prf:algorithm} Résoudre une équation différentielle du premier ordre
:label: algo-edo-premier-ordre
La solution de l'équation $\dot{X} + \dfrac{1}{\tau}X = A$ est de la forme :

$$
X(t) = A\tau + Ke^{-t/\tau}
$$

avec $A\tau$ la solution particulière et $Ke^{-t/\tau}$ la solution générale.

1. La **solution particulière** est trouvée en considérant, dans l'équation
   différentielle, $\dfrac{dX}{dt} = 0$.
2. La **constante $K$** est à déterminer en utilisant une condition initiale
   (condition à $t = 0$). En pratique, on connaît $x(0) = C$ avec $C$
   constant. Or $x(0) = A\tau + Ke^0 = A\tau + K$, donc
   $K = C - A\tau$.

Au final : $x(t) = A\tau + (C - A\tau)e^{-t/\tau}$.
:::

Reprenons notre problème et appliquons cet algorithme.

La solution particulière de $\dfrac{dv}{dt} + \dfrac{\alpha}{m}v = -g$ est
$v_p = -mg/\alpha$. La solution générale est $v_G = Ke^{-\alpha t/m}$.

D'après les conditions initiales, on sait que $v(0) = 0$. Alors on a
$v(0) = 0 = -\dfrac{mg}{\alpha} + K$. Ce qui donne l'expression de la vitesse :

$$
v(t) = -\frac{mg}{\alpha} + \frac{mg}{\alpha}e^{-\alpha t/m}
$$

:::{attention}
Rappelons que cette vitesse est négative, car le corps qui chute se dirige de
haut en bas (à l'opposé de $Oz$ défini).
:::

La norme de la vitesse est la valeur absolue de $v(t)$, soit :

$$
\left| v(t) \right| = \frac{mg}{\alpha}\left( 1 - e^{-\alpha t/m} \right)
$$

:::{important}
La valeur $\dfrac{mg}{\alpha}$ correspond à la **vitesse limite** atteinte
par le corps — c'est la valeur limite de $\left| v(t) \right|$ lorsque $t$
tend vers l'infini. C'est aussi la valeur absolue de la solution
particulière.
:::

Pour obtenir la position du corps au cours du temps, il faut intégrer $v(t)$.
On obtient :

$$
z(t) = -\frac{mg}{\alpha}t - \left( \frac{m}{\alpha} \right)^2 g\left[ e^{-\alpha t/m} - 1 \right] + h_0
$$
::::
:::::

## La balistique

La balistique consiste à envoyer un objet en lui donnant une vitesse initiale
et un angle donné par rapport à l'horizontale. La balistique concerne donc
tous les problèmes de lancer, de jet de projectile, de divers sports, etc.
C'est donc un problème « commun » à résoudre en dynamique du point matériel.
De nouveau, nous allons distinguer deux cas : sans et avec frottement de
l'air.

:::::{prf:example} Sans frottements de l'air
:label: ex-balistique-sans-frottements
**Situation** : on considère un corps de masse $m$ assimilé à un point
matériel $M$. À $t = 0$, on lance un objet de masse $m$ avec une vitesse
$V_0$ faisant un angle $\theta$ avec l'axe $Ox$. On ne considère pas les
frottements de l'air. Le référentiel d'étude est le référentiel terrestre
supposé galiléen.

:::{figure} /media/ch4-balistique-sans-frottements.png
:label: fig-balistique-sans-frottements
:align: center
:width: 35%

Trajectoire balistique sans frottements : vitesse initiale $\overrightarrow{V_0}$
et poids $\overrightarrow{P}$.
:::

**Question** : déterminer les équations horaires $x(t)$ et $y(t)$, ainsi que
l'équation de la trajectoire $y(x)$.

::::{dropdown} Corrigé
**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$.

On prend le repère cartésien afin de résoudre le problème. Le PFD nous
donne : $\overrightarrow{P} = m\overrightarrow{a}(M)_{/R}$.

Dans la base $(O, \overrightarrow{u_x}, \overrightarrow{u_y})$ :
$\overrightarrow{P} = -mg\overrightarrow{u_y}$. Alors on a :
$-mg\overrightarrow{u_y} = ma_x\overrightarrow{u_x} + ma_y\overrightarrow{u_y}$.

Soit les deux équations :

$$
\begin{cases}
a_x = 0 \\
a_y = -g
\end{cases}
$$

En intégrant :

$$
\begin{cases}
dv_x = 0 \\
dv_y = -g\,dt
\end{cases}
\Leftrightarrow
\begin{cases}
v_x = v_x(t=0) \\
v_y = -gt + v_y(t=0)
\end{cases}
$$

Or $v_x(t=0) = V_0\cos\theta$ et $v_y(t=0) = V_0\sin\theta$, ce qui amène :

$$
\begin{cases}
v_x = V_0\cos\theta \\
v_y = -gt + V_0\sin\theta
\end{cases}
$$

En intégrant encore une fois :

$$
\begin{cases}
x(t) = V_0\cos\theta \cdot t + x(t=0) \\
y(t) = -\dfrac{1}{2}gt^2 + V_0\sin\theta \cdot t + y(t=0)
\end{cases}
$$

Généralement $x(t=0) = 0$, mais $y(t=0)$ n'est pas forcément nul (comme, par
exemple, un lancer au basket…). Dans notre exemple, les deux sont nuls à
$t = 0$, donc :

$$
\begin{cases}
x(t) = V_0\cos\theta \cdot t \\
y(t) = -\dfrac{1}{2}gt^2 + V_0\sin\theta \cdot t
\end{cases}
$$

Dans les faits, on cherchera à déterminer le **temps de vol**, le **point de
chute** (son abscisse $x(t)$), ou la vitesse initiale en connaissant au moins
l'un de ces paramètres.

**Comment retrouver l'équation de trajectoire $y(x)$ à partir des équations
horaires ?** On remarque que $V_0 = \dfrac{x(t)}{\cos\theta \cdot t}$ et
$t^2 = \dfrac{x(t)^2}{V_0^2\cos^2\theta}$. En remplaçant dans l'expression de
$y(t)$, on a :

$$
y(t) = -\frac{1}{2}g\frac{x(t)^2}{V_0^2\cos^2\theta} + \frac{x(t)}{\cos\theta \cdot t}\sin\theta \cdot t
\Leftrightarrow
y(x) = -\frac{1}{2}g\frac{x^2}{V_0^2\cos^2\theta} + x\tan\theta
$$

C'est l'équation de trajectoire.
::::
:::::

:::::{prf:example} Avec frottements de l'air
:label: ex-balistique-avec-frottements
**Situation** : on considère un corps de masse $m$ assimilé à un point
matériel $M$. À $t = 0$, on lance un objet de masse $m$ avec une vitesse
$V_0$ faisant un angle $\theta$ avec l'axe $Ox$. On considère les frottements
de l'air tels que $\overrightarrow{f} = -\alpha\overrightarrow{v}$. Le
référentiel d'étude est le référentiel terrestre supposé galiléen.

:::{figure} /media/ch4-balistique-avec-frottements.png
:label: fig-balistique-avec-frottements
:align: center
:width: 35%

Trajectoire balistique avec frottements de l'air : le frottement
$\overrightarrow{f}$ s'oppose à la vitesse $\overrightarrow{V_0}$.
:::

**Question** : déterminer les équations horaires $x(t)$ et $y(t)$ du point
$M$.

::::{dropdown} Corrigé
**Bilan des forces** : le poids $\overrightarrow{P} = m\overrightarrow{g}$ et
la force de frottement $\overrightarrow{f} = -\alpha\overrightarrow{v}$.

Le PFD nous donne : $\overrightarrow{P} = m\overrightarrow{a}(M)_{/R}$. Dans
la base $(O, \overrightarrow{u_x}, \overrightarrow{u_y})$ :
$\overrightarrow{P} = -mg\overrightarrow{u_y}$ et
$\overrightarrow{f} = -\alpha\left( v_x\overrightarrow{u_x} + v_y\overrightarrow{u_y} \right)$.
Alors on a :

$$
-mg\overrightarrow{u_y} - \alpha v_x\overrightarrow{u_x} - \alpha v_y\overrightarrow{u_y}
= ma_x\overrightarrow{u_x} + ma_y\overrightarrow{u_y}
$$

Soit les deux équations :

$$
\begin{cases}
a_x = -\dfrac{\alpha}{m}v_x \\[1ex]
a_y = -g - \dfrac{\alpha}{m}v_y
\end{cases}
$$

On obtient deux équations différentielles du premier ordre en vitesse. Leur
résolution, comme montré pour la chute libre, conduit à :

$$
\begin{cases}
v_x(t) = Ke^{-\alpha t/m} \\
v_y(t) = -\dfrac{mg}{\alpha} + K_1 e^{-\alpha t/m}
\end{cases}
$$

Or $v_x(t=0) = V_0\cos\theta = K$ et
$v_y(t=0) = V_0\sin\theta = -\dfrac{mg}{\alpha} + K_1$, soit
$K_1 = V_0\sin\theta + \dfrac{mg}{\alpha}$. On a donc :

$$
\begin{cases}
v_x(t) = V_0\cos\theta\, e^{-\alpha t/m} \\
v_y(t) = -\dfrac{mg}{\alpha} + \left( V_0\sin\theta + \dfrac{mg}{\alpha} \right)e^{-\alpha t/m}
\end{cases}
$$

En intégrant encore une fois (avec $x(t=0) = 0$ et $y(t=0) = 0$ dans notre
exemple) :

$$
\begin{cases}
x(t) = -\dfrac{m}{\alpha}V_0\cos\theta\left( e^{-\alpha t/m} - 1 \right) \\[1ex]
y(t) = -\dfrac{mg}{\alpha}t - \dfrac{m}{\alpha}\left( V_0\sin\theta + \dfrac{mg}{\alpha} \right)\left( e^{-\alpha t/m} - 1 \right)
\end{cases}
$$
::::
:::::

## Bilan du chapitre

Dans ce chapitre, nous avons vu comment résoudre des problèmes de mouvements
rectilignes, de chute libre et de balistique à l'aide de la seconde loi de
Newton. Nous avons regardé la méthodologie à appliquer à travers des exemples
et des exercices pour chaque cas : la méthodologie est bien sûr à apprendre
et à maîtriser.

Quitte à se répéter, il y a peu de choses nouvelles dans la dynamique : les
projections, le bilan des forces et la cinématique ont été vus dans les
chapitres précédents du cours. Ils interviennent juste tous ensemble en
dynamique. Bien entendu, il faut alors bien maîtriser tous les outils
précédemment abordés depuis le début du cours.

La seule nouveauté est l'équation différentielle du premier ordre. Il faut
bien apprendre à la résoudre afin de déterminer les équations horaires du
mouvement dans les cas où elle intervient.
