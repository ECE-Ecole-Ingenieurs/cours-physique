---
title: Les forces usuelles
authors:
  - coralie-thieulin
keywords:
  - force
  - gravitation
  - poids
  - force de Coulomb
  - frottement
  - poussée d'Archimède
  - tension
abstract: |
  Dans le chapitre précédent, nous avons posé les trois lois de Newton, dans
  lesquelles la notion de force intervient directement. Ce chapitre en propose
  un inventaire pratique : les forces les plus fréquemment rencontrées dans les
  problèmes de mécanique du point.

  Nous distinguons les forces à distance (gravitation, poids, forces de
  Lorentz) des forces de contact (frottements solide et fluide, poussée
  d'Archimède, tension d'un ressort ou d'un fil), en donnant pour chacune son
  expression et son domaine de validité.
---

## Introduction

Dans le chapitre « [Principes fondamentaux](#lois-newton) », nous avons vu les
relations fondamentales qui permettront d'étudier et de résoudre un problème de
mécanique du point matériel. Ces relations fondamentales sont les trois lois de
Newton. La notion de **force** intervient dans ces trois lois.

Dans ce chapitre, nous allons voir les forces rencontrées le plus fréquemment
dans les problèmes physiques relevant de la mécanique du point.

## La notion de force

:::{prf:definition} Force
:label: def-force
Une **force** est une quantité physique qui modélise l'action exercée sur un
système physique. Ainsi, une force est une action ou un effort qui,
s'appliquant en un point matériel, modifie son comportement. Si le point est
immobile, une force s'appliquant va le mettre en mouvement dans un sens et une
direction donnés. Si le point est déjà en mouvement, une nouvelle force
s'appliquant sur le point va le faire changer de direction, voire de sens.
:::

Toute force est caractérisée par son intensité (norme), par une direction dans
laquelle elle est appliquée et par un sens : les forces sont donc des **notions
vectorielles** (comme notées dans les lois de Newton).

La dimension de toute force est $M \cdot L \cdot T^{-2}$.

Les forces sont exprimées en $\mathrm{N}$ (Newton) ou, dans le système
international, en $\mathrm{kg \cdot m \cdot s^{-2}}$.

Les forces peuvent se scinder en deux familles :

- Les forces à distance
- Les forces de contact

Regardons ces deux familles l'une après l'autre.

## Les forces d'interaction à distance

Ces forces sont des forces d'interaction : elles sont dues à l'action d'un
point matériel sur un autre point matériel, les deux points étant distants
l'un de l'autre (ils ne se touchent pas !). Ces forces sont au nombre de quatre
en physique. Elles possèdent toutes un point commun : leur intensité décroît
lorsque la distance d'interaction augmente. Les quatre types de forces sont :

- La force de gravitation
- Les forces électriques et magnétiques
- Les forces d'interaction faible
- Les forces d'interaction forte

:::{note}
Les deux dernières sortent totalement du cadre de la mécanique du point car
elles interviennent dans la cohésion de la matière au niveau subatomique
(physique des particules). Nous ne les aborderons donc pas.
:::

Nous avons donc deux types de force à distance à regarder, à décrire, et qui
seront rencontrés par la suite : les forces de gravitation et les forces
électriques et magnétiques.

### La force de gravitation

Énoncée par Newton dès 1650 (les lois du mouvement datent de 1686), la force de
gravitation a été une véritable révolution. Elle expliquait pour la première
fois le mouvement des planètes.

:::{prf:definition} Force de gravitation
:label: def-force-gravitation
Deux masses ponctuelles (deux points matériels) s'attirent en raison de leur
masse et de l'inverse du carré de la distance qui les sépare, selon la
direction passant par les deux points :

$$
\overrightarrow{F}_{m_1 \rightarrow m_2} = - \overrightarrow{F}_{m_2 \rightarrow m_1}
= - \frac{G \cdot m_1 \cdot m_2}{\left( M_1M_2 \right)^2} \cdot \frac{\overrightarrow{M_1M_2}}{M_1M_2}
$$

avec $G = 6{,}675 \times 10^{-11}\ \mathrm{N \cdot m^2 \cdot kg^{-2}}$.
:::

:::{figure} /media/ch2-gravitation-masses.png
:label: fig-gravitation-masses
:align: center
:width: 45%

Deux masses ponctuelles $m_1$ et $m_2$ s'attirent mutuellement :
$\overrightarrow{F}_{m_1 \rightarrow m_2} = -\overrightarrow{F}_{m_2 \rightarrow m_1}$.
:::

La force de gravitation est une **force attractive**. Les normes des deux
forces sont égales.

:::{attention}
Si les masses ne peuvent pas être considérées comme ponctuelles, c'est-à-dire
si leur taille n'est pas petite devant la distance qui les sépare, il ne faut
pas appliquer cette loi.
:::

La force de gravitation est une interaction fondamentale. C'est une force
pleine de surprises et encore bien mystérieuse. Encore de nos jours, elle est
source de recherche et de questionnement, car sa portée est infinie : elle
structure la répartition des masses dans l'univers tout entier. Son
comportement aux échelles subatomiques est encore une énigme, mais elle existe
aussi à cette échelle de taille.

Une force commune que nous ressentons tous les jours découle directement de la
force de gravitation : le poids.

#### Le poids

:::{prf:definition} Poids
:label: def-poids
Le **poids**, noté $\overrightarrow{P}$, représente la force de gravitation
exercée par une planète sur des objets dans son entourage proche. C'est le
produit de la masse du point par l'accélération de la pesanteur
$\overrightarrow{g}$ due à la planète :

$$
\overrightarrow{P} = m\overrightarrow{g}
$$
:::

Le poids est donc toujours colinéaire à l'accélération de la pesanteur. Mais
comment exprimer cette dernière ?

Lorsque les masses sont concentrées en des points matériels, l'expression de
l'interaction gravitationnelle est claire. Par contre, pour deux objets
étendus, comme une planète ou une personne, on doit se poser la question de la
position des deux points matériels.

Comme déjà dit dans le chapitre « Principes fondamentaux », en mécanique du
point, les points matériels sont choisis comme étant le centre de masse des
{term}`objets <point matériel>` auquel on alloue la masse totale de l'objet.

Ainsi une planète est modélisée par une sphère parfaite homogène de masse
moyenne et de rayon moyen $R_T$. Dans ce cas, le centre de la sphère est le
centre de masse de la planète.

::::{prf:example} Poids d'un point matériel à la surface de la Terre
:label: ex-poids-terre
La Terre est modélisée par une sphère parfaite homogène de masse moyenne
$m_{\text{Terre}}$ et de rayon moyen $R_T$. Pour un point $M$ de masse $m$, se
trouvant à une altitude $z$ au-dessus de la surface de la Terre, la distance
entre les deux masses (les deux points) est alors la distance du centre de la
Terre jusqu'à l'altitude $z$ au-dessus de sa surface.

**Question** : établir l'expression du poids $\overrightarrow{P}$ du point
$M$, puis celle de l'accélération de la pesanteur terrestre
$\overrightarrow{g}$, dans le cas où $z \ll R_T$.

:::{dropdown} Corrigé
On définit le poids comme étant la force gravitationnelle qu'exerce la Terre
sur le point $M$. On a alors :

$$
\overrightarrow{P} = \overrightarrow{F}_{\text{Terre} \rightarrow M}
= - \frac{G \cdot m_{\text{Terre}} \cdot m}{\left( R_T + z \right)^2} \overrightarrow{u_z}
= m \cdot \frac{-G \cdot m_{\text{Terre}}}{R_T^2 \left( 1 + \dfrac{z}{R_T} \right)^2} \overrightarrow{u_z}
$$

Donc si $\dfrac{z}{R_T} \ll 1$ (très petit), on a
$\left( 1 + \dfrac{z}{R_T} \right) \approx 1$, alors :

$$
\overrightarrow{P} = \overrightarrow{F}_{\text{Terre} \rightarrow M}
= m \cdot \frac{-G \cdot m_{\text{Terre}}}{R_T^2} \overrightarrow{u_z}
$$

On pose $\overrightarrow{g} = \dfrac{-G \cdot m_{\text{Terre}}}{R_T^2}\overrightarrow{u_z}$ :
c'est l'**accélération de la pesanteur** terrestre.
:::
::::

:::{note}
Le vecteur $\overrightarrow{g}$ a la dimension d'une accélération, mais ce
n'en est pas une au sens où ce n'est ni la dérivée d'une vitesse, ni la dérivée
seconde d'une position.
:::

En prenant $m_{\text{Terre}} = 6{,}0 \times 10^{24}\ \mathrm{kg}$ et
$R_T = 6400\ \mathrm{km}$, on obtient la valeur $g = 9{,}81\ \mathrm{m \cdot s^{-2}}$.

L'expression de $\overrightarrow{g}$ est la même quelle que soit la planète,
seules sa masse et son rayon moyen changent.

:::{note}
En toute rigueur, le vecteur $\overrightarrow{u_z}$ est ici le vecteur
$\overrightarrow{u_r}$ des coordonnées sphériques. Toutefois, compte tenu des
échelles mises en jeu, celui-ci est confondu avec l'axe vertical de la base
cartésienne à l'échelle humaine.
:::

Il faut remarquer que $\overrightarrow{g}$ est colinéaire à $\overrightarrow{u_z}$
(considéré maintenant comme l'axe vertical de la base cartésienne) et de sens
opposé. Comme le poids est une force colinéaire à $\overrightarrow{g}$ et de
même sens, **le poids est toujours vertical, dirigé vers le centre de la
Terre**.

### Les forces de Lorentz

Ces forces interviennent lorsque les objets (et donc les points matériels)
sont porteurs de charges électriques.

On distingue les forces électriques (ou coulombiennes), qui s'appliquent
lorsque les particules sont au repos, des forces magnétiques, qui s'ajoutent
lorsque les particules (ou charges) sont en mouvement relatif (l'une par
rapport à l'autre).

#### La force de Coulomb

C'est la force électrique. Son expression ressemble étrangement à celle de la
force gravitationnelle, mais celle-ci peut être attractive ou répulsive
suivant le signe des charges.

:::{prf:definition} Force de Coulomb
:label: def-force-coulomb
$$
\overrightarrow{F}_{q_1 \rightarrow q_2} = - \overrightarrow{F}_{q_2 \rightarrow q_1}
= \frac{K \cdot q_1 \cdot q_2}{r^2} \cdot \frac{\overrightarrow{M_1M_2}}{M_1M_2}
$$

La constante $K$ vaut $K = \dfrac{1}{4\pi\varepsilon_0}$. Dans le vide,
$K \approx 9 \times 10^{9}\ \mathrm{m/F}$ (mètre par Farad). Les charges $q_1$
et $q_2$ sont exprimées en Coulomb ($\mathrm{C}$).
:::

:::{note}
Vous verrez plus en détail dans le cours d'électrostatique comment relier la
constante $\varepsilon_0$ (permittivité du vide) à la perméabilité magnétique
du vide et à la vitesse de la lumière. Dans le cadre du cours de mécanique, la
constante $K$ sera toujours donnée.
:::

Comme il a été fait pour le poids à partir de la force gravitationnelle, il est
commode de définir le **champ électrique** $\overrightarrow{E_1}$ créé par la
charge $q_1$ dans l'expression de la force électrique. En considérant l'action
de la charge $q_1$ sur la charge $q_2$, nous avons :

$$
\overrightarrow{F}_{q_1 \rightarrow q_2} = q_2\overrightarrow{E_1}
\qquad \text{avec} \qquad
\overrightarrow{E_1} = \frac{K \cdot q_1}{r^2} \cdot \frac{\overrightarrow{M_1M_2}}{M_1M_2}
$$

le champ créé par $q_1$.

:::{prf:example} Réciprocité de la force de Coulomb
:label: ex-force-coulomb-reciproque
En déduire la force exercée par la charge $q_2$ sur la charge $q_1$ :
$\overrightarrow{F}_{q_2 \rightarrow q_1}$ ?
:::

#### La force magnétique

:::{attention}
Cette sous-section n'est pas au programme de cette année.
:::

Lorsque les particules sont en mouvement, une force dite magnétique s'ajoute à
la force électrique. Elle se déduit totalement de la force électrique et
s'écrit, pour une charge $q$, comme :

$$
\overrightarrow{F}_M = q\,\overrightarrow{V} \wedge \overrightarrow{B}
$$

avec $\overrightarrow{V}$ la vitesse de la charge et $\overrightarrow{B}$ le
champ magnétique.

La force magnétique est donc toujours perpendiculaire à la vitesse de la
charge.

Donc si la charge $q_2$ est en mouvement, elle subit une force totale, dite
**force de Lorentz**, de :

$$
\overrightarrow{F}_{q_1 \rightarrow q_2} = q_2\left( \overrightarrow{E} + \overrightarrow{V} \wedge \overrightarrow{B} \right)
$$

## Les forces de contact

Il s'agit des forces qui existent lorsque le nombre de degrés de liberté de
l'objet est inférieur à 6. En effet, un objet seul dans l'espace possède 6
degrés de liberté (3 translations et 3 rotations possibles). Lorsque l'objet
est en contact avec un autre objet, il y a perte d'un degré de liberté et gain
d'un degré de contact.

Les forces de contact les plus fréquemment rencontrées sont :

- Les frottements solides
- Les frottements fluides
- Les forces de tension sur un ressort ou un fil de masse négligeable

### Force de frottement solide

Si une masse $m$ est en contact avec un support (par exemple votre stylo sur
votre table), le support exerce aussi sur la masse $m$ une force — c'est la
[troisième loi de Newton](#principe-action-reaction) — appelée **réaction du
support**.

Il est utile et indispensable de décomposer la réaction du support en deux
composantes : une composante normale aux surfaces en contact et une composante
tangentielle (c'est-à-dire dans le plan des surfaces en contact) :

$$
\overrightarrow{R} = \overrightarrow{R_N} + \overrightarrow{R_T}
$$

:::{figure} /media/ch2-reaction-normale-tangentielle.png
:label: fig-reaction-normale-tangentielle
:align: center
:width: 40%

Décomposition de la réaction du support $\overrightarrow{R}$ en une composante
normale $\overrightarrow{R_N}$ et une composante tangentielle
$\overrightarrow{R_T}$.
:::

- Si $R_N = 0$, alors il n'y a pas de contact !
- Si la masse $m$ est sur une surface plane horizontale, alors
  $\overrightarrow{R}$ est verticale. Comme
  $\overrightarrow{R} = \overrightarrow{R_N} + \overrightarrow{R_T}$, alors
  $\overrightarrow{R_T} = \overrightarrow{0}$.
- Si la masse $m$ est **immobile** sur une surface faisant un angle $\alpha$
  avec l'horizontale, $\overrightarrow{R}$ est aussi verticale car elle
  compense le poids. Si elle n'est pas verticale, alors la masse $m$ ne peut
  pas être immobile.

Le vecteur $\overrightarrow{R_T}$ **s'oppose au mouvement du point $M$**.
C'est en fait ce que l'on appelle la force de frottement solide entre la masse
$m$ (point $M$) et le support solide.

:::{note}
La notion de frottement solide est une notion complexe, car elle fait
intervenir les forces au niveau moléculaire (contact au niveau moléculaire).
:::

:::{prf:definition} Loi de Coulomb du frottement solide
:label: def-frottement-solide
$$
\left\| \overrightarrow{R_T} \right\| = f \left\| \overrightarrow{R_N} \right\|
$$

Le coefficient $f$ est le **coefficient de frottement solide**. C'est le
coefficient de frottement statique lorsque l'objet est en équilibre ; il
devient le coefficient de frottement dynamique lorsque l'objet est en
mouvement. La relation ci-dessus reste vraie s'il n'y a pas de mouvement de
glissement.
:::

- Si $R_T = 0$, alors il n'y a pas de frottement, c'est-à-dire que $f = 0$.

### Force de frottement fluide

Cette force résulte de l'interaction entre les atomes ou molécules de la masse
solide avec les atomes ou molécules d'un fluide. Lorsque le mobile se déplace
dans un fluide, cette force dépend de la vitesse relative entre le mobile et
le fluide.

#### À faible vitesse

:::{prf:definition} Frottement fluide à faible vitesse
:label: def-frottement-fluide-faible
La force de frottement qui s'exerce sur un objet se déplaçant à faible vitesse
dans un fluide (écoulement laminaire : les forces de viscosité dominent) est
donnée par :

$$
\overrightarrow{F_f} = -\alpha \overrightarrow{v}
$$

avec $\alpha$ le coefficient de résistance de l'objet dans le liquide. Il
dépend de la forme de l'objet et de la viscosité du fluide.
:::

:::{prf:example} Dimension du coefficient de résistance
:label: ex-dimension-alpha
Déterminer la dimension et l'unité du coefficient de résistance $\alpha$.
:::

#### À forte vitesse

:::{prf:definition} Frottement fluide à forte vitesse
:label: def-frottement-fluide-forte
La force de frottement qui s'exerce sur un objet se déplaçant à forte vitesse
(écoulement turbulent : les effets cinétiques dominent) dans un fluide est
donnée par :

$$
\overrightarrow{F_f} = -\alpha' v\,\overrightarrow{v} = -\alpha' v^2 \overrightarrow{u}
\qquad \text{avec} \qquad
\overrightarrow{u} = \frac{\overrightarrow{v}}{v}
$$

qui est, par définition, un vecteur unitaire.
:::

### La poussée d'Archimède

:::{prf:definition} Poussée d'Archimède
:label: def-poussee-archimede
Tout corps plongé dans un fluide est soumis à une force verticale, dirigée
vers le haut, égale au poids du **fluide déplacé** :

$$
\overrightarrow{\pi_a} = \rho V g\,\overrightarrow{u_z}
$$

avec $\rho$ la masse volumique du fluide, $V$ le volume de fluide déplacé, $g$
l'accélération de la pesanteur et $\overrightarrow{u_z}$ un vecteur unitaire
dirigé vers le haut suivant la verticale.
:::

### Les forces de tension

#### Force de rappel d'un ressort

Soit un ressort de constante de raideur $k$, de masse négligeable, de longueur
à vide $l_0$. On suppose le ressort linéaire.

:::{figure} /media/ch2-ressort-force-rappel.png
:label: fig-ressort-force-rappel
:align: center
:width: 50%

Ressort de longueur $l$ exerçant sur la masse $M$ la force de rappel
$\overrightarrow{F}_{\text{ressort} \rightarrow M}$.
:::

:::{prf:definition} Force de rappel d'un ressort
:label: def-force-ressort
La force de rappel du ressort sur la masse $M$ est donnée par la relation
suivante :

$$
\overrightarrow{F}_{\text{ressort} \rightarrow M} = -k(l - l_0)\overrightarrow{u_x}
$$
:::

Lorsque :

- $l > l_0$ : le ressort est étiré et tire la masse
  ($\overrightarrow{F}_{\text{ressort} \rightarrow M}$ est en sens inverse de
  $\overrightarrow{u_x}$) ;
- $l < l_0$ : le ressort est comprimé et pousse la masse
  ($\overrightarrow{F}_{\text{ressort} \rightarrow M}$ est dans le sens de
  $\overrightarrow{u_x}$).

:::{prf:example} Force de rappel dans différents cas
:label: ex-force-ressort-cas
Exprimer la force de rappel exercée sur la masse $M$ (ou $M_1$ et $M_2$) dans
chacun des six cas suivants.

```{figure} /media/ch2-ressort-cas.png
:label: fig-ressort-cas
:align: center
:width: 90%

Six configurations d'un ressort de longueur naturelle $l_0$ fixé en $O = H$ :
horizontal (1, 2, 3), vertical (4, 5), et couplant deux masses (6).
```
:::

#### Tension d'un fil

Soit un point matériel $M$ de masse $m$, accroché à un fil souple tendu. Le
fil est **idéal** : sa masse est négligeable et sa longueur est fixe (fil
inextensible).

La tension est une force dirigée selon la direction du fil, représentée sur le
schéma ci-dessous.

:::{figure} /media/ch2-tension-fil.png
:label: fig-tension-fil
:align: center
:width: 40%

Point matériel $M$ suspendu à un fil tendu depuis $O$ : le poids
$\overrightarrow{P}$ et la tension $\overrightarrow{T}$ s'appliquent sur $M$.
:::
