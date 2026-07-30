# Tâches à réaliser

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

### Vitesse et accélération

- [ ] Expliquer la différence entre les notions centripète et centrifuge.
- [ ] Ajouter une animation représentant une cycloïde.

## Notebook 4 — Dynamique (durée prévue : 2 h)

### Chute libre

- [ ] Examiner le « stage numérique » ainsi que des exemples de parachutiste
  et de plongeur.
- [ ] Introduire des animations permettant de comparer ces différents cas.

### Balistique

- [ ] Réaliser une étude paramétrique faisant varier les conditions initiales :
  $v_0$, $h_0$ et $\theta_0$.
- [ ] Introduire la parabole de sûreté.
- [ ] Comparer les mouvements avec et sans frottement.

## Notebook 5 — Oscillations (au moins deux notebooks)

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

## Structure du contenu

- [ ] Ajouter, vers la fin de chaque chapitre ou notebook, une section
  « À retenir ».

  **État :** cette section existe déjà dans le notebook 2, mais pas dans tous
  les contenus concernés.
- [ ] Ajouter une section « Compétences acquises ».

  **État :** cette section existe déjà dans le notebook 2, mais pas dans tous
  les contenus concernés.
