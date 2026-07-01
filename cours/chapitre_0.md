---
title: Principes fondamentaux
authors:
  - name: Coralie Thieulin
    affiliation: Enseignante physique, ECE
abstract: |
  Dans ce chapitre, nous allons poser les relations fondamentales sur lesquelles
  se construira la mécanique.

  Les lois sont données sous forme vectorielle. Ceci suppose un espace Euclidien
  (espace de dimension finie, muni du produit scalaire) et isotrope, c'est-à-dire
  qui a les mêmes propriétés dans tous les sens.
---

## Introduction

Dans un cours sur la mécanique du point matériel, il est naturel de commencer
par se poser la question suivante : _qu'est-ce que la mécanique du point
matériel_ ?

La mécanique du point est la base de la **mécanique classique**, aussi appelée
**mécanique newtonienne** car on la doit au physicien **_Isaac Newton_**. C'est
la théorie physique qui traite du mouvement d'objets qui se déplacent à des
vitesses faibles par rapport à la vitesse de la lumière ($c = 3{,}0 \times 10^{8}\ \mathrm{m \cdot s^{-1}}$). Dans le cas de vitesses importantes par rapport à la vitesse de la
lumière, on doit utiliser la **mécanique relativiste**. De plus, la taille des
objets considérés doit être petite par rapport à l'échelle du problème envisagé
pour négliger les mouvements internes de l'objet. Par exemple, la mécanique du
point permet de déterminer le mouvement des planètes du système solaire, la
distance entre planètes étant grande par rapport à la taille de chacune des
planètes. Ainsi, seuls les mouvements d'ensembles peuvent être considérés et des
objets aussi volumineux dans la réalité que les planètes peuvent être assimilés
à des points. La taille des objets doit être dans le même temps grande devant
les dimensions atomiques afin de pouvoir négliger les mouvements des atomes
constituants la matière. En effet, il a été montré il y a un siècle que les
notions de mécanique classique doivent être remplacées par celles de mécanique
quantique dans ce cas.

La mécanique du point n'est pas la seule composante de la mécanique newtonienne.
La mécanique du solide indéformable fait, elle aussi, partie intégrante de la
mécanique classique. Elle a été développée à partir de la mécanique du point
pour tenir compte des mouvements internes des objets solides en plus de leur
mouvement d'ensemble, les mouvements internes étant les mouvements de rotation.
L'exemple le plus simple et parlant étant le cas d'une balle roulant sur la
terre : elle tourne sur elle-même et en même temps elle avance. La mécanique du
point matériel ne peut rendre compte que du mouvement global, c'est-à-dire de la
translation de la balle sur le sol (=mouvement d'ensemble).

Une grandeur physique dont nous n'avons pas encore parlé mais qui est
primordiale est le temps. En effet, nous savons maintenant que celui-ci n'est
pas absolu mais s'écoule de manière différente suivant la vitesse des mouvements
et la durée du mouvement étudiés. Dans le cadre de la mécanique classique, comme
les vitesses des corps observés sont faibles devant la vitesse de la lumière et
que la durée d'observation des mouvements est courte, nous pourrons toujours
considérer le temps comme absolu, c'est-à-dire s'écoulant de la même manière en
tous points de l'espace.

:::{note}

Dans ce cours, nous nous placerons dans un cadre où les effets relativistes et
quantiques peuvent être négligés. Cela revient notamment à supposer que :

```{math}
:enumerated: false
v_{\text{objet}} \ll c
```

Nous supposerons également que l’échelle caractéristique du problème est très
grande devant les dimensions atomiques :

```{math}
:enumerated: false
\text{dimension atomique} \ll \text{taille de l’objet} \ll \text{échelle du problème}
```

:::

## La révolution Newtonienne

Si l'histoire de la mécanique débute réellement avec Galilée au XVIIe siècle,
cette science prend ses racines dans des savoirs datant de l'Antiquité notamment
avec Aristote et Archimède.

En effet, aux origines, la mécanique (qui ne porte pas encore ce nom) regroupe
un ensemble de réflexions d'ordre philosophique ou religieux dont l'objectif est
l'étude du mouvement des astres. À cette époque, le ciel et les astres sont
considérés comme une grosse machine.

C'est Aristote (384-322 av. J.-C.) qui pose les bases de la mécanique. Pour lui,
tous les corps de l'Univers tirent leur mouvement d'un moteur, les mouvements
sont ensuite transmis par contact. À cela s'ajoute l'idée que ces corps se
meuvent pour atteindre le lieu propre qui leur est destiné, où ils trouvent
l'immobilité.

Les contributions d'Archimède (287-212 av. J.-C.) sont également fondamentales. En
particulier, ses réflexions sur l'étude de l'équilibre des corps seront reprises
ensuite par Galilée.

Bien plus tard, Galilée va poser les fondements de la mécanique en tant que
science. On lui doit notamment la loi de la chute des corps. Il montre que deux
objets de masses différentes atteignent le sol en même temps lorsqu'ils sont
lâchés du haut d'une tour. Il est également à l'origine du principe de l'inertie
(un corps en mouvement sur une surface plane garde une vitesse et une direction
constante si on néglige la résistance de l'air et les frottements). Enfin, on
lui doit la loi de composition des mouvements.

Finalement, la théorie de la mécanique du point matériel, telle qu'on la connaît
aujourd'hui, est développée par Sir Isaac Newton en 1686 dans l'ouvrage
_Philosophiae naturalis principia mathematica_, ouvrage scientifique en trois
tomes. Dans le premier tome, Newton expose les 3 lois du mouvement universel
(qui, à l'origine de sa réflexion, étaient au nombre de 5). Il y clarifie des
notions fondamentales qui n'étaient pas claires auparavant sur les forces et il
définit en termes scientifiques la notion de _masse_, c'est-à-dire la quantité
de matière que possède un corps indépendamment de son volume. La masse d'un
corps réel peut varier au cours du temps pour de nombreuses raisons. La
mécanique de Newton ne considère pas ce cas. Le modèle choisi implique que la
masse du corps étudié est constante pendant l'étude de son mouvement : 

$$
m = cte
$$

C'est la première restriction importante dans la théorie de la mécanique
newtonienne.

Citons les trois lois du mouvement telles que Newton les a exprimées en 1686
(bien que traduites du latin) :

**Première loi** : Tout corps persévère dans l'état de repos ou de mouvement
uniforme en ligne droite dans lequel il se trouve, à moins que quelque force
n'agisse sur lui, et ne le contraigne à changer d'état.

**Deuxième loi** : L'altération du mouvement est proportionnelle à la force qui
lui est imprimée ; et cette altération se fait en ligne droite dans la direction
de la force.

**Troisième loi** : Pour chaque action, il existe une réaction égale et opposée.
L'action est toujours égale à la réaction ; c'est-à-dire que les actions de deux
corps l'un sur l'autre sont toujours égales, et dans des directions contraires.

La théorie décrite par Newton s'inspire des nombreux scientifiques qui l'ont
précédé ! Comme il le résume lui-même dans une lettre restée célèbre :

```{epigraph}
Si j'ai vu plus loin, c'est en me plaçant sur les épaules des géants.

-- Isaac Newton, lettre à Robert Hooke, 1676
```

Néanmoins, l'approche de Newton est radicalement différente : ces lois
sont d'une nature différente des lois précédentes. Elles sont des hypothèses sur
la réalité physique des relations entre matière (masse), forces et mouvements.

Ces lois du mouvement ont dicté la physique jusqu'au début du vingtième siècle
et l'émergence de la théorie de la relativité et de la théorie de la mécanique
quantique. Toutefois, ces lois restent entièrement fondamentales et utiles à
l'échelle humaine pour comprendre les mouvements, étudier et concevoir des
systèmes de notre environnement.

Dans ces lois du mouvement, Newton indique déjà que la notion de direction et de
sens des grandeurs physiques est aussi importante que leur intensité.
Mathématiquement, cela fait intervenir un formalisme géométrique et la notion de
vecteurs.

## Les principes fondamentaux de la mécanique du point matériel

### Qu'est-ce qu'un point matériel ?

Nous en parlons depuis le début de ce chapitre mais la notion de point matériel
n'a pas encore été définie. Un corps, un objet réel possède un volume ou une
surface. C'est un ensemble fermé de points qui peuvent posséder chacun une masse
particulière dont la somme donne la masse totale du corps.

Dans notre espace à trois dimensions, un point peut être défini grâce à
uniquement trois coordonnées d'espace (correspondant aux trois directions de
l'espace). **Considérer un corps quelconque comme un point matériel comme dans
la théorie de la mécanique newtonienne correspond à faire abstraction de sa
forme et à attribuer la masse totale du corps à un seul point de l'espace**.
Généralement, ce point correspond au centre de masse (barycentre) du corps réel,
mais ce n'est pas une obligation. La motivation vient du fait qu'en mécanique du point,
seuls les mouvements d'ensemble peuvent être caractérisés : l'étude de la
direction et du sens du mouvement d'un seul point suffit (mais celui-ci doit avoir
la masse totale du corps réel).

### Le principe fondamental de la dynamique

Le principe fondamental de la dynamique est basé sur la grandeur appelée quantité de
mouvement. C'est une grandeur essentielle dans l'approche des mouvements dont la
définition et la compréhension permettent de clarifier bien des choses.

(qte-mouvement)=
La quantité de mouvement est le produit de la masse (scalaire) et de la vitesse
(qui est vectorielle). **La quantité de mouvement est donc un vecteur**. Elle
est usuellement notée : $\overrightarrow{p}$.

Soit $M$ un point matériel de masse $m$ et de vitesse $\overrightarrow{v}(M)$.
Sa quantité de mouvement est alors donnée par :

$$
\overrightarrow{p}(M) = m\overrightarrow{v}(M)
$$

La quantité de mouvement est donc une grandeur physique qui augmente avec la
vitesse d'un corps mais aussi avec la masse. La définition que nous venons de
donner ci-dessus de la quantité de mouvement permet d'énoncer le principe
fondamental de la dynamique :

````{prf:axiom} Principe fondamental de la dynamique
:label: principe-fondamental-dynamique

Dans un référentiel galiléen, la résultante des forces extérieures appliquées
à un point matériel est égale à la dérivée temporelle de sa quantité de mouvement :

```{math}
\sum \overrightarrow{F}_{\text{ext}} = \frac{d\overrightarrow{p}}{dt}
```
````

### Le principe d'action-réaction

Quand deux corps interagissent l'un avec l'autre, la force exercée par le
premier corps sur le second est égale en intensité, de même direction et opposée
en sens à la force produite par le second corps sur le premier.

Ce principe fondamental est directement la troisième loi de Newton telle
qu'énoncée en 1686. Ce principe (et donc cette loi de Newton) concerne
uniquement les forces et n'est pas relié à d'autres grandeurs, contrairement aux
deux autres lois.

:::{prf:axiom} Principe d'action-réaction
:label: principe-action-reaction

Soit deux points matériels interagissant l'un sur l'autre, on a :

$$
{\overrightarrow{F}}_{1/2} = - {\overrightarrow{F}}_{2/1}
$$

ou, en termes de normes :

$$
\left\|
{\overrightarrow{F}}_{1/2} \right\| = \left\| {\overrightarrow{F}}_{2/1}
\right\|
$$
:::

:::{prf:example} LE SYSTEME ISOLE
:label: systeme-isole

Considérons deux points matériels (notés 1 et 2) isolés de l'extérieur. Cela
veut dire qu'aucune force extérieure ne s'applique et ne peut s'appliquer sur le
système. Les deux points réunis définissent un système fermé, et seules les
forces d'interactions entre les deux points sont mises en jeu dans le système.

D'après le [principe d'action-réaction](#principe-action-reaction), nous avons alors :

${\overrightarrow{F}}_{1/2} = - {\overrightarrow{F}}_{2/1}$.

C'est-à-dire que ${\overrightarrow{F}}_{1/2} + {\overrightarrow{F}}_{2/1} =
\overrightarrow{0}$

D'après le [principe fondamental de la dynamique](#principe-fondamental-dynamique), nous pouvons écrire pour chacun
des points :

${\overrightarrow{F}}_{1/2} = \frac{d\overrightarrow{p_{2}}}{dt}$ et
${\overrightarrow{F}}_{2/1} = \frac{d\overrightarrow{p_{1}}}{dt}$.

Additionnons ces deux équations :

${\overrightarrow{F}}_{1/2} + {\overrightarrow{F}}_{2/1} =
\frac{d\overrightarrow{p_{2}}}{dt} + \frac{d\overrightarrow{p_{1}}}{dt} =
\frac{d(\overrightarrow{p_{2}} + \overrightarrow{p_{1}})}{dt}$

Or la quantité de mouvement totale du système est : $\overrightarrow{p} =
\overrightarrow{p_{2}} + \overrightarrow{p_{1}}$.

On a donc : ${\overrightarrow{F}}_{1/2} + {\overrightarrow{F}}_{2/1} =
\frac{d\overrightarrow{p}}{dt}$.

Comme ${\overrightarrow{F}}_{1/2} + {\overrightarrow{F}}_{2/1} =
\overrightarrow{0}$, on obtient alors que $\frac{d\overrightarrow{p}}{dt} =
\overrightarrow{0}.$

**Conclusion** : dans un système isolé de deux points, il n'y a pas de variation de
quantité de mouvement. Elle est conservée au cours du temps :
$\overrightarrow{p} = \overrightarrow{cste}$.
:::

Il est assez facile de généraliser ce problème à un système fermé de N points
matériels. Ainsi en suivant le même raisonnement et en sommant les interactions
deux à deux dans le système, on obtient le théorème de la conservation de la
quantité de mouvement :

```{prf:theorem}
:label: conservation-quantite-mouvement
**La quantité de mouvement d'un système isolé est conservée au cours du temps**
```

## Conséquence de l'invariance de la masse : Les 3 lois de Newton

Les deux principes fondamentaux que nous venons d'expliciter peuvent être
réécrits dans le cadre de la mécanique du point en considérant la masse $m$
**constante**

D'après le [principe fondamental de la dynamique](#principe-fondamental-dynamique) et la définition de la quantité
de mouvement, puisque la masse est constante et est scalaire, il vient de suite
que :

```{prf:corollary} Deuxième loi de Newton
:label: corollaire-deuxieme-loi

**Une force est égale au produit de la masse et de la dérivée par rapport au
temps de la vitesse du point matériel.**
```

C'est la **seconde loi de Newton**. Le terme de dérivée par rapport au temps de la
vitesse représente l'altération du mouvement dont parlait Newton en 1686. Nous
verrons par la suite que ce terme est égal à l'accélération du point.

La **première loi de Newton** se déduit immédiatement de cette seconde loi. En
effet, si les forces se compensent (la force totale appliquée est égale à zéro),
on a la dérivée de la vitesse par rapport au temps qui est nulle. Donc la
vitesse est constante vectoriellement (elle garde au cours du temps même norme,
même direction et même sens). C'est la première loi de Newton.

Nous avons vu que le principe d'action-réaction est directement la troisième loi
de Newton.

Ceci nous permet d'énoncer les lois de Newton dans un formalisme mathématique
moderne.

:::{prf:axiom} Synthèse — Les trois lois de Newton
:label: lois-newton

**Première loi** (principe d'inertie) :

$$
\overrightarrow{F} = \overrightarrow{0} \Leftrightarrow
\overrightarrow{\ v} = \overrightarrow{cste}
$$

**Deuxième loi** (principe fondamental de la dynamique, PFD) :

$$
\overrightarrow{F} = m\frac{d\overrightarrow{\ v}}{dt}
$$

**Troisième loi** (principe d'action-réaction) :

$$
{\overrightarrow{F}}_{1/2} = - {\overrightarrow{F}}_{2/1}
\qquad \text{et} \qquad
\left\| {\overrightarrow{F}}_{1/2} \right\| = \left\|
{\overrightarrow{F}}_{2/1} \right\|
$$
:::

:::{note}

Nous avons vu que la première loi se déduit immédiatement de la seconde loi de
Newton. Elle peut apparaître superflue. Néanmoins, elle est gardée séparée de la
seconde pour des raisons historiques : Newton les avait différenciées car la
première loi peut être attribuée à Galilée.

Même si cette loi apparaît évidente et simple de nos jours, elle est loin dans
les faits d'être triviale. Pendant longtemps, on pensait que s'il n'y avait pas
de force appliquée sur un corps en mouvement celui-ci s'arrêtait dans tous les
cas. C'est une idée fausse et une observation fausse que nous faisons dans la
vie courante. En effet, dans la vie de tous les jours tout corps s'arrête
effectivement si le mouvement n'est pas entretenu. La cause en est les
frottements qui sont inévitables ! En d'autres termes, il est extrêmement
difficile sur Terre d'observer des systèmes réellement isolés de l'environnement
extérieur.

La seconde loi de Newton (anciennement loi fondamentale de la dynamique
générale) est, dans la physique actuelle, une forme restrictive du principe
fondamental de la dynamique puisqu'elle n'est valable que pour des masses
constantes au cours du temps. Néanmoins, dans le cadre d'un cours de mécanique
classique, utiliser le principe fondamental de la dynamique ou la seconde loi de
Newton est parfaitement équivalent.
:::

## Conditions d'application du PFD

### Référentiels, repères et systèmes de coordonnées

Avant tout, il est essentiel de préciser la signification de ces notions.

:::{prf:definition} Référentiel
:label: def-referentiel

Un **référentiel** (=point de vue d'un observateur) est la référence que l'on
utilise pour décrire un mouvement. Cette référence est constituée de l'ensemble
des points qui sont immobiles pour l'observateur.

Cela peut être la salle de cours, une voiture, un train, un avion, la Lune...

Notation : $R$
:::

:::{prf:definition} Repère
:label: def-repere

Pour repérer le mouvement d'un corps dans un référentiel (=point de vue d'un
observateur immobile), il faut associer au référentiel un repère d'espace dont
l'origine est un point fixe du référentiel et dont la base est aussi fixe.

Les axes du repère ne sont pas forcément orthogonaux (c'est plus simple s'ils le
sont !), mais ils ne doivent en aucun cas être coplanaires. Pour un même
référentiel, il y a une infinité de repères différents.

Notation : $R(0,\overrightarrow{u},\overrightarrow{v},\overrightarrow{w})$

Remarque : Dans l'absolu, il faudrait ajouter une base de temps au référentiel.
Mais, comme en mécanique newtonienne on considère le temps comme absolu, il
n'est pas nécessaire de l'indiquer.
:::

::::{prf:definition} Systèmes de coordonnées
:label: def-coordonnees

Afin de déterminer les composantes du mouvement du corps dans le référentiel et
de quantifier ce mouvement, le plus simple consiste à prendre un système d'axes
orthonormés fixes dans le référentiel. Toutefois de nombreux problèmes sont plus
évidents à résoudre en utilisant un système de coordonnées de résolution du
problème autre que celui associé au référentiel (coordonnées cylindriques,
sphériques...).

Dans tous les cas, il faudra définir trois vecteurs unitaires constituant la
base de résolution du problème.

:::{attention}
Si la base de résolution est différente de celle liée au référentiel,
ces vecteurs unitaires ne seront pas fixes dans le référentiel : leurs sens et
directions vont suivre le mouvement.
:::
::::

(referentiel-galileen)=
### Référentiel Inertiel (ou Galiléen)

C'est le référentiel utilisé en mécanique du point (en mécanique classique). En
effet, la première et la seconde loi de Newton ne sont valables que lorsqu'elles
sont appliquées dans un **référentiel non-accéléré dit référentiel inertiel ou
référentiel Galiléen**. On doit la définition de ce référentiel à Galileo
Galilei dit Galilée.

**Mais qu'est-ce qu'un référentiel non-accéléré ?**

Un référentiel inertiel peut être défini comme étant un référentiel dans lequel
la première loi de Newton est vérifiée. C'est-à-dire qu'un corps est soit au
repos soit en mouvement à vitesse constante si aucune force ne s'applique sur
lui. Il faut donc que le corps soit isolé dans le référentiel Galiléen. Il
faudrait alors vérifier à chaque fois dans ce référentiel que la vitesse est
bien constante (et donc que la quantité de mouvement est bien conservée). On a
vu que ce n'est pas évident à réaliser sur Terre, principalement à cause des
frottements mais aussi des forces à distance qui s'appliquent inévitablement
comme la force d'attraction de la gravitation !

Donc restons pragmatiques : un référentiel inertiel ou galiléen est un
référentiel où tout se passe bien. Si vous posez un objet à l'équilibre, il ne
doit rien lui arriver (il ne bouge pas).

Ainsi pour nos problèmes locaux et pour des temps bien inférieurs à la journée,
nous pourrons considérer la Terre comme un référentiel Galiléen (on ne ressent
pas la rotation de la Terre et tout se passe bien !).

Vous verrez donc souvent dans les exercices : le référentiel d'étude est le
référentiel terrestre considéré comme Galiléen ou pseudo-Galiléen.

Si le problème met en jeu des mouvements ou des temps à plus grande échelle,
alors le référentiel inertiel de référence (référentiel absolu) doit avoir pour
origine le centre de la Terre et des axes liés aux étoiles.

Si l'on regarde le mouvement des planètes du système solaire, l'origine du
référentiel inertiel de référence est le centre de masse du système solaire
(quasiment le centre du Soleil à quelques centimètres près !) et des axes liés
aux étoiles : ce référentiel a été défini par Nicolas Copernic dès 1517. Il est
généralement appelé le référentiel de Copernic. Le référentiel héliocentrique a
lui pour origine le centre du Soleil.

### Ensemble des référentiels Galiléens

Si l'on connaît un seul référentiel galiléen R (le référentiel de Copernic par
exemple ou le référentiel terrestre), on peut en définir une infinité.

En effet, tout référentiel R' qui effectue une translation à vitesse constante
par rapport à R est lui-même un référentiel Galiléen.

:::{note}
Un référentiel $R'$ est en translation par rapport à un référentiel $R$
si tous les points de $R'$ se déplacent à la même vitesse dans $R$.

Dans une translation d'un référentiel $R'$ par rapport à $R$, uniquement le point
origine du repère associé à $R'$ est animé d'un mouvement entre les instants $t$ et
t+dt. Les vecteurs de la base associée à $R'$ sont fixes (ils n'ont pas de
mouvement).

Il existe différents types de translations :

- Translation rectiligne (_ex : voiture qui se déplace en ligne droite à vitesse
  constante_)
- Translation circulaire (_ex : la grande roue_)
- Translation curviligne

:::

::::{prf:example}

:::{figure} /media/ch0-img1.png
:label: fig-train-galileen
:align: center
:width: 70%

Passager 1 se déplaçant dans un train en translation rectiligne uniforme par
rapport au référentiel terrestre.
:::

Un passager (noté 1) se déplace à la vitesse $\overrightarrow{v}'$ dans un train
se déplaçant à la vitesse constante $\overrightarrow{v}$ par rapport au sol.

Le train est donc en **translation rectiligne uniforme** par rapport au sol : il
est donc en translation rectiligne uniforme dans le référentiel terrestre
$R(0,\overrightarrow{U_{x}},\overrightarrow{U_{y}})$ considéré comme
pseudo-Galiléen.

On peut définir le train comme le référentiel $R'\left(
0',\overrightarrow{U_{x'}},\overrightarrow{U_{y'}} \right)$ qui est galiléen.
C'est effectivement un ensemble de points fixes pour le passager 1 qui se déplace.
::::

## Bilan du chapitre

Au cours de ce chapitre, nous avons vu qu'il existe deux [principes fondamentaux](#principe-fondamental-dynamique)
qui permettent de résoudre tous les problèmes de la mécanique classique.

Dans le cadre spécifique de la mécanique du {term}`point matériel`, où la **masse est
constante**, ces deux principes peuvent être déclinés par les [trois lois de
Newton](#lois-newton) qui seront les lois fondamentales utilisées dans toute la suite.

Ces lois sont valables pour des référentiels dits galiléens ou inertiels.
