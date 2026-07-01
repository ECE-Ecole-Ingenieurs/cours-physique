---
title: De la statique du point matériel
authors:
  - coralie-thieulin
keywords:
  - statique
  - équilibre
  - bilan des forces
  - frottement solide
abstract: |
  Avant de nous lancer dans la dynamique du point matériel, nous allons
  regarder ce qu'il se passe lorsque le point matériel est immobile. La
  statique du point consiste à reconnaître les forces qui s'appliquent sur un
  point matériel à l'équilibre et à en déduire des propriétés (forces inconnues,
  coefficient de frottement…) en appliquant deux lois.

  Nous détaillons une méthodologie en six étapes, applicable à tout problème
  d'équilibre, puis nous l'illustrons sur un exemple complet.
---

## Introduction

En statique du point, l'objet matériel est un point immobile où se trouve
concentrée toute la masse de l'objet. On considère, dans le cas de plusieurs
points, que ceux-ci interagissent par l'intermédiaire de liaisons supposées
rigides dont les masses seront considérées comme négligeables, ou bien via des
forces à distance.

Nous avons vu dans le chapitre précédent l'ensemble des
{term}`forces usuelles <force>` à distance ou de contact qui sont rencontrées
le plus souvent dans un problème de mécanique. La statique du point consiste à
reconnaître ces forces (à faire un bilan des forces appliquées sur un point
matériel) et à en déduire des propriétés (forces inconnues, coefficient de
frottement…) en appliquant deux lois.

## Les deux lois de la statique du point

:::{prf:axiom} Première loi de la statique
:label: statique-loi-1
La somme des forces qui s'exercent sur un point matériel du système est
nulle :

$$
\sum \overrightarrow{F} = \overrightarrow{0}
$$
:::

Obligatoirement, s'il n'y a pas de mouvement, les forces appliquées sur un
point matériel se compensent **vectoriellement**.

:::{prf:axiom} Deuxième loi de la statique
:label: statique-loi-2
Lorsqu'une interaction existe entre deux points matériels, la force exercée
par le premier sur le second est à chaque instant égale et opposée à la force
exercée par le second sur le premier. C'est en fait directement la
[troisième loi de Newton](#principe-action-reaction) (principe
d'action-réaction).

Autrement dit, si on note $\overrightarrow{F_{1/2}}$ la force qu'exerce un
point $M_1$ sur un point $M_2$, et $\overrightarrow{F_{2/1}}$ la force
qu'exerce le point $M_2$ sur le point $M_1$, alors :

$$
\overrightarrow{F_{1/2}} = -\overrightarrow{F_{2/1}}
$$
:::

## Méthodologie pour étudier un système en équilibre

:::{prf:algorithm} Résoudre un problème de statique
:label: algo-statique
1. Définir le référentiel et le système.
2. Faire le bilan des forces qui s'exercent sur le(s) point(s) matériel(s).
3. Faire un dessin de ces forces et des points afin de bien identifier sens et
   direction des forces.
4. Choisir un repère de base orthonormée **directe** (s'il n'est pas donné ni
   imposé).
5. Projeter toutes les forces appliquées aux points dans ce repère afin de
   déterminer toutes les composantes des forces sur chacun des axes composant
   le repère.
6. Utiliser les deux lois de la statique du point, qui donneront les
   conditions d'équilibre vectoriellement, puis les écrire en composantes
   (c'est-à-dire sur chacun des axes).
:::

Ces six étapes permettent de déterminer les expressions de forces et donc de
répondre à toutes les questions d'un problème de statique.

## Appliquons les lois de la statique

À ce point du cours, la statique du point matériel est essentiellement
applicative. Elle sert à travailler sur les forces et à appliquer ce que l'on
a appris sur les vecteurs, à la fois sur les opérations vectorielles et sur
les projections de vecteurs dans les repères.

:::{note}
Un lecteur attentif aura remarqué que les deux lois de la statique sont les
lois de Newton pour des objets immobiles.

Les lois de Newton impliquent que pour un objet en mouvement à vitesse
constante, la somme des forces est nulle (**comme si l'objet était
immobile**). En conséquence, pour un tel mouvement, la résolution du problème
se fait par l'intermédiaire des lois de la statique si l'on connaît les
forces qui s'appliquent.
:::

:::::{prf:example} Le wagon de montagne russe
:label: ex-wagon-montagne-russe
Un wagon de masse $m_W$ remonte la rampe de lancée (vers la droite) d'une
montagne russe à vitesse constante grâce à une force de traction notée
$\overrightarrow{F_T}$, avant d'être lancé dans la première pente. La pente
fait un angle $\theta$ avec l'horizontale.

Appliquer la méthode décrite ci-dessus, avec le repère le plus adapté à la
résolution du problème, pour en déduire l'expression de la force de
frottement solide en fonction des autres paramètres. Calculer la valeur
numérique pour le cas où $\theta = 60°$, $F_T = 1{,}5\ \mathrm{kN}$ et
$m_W = 150\ \mathrm{kg}$.

::::{dropdown} Corrigé
**Étape 1 — Bilan des forces**

Les forces extérieures qui s'exercent sur le wagon sont :

- le poids, noté $\overrightarrow{P}$ avec $P = mg$, vertical, dirigé vers le
  sol ;
- la réaction normale du support (les rails), notée
  $\overrightarrow{R_N}$, perpendiculaire à la pente, dirigée vers le haut ;
- la force de frottement solide, notée $\overrightarrow{F_S}$, parallèle à
  la pente, vers l'aval ;
- la force de traction, notée $\overrightarrow{F_T}$, parallèle à la pente,
  vers l'amont.

**Étape 2 — Schéma du problème et représentation des forces**

% TODO(Coralie): ajouter le schéma du wagon sur la pente inclinée d'angle
% theta, avec les quatre forces P, R_N, F_S et F_T représentées, ainsi que la
% base (u_x, u_y). Exercice laissé aux étudiants — ne pas leur donner le
% dessin tout fait.

**Étape 3 — Repère associé**

On choisit un repère cartésien avec pour base
$\left( \overrightarrow{u_x}, \overrightarrow{u_y} \right)$, avec
$\overrightarrow{u_x}$ parallèle à la pente et $\overrightarrow{u_y}$
perpendiculaire, de sens direct.

**Étape 4 — Projection des forces sur la base du repère**

$$
\begin{align}
\overrightarrow{P} &= -mg\sin\theta\,\overrightarrow{u_x} - mg\cos\theta\,\overrightarrow{u_y} \\
\overrightarrow{R_N} &= R_N\,\overrightarrow{u_y} \\
\overrightarrow{F_S} &= -F_S\,\overrightarrow{u_x} \\
\overrightarrow{F_T} &= F_T\,\overrightarrow{u_x}
\end{align}
$$

**Étape 5 — Lois de la statique, décomposition par axe et résolution**

On réalise un système de deux équations en décomposant la première loi de
Newton sur les deux axes :
$\overrightarrow{F} = \overrightarrow{0} \Leftrightarrow \overrightarrow{v}(M)_{/R} = \overrightarrow{cte}$.

Ici, $\overrightarrow{v}(M)_{/R} = \overrightarrow{cte}$, donc on peut
appliquer $\overrightarrow{F} = \overrightarrow{0}$, ce qui donne :

$$
\begin{cases}
-mg\sin\theta - F_S + F_T = 0 \\
-mg\cos\theta + R_N = 0
\end{cases}
$$

En plus, on sait que $F_S = fR_N$, avec $f$ le coefficient de frottement
solide. On résout donc le système :

$$
\begin{cases}
-mg\sin\theta + F_T = F_S \\
mg\cos\theta = R_N
\end{cases}
$$

On a donc également $\dfrac{F_S}{R_N} = f$, d'où :

$$
f = \frac{-mg\sin\theta + F_T}{mg\cos\theta}
$$

**Application numérique** : $f = 2 - \sqrt{3} \approx 0{,}27$.
::::
:::::
