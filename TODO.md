# Tâches à réaliser

## TP préparatoire — NumPy et Matplotlib

- [ ] Finaliser un notebook d'introduction à NumPy et Matplotlib à partir des
  supports et exercices déjà disponibles.
- [ ] Ajouter, dans les TP de physique, des rappels numériques courts au moment
  où une notion de NumPy ou de Matplotlib est utilisée pour la première fois.
- [ ] Relier ces rappels aux formations NumPy et Matplotlib existantes, sans
  reproduire intégralement leur contenu.

## Notebook 1 — Systèmes de coordonnées

- [x] Ajouter une partie sur le changement de base et la projection de
  vecteurs.
- [x] Conserver l'introduction, mais retirer les admonitions de type `note`.
- [x] Ajouter une partie sur la projection.
- [x] Dans la partie sur le changement de base, ajouter l'angle $\theta$ sur
  la figure dans le plan.

  **État :** l'angle apparaît désormais dans la visualisation 3D et sur la
  figure plane représentant les bases.
- [x] Dans la partie sur les systèmes de coordonnées, retirer l'image fixe et
  afficher directement les curseurs.

  **État :** la version étudiant affiche directement les curseurs en local.
  La version enseignant conserve une image statique pour le book et masque la
  cellule interactive lors de la publication.

### Amélioration des visualisations

#### Projection du vecteur position

- [x] Limiter les coordonnées proposées par les curseurs à des valeurs
  positives afin de travailler dans le premier octant.
- [x] Remplacer les segments en pointillés représentant les composantes par
  des flèches colorées réalisées avec `quiver`.
- [x] Utiliser, dans les légendes, les mêmes couleurs que celles des flèches
  correspondantes.
- [x] Disposer les flèches de manière à faire apparaître la construction de
  la somme vectorielle :
  $\overrightarrow{OM}
  = x\overrightarrow{e_x}
  + y\overrightarrow{e_y}
  + z\overrightarrow{e_z}$.

#### Représentation plane des bases

- [x] Remplacer la légende par des étiquettes placées directement à
  l'extrémité des vecteurs
  $\overrightarrow{e_x}$, $\overrightarrow{e_y}$,
  $\overrightarrow{e_r}$ et $\overrightarrow{e_\theta}$.
- [x] Retirer la boîte de légende afin d'obtenir une figure plus claire et
  plus autonome.

#### Visualisation 3D

- [x] Représenter en noir la base cartésienne
  $(\overrightarrow{e_x},\overrightarrow{e_y},\overrightarrow{e_z})$ à
  l'origine du repère.
- [x] Représenter au point $M$ la base cylindrique mobile
  $(\overrightarrow{e_r},\overrightarrow{e_\theta},
  \overrightarrow{e_z})$.
- [x] Mettre à jour l'orientation et la position de la base cylindrique
  lorsque le point $M$ se déplace avec les curseurs.

- [x] Ajouter une section « Pour aller plus loin » consacrée aux coordonnées
  sphériques ou à un autre système de coordonnées.
- [ ] Envoyer le notebook aux professeurs lorsqu'il sera terminé.

## Notebook 2 — Cinématique

### Équations horaires et trajectoire

- [ ] **Optionnel — version enseignant :** intégrer dans la page web une
  animation autonome de la trajectoire, sans remplacer le curseur temporel ni
  les contrôles interactifs de la version étudiant.

  **État :** la trajectoire, ses projections et le vecteur position sont déjà
  mis à jour jusqu'à l'instant sélectionné, tandis que les limites des axes
  restent fixes.
- [x] Dans les trois visualisations 3D, conserver uniquement la trajectoire et
  retirer le graphique séparé des équations horaires.
- [x] Harmoniser la publication des versions enseignant et étudiant : conserver
  une image statique dans la version enseignant et afficher directement le
  widget dans la version étudiant.
- [x] Étudier un autre système de coordonnées, par exemple une trajectoire
  hélicoïdale dans un cylindre.
- [x] Ajouter à la visualisation cylindrique générale des curseurs permettant
  d'étudier séparément l'effet de $a_r$, $A$ et $B$.

  **État :** les lois $r(t)=r_0+a_rt$, $\theta(t)=At$ et $z(t)=Bt$ sont déjà
  implémentées et leurs coefficients peuvent désormais être modifiés
  interactivement. Les bornes des curseurs garantissent $0\leq r(t)\leq 6$
  et $0\leq z(t)\leq 10$.
- [x] Demander les dimensions des coefficients $A$, $B$ et $C$, leur
  interprétation physique et la raison pour laquelle $\omega t$ doit être sans
  dimension.
- [x] Vérifier l'homogénéité dimensionnelle des coefficients à partir de leurs
  unités.
- [x] Ajouter, dans les trois visualisations 3D, des cases permettant de choisir
  les projections à afficher.
- [x] Afficher, dans la représentation 3D, les projections associées aux
  équations horaires.
- [x] Mettre à jour la trajectoire et ses projections jusqu'à l'instant
  sélectionné avec le curseur.
- [x] Faire coïncider les graduations extrêmes avec les limites fixées des axes.
- [x] Ajouter, dans les trois visualisations 3D, les projections de la
  trajectoire sur les plans $xy$, $xz$ et $yz$, ainsi que les segments reliant
  le point $M$ à ses projections.
- [x] Pour les mouvements cylindriques, ajouter des questions sur les dimensions,
  les unités et l'interprétation physique de $r_0$, $a_r$, $A$ et $B$, puis
  étudier interactivement plusieurs cas particuliers.
- [ ] Ajouter une animation autonome représentant une cycloïde.

## Notebook 3 — Vitesse et accélération

### Mouvement circulaire en coordonnées polaires

- [x] Exprimer les composantes polaires de la vitesse et de l'accélération.
- [x] Implémenter les fonctions permettant de calculer ces composantes.
- [x] Visualiser dans un repère polaire la trajectoire, la vitesse et
  l'accélération centripète dans le cas uniforme.
- [x] Expliquer la différence entre les directions centripète et centrifuge.
- [x] Relier l'accélération centripète à la résultante des forces avec la
  deuxième loi de Newton.
- [x] Implémenter et représenter les forces centripète et centrifuge en
  précisant leurs référentiels d'utilisation.
- [ ] Définir avec l'équipe enseignante les questions de synthèse du bilan.

  **État :** un résumé et une première question de synthèse ont été rédigés ;
  le bloc est marqué « À revoir avec les profs » dans le notebook enseignant
  en attendant leur validation.

## Notebook 4 — Dynamique (durée prévue : 2 h)

### Sources classées (stage numérique, dans `.temp/activites/`)

Périmètre de la branche `notebook-dynamique` : uniquement les sources
ci-dessous. Les sources liées aux oscillations ou hors mécanique du point ne
sont pas traitées dans cette branche (voir Notebook 5 et note en fin de
fichier).

- Activité 1 (`a1/activite-1.md`, correction `corrections-activites/Activite1`)
  — chute libre : $z(t)$, énergies cinétique/potentielle/mécanique, puis
  balistique (Q4 : trajectoire $z(x)$ avec vitesse initiale inclinée).
- Activité 2 (`a2/activite-2.md`, correction `corrections-activites/Activite2`)
  — chute avec frottement linéaire (méthode d'Euler) puis quadratique
  (régime turbulent).
- Sujet de soutenance 1 — Ski de vitesse : descente rectiligne avec
  frottement quadratique.
- Sujet de soutenance 2 — Viscosimètre : chute libre avec frottement
  linéaire (loi de Stokes).
- Sujet de soutenance 3 — Badminton : balistique avec/sans frottement,
  parabole de sûreté.

### Répartition en TP

| TP | Contenu | Sources | État |
|---|---|---|---|
| TP04 | Chute libre sans frottement : équation horaire, énergies (Ec, Ep, Em) | Activité 1 (base + Q3) | ✅ fait |
| TP05 | Résolution numérique d'une EDO : chute avec frottement (méthode d'Euler, comparaison avec `scipy`/Runge-Kutta) | Activité 2 + application au parachutiste ; viscosimètre encore à intégrer | ⚠️ cœur du TP fait |
| TP06 | Mouvement sur plan incliné avec frottement | Sujet 1 (Ski de vitesse) | à faire |
| TP07 | Balistique : sans frottement → avec frottement, parabole de sûreté | Activité 1 (Q4) + Sujet 3 (Badminton, en application finale) | ✅ fait |

Raisonnement : la résolution numérique d'EDO (méthode d'Euler) est la
première fois du cours que les étudiants résolvent une équation
différentielle sans solution analytique directe — cela mérite son propre
rappel de cours et sa propre progression (Euler codé par l'étudiant →
comparaison avec la solution exacte quand elle existe → limites d'Euler à
grand pas de temps → `scipy`/Runge-Kutta), plutôt que d'être une simple
sous-section de la chute libre. Le Sujet 2 (Viscosimètre) est exactement le
cas de frottement linéaire appliqué à un cas concret, donc fusionné comme
application plutôt que comme TP séparé. Le Sujet 1 (plan incliné) reste à
part malgré le frottement quadratique partagé avec la chute avec
frottement, car la mise en équation change (décomposition du poids selon le
plan) — ce n'est pas la même chose, contrairement au Sujet 2.

### Continuité avec les notebooks précédents

- [ ] Faire valider par l'équipe enseignante le contenu, le niveau de
  difficulté et la progression pédagogique des TP04 et TP05.
- [x] Reprendre les sujets du stage numérique, les mettre en forme et conserver
  la même structure pédagogique que dans les premiers notebooks.
- [x] Relier explicitement les activités de dynamique aux outils déjà étudiés :
  équations horaires, trajectoire, vitesse, accélération et représentation des
  forces.
- [ ] Réutiliser, lorsque cela est pertinent, les fonctions et visualisations
  développées dans les notebooks de cinématique plutôt que repartir de zéro.

### Chute libre

- [ ] Examiner le « stage numérique » ainsi que des exemples de parachutiste
  et de plongeur.

  **État :** les sources du stage numérique ont été classées et l'application
  au parachutiste est intégrée au TP05 ; l'exemple du plongeur reste à décider.
- [ ] Introduire des animations permettant de comparer ces différents cas.

### Balistique

- [x] Réaliser une étude paramétrique faisant varier les conditions initiales :
  $v_0$, $h_0$ et $\theta_0$.
- [x] Introduire la parabole de sûreté.
- [x] Comparer les mouvements avec et sans frottement.

## Notebook 5 — Oscillations (au moins deux notebooks)

### Sources classées (stage numérique, dans `.temp/activites/`)

**Non traité dans la branche `notebook-dynamique`** — à reprendre dans une
branche dédiée à ce notebook.

- Activité 3 (`a3/activite-3.md`, correction
  `corrections-activites/Activite3_Oscillation`) — oscillateur amorti
  (ressort + frottement fluide, facteur de qualité Q), oscillateur de
  Van der Pol, circuit RLC amorti.
- Activité 4 (`a4/activite-4.md`, correction `corrections-activites/Activite4`)
  — oscillations forcées, diagramme de Bode, résonance.
- Sujets de soutenance 4 et 5 — Balançoire 1/2 : pendule sans frottement,
  approximation des petits angles vs solution exacte.
- Sujet de soutenance 6 — Balançoire 3 : pendule avec frottement.
- Sujet de soutenance 7 — Camion sur route ondulée : oscillations forcées,
  résonance.
- Sujet de soutenance 8 — Circuit LC-RLC : oscillations électriques.

### Généralités

- [ ] Ajouter une section présentant les notions générales et les équations
  fondamentales.
- [ ] Comparer, pour chaque situation, les systèmes mécaniques et
  électroniques en mettant en évidence leurs analogies.

### 1. Oscillations libres

- [ ] Étudier les oscillations libres en fonction des différents facteurs de
  qualité.
- [ ] Présenter des applications mécaniques :
  - [ ] système masse-ressort ;
  - [ ] pendule ;
  - [ ] associations de ressorts.
- [ ] Présenter des applications électroniques :
  - [ ] circuit LC ;
  - [ ] circuit RLC.

### 2. Oscillations forcées

- [ ] Tracer $x(t)$ en tenant compte de l'amplitude $A(\omega)$ et de la phase
  $\varphi(\omega)$.
- [ ] Étudier une force d'excitation différente d'un cosinus.
- [ ] Présenter le phénomène de résonance.
- [ ] Contacter Hamzeh pour obtenir le code source de l'exemple de l'avion.
- [ ] Introduire une animation ou un média mettant en évidence le phénomène
  de résonance, par exemple un pont en résonance.
- [ ] Présenter des applications mécaniques :
  - [ ] système masse-ressort ;
  - [ ] pendule.
- [ ] Présenter des applications électroniques :
  - [ ] circuit LC ;
  - [ ] circuit RLC.
- [ ] Rechercher des exemples concrets et parlants.

## Hors périmètre (autre module ?)

Sources du stage numérique qui ne relèvent pas de la mécanique du point et ne
correspondent à aucun notebook prévu ci-dessus : Activité 5 (résolution de
circuits linéaires par pivot de Gauss, analyse nodale), Activité 6 (série de
Fourier), Sujet de soutenance 9 (circuit à AOP), Sujets 10 et 11 (débruitage
d'un signal périodique). À clarifier avec l'équipe enseignante : module
électronique/traitement du signal distinct, ou à intégrer autrement ?

## Structure du contenu

- [x] Entre les questions théoriques et le travail de programmation, ajouter un
  bloc « Appelez le professeur » demandant aux étudiants de faire valider leurs
  réponses avant de commencer à coder.

  **Objectif :** distinguer clairement le raisonnement physique de sa mise en
  œuvre numérique et permettre une vérification intermédiaire avec
  l'enseignant.

  **État :** conservé uniquement là où la question théorique demande une
  véritable dérivation dont une erreur se propagerait silencieusement au
  code (TP01 §3-4, TP03 §2-3). Retiré des sections où la question ne porte
  que sur l'interprétation d'une formule déjà donnée (TP01 §2, TP02 §2-5),
  où le risque de dérivation est faible.
- [ ] Terminer chaque notebook par une application physique concrète, placée
  dans la progression principale ou dans « Pour aller plus loin » selon sa
  difficulté.

  **Principe :** cette activité finale doit mobiliser les notions étudiées dans
  une situation physique réelle, et ne pas constituer uniquement un exemple
  mathématique supplémentaire.

  **État :** le TP05 se termine par l'application au parachutiste et le TP07
  par l'étude du volant de badminton. Les applications finales des autres
  notebooks restent à compléter ou à valider.

- [ ] Ajouter, vers la fin de chaque chapitre ou notebook, une section
  « À retenir ».

  **État :** cette section existe déjà dans les TP01 à TP05 ainsi que dans le
  TP07, mais doit encore être généralisée aux contenus suivants.
- [ ] Ajouter une section « Compétences acquises ».

  **État :** cette section existe déjà dans les TP01 à TP05 ainsi que dans le
  TP07, mais doit encore être généralisée aux contenus suivants.
