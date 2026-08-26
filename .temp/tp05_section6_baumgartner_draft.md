# Draft : §6 Baumgartner (retiré de TP05, à reprendre plus tard)

Plan discuté pour la reprise : introduire rho(z) variable (modèle
exponentiel rho(z)=rho0*exp(-z/H), H~8000m, DONNE et non dérivé),
6.1 Théorie (système couplé dz/dt=v_z, dv_z/dt=-g+mu(z)/m*v_z^2,
mu(z)=1/2 rho(z) Cx S ; pourquoi non séparable contrairement au §3),
6.2 Implémentation (Euler couplé sur (v_z, z), conditions initiales
z(0)=39000, v_z(0)=0), 6.3 Analyse (comparaison simulation vs données
réelles uniquement, pas de comparaison avec l'ancien modèle rho constant).

---

# Contenu précédent (rho constant, restreint au subsonique) :


## Cell type: markdown tags=[]
```
## 6. Application : le saut de Felix Baumgartner (Red Bull Stratos)

Le 14 octobre 2012, le parachutiste autrichien Felix Baumgartner s'est
élancé depuis une capsule à environ 39 km d'altitude (mission *Red
Bull Stratos*), atteignant au passage une vitesse d'environ 377 m/s —
plus rapide que le son à cette altitude. Équipé de son scaphandre, il
présente une masse $m\approx120$ kg, une surface frontale
$S\approx1{,}1$ m$^2$, et un coefficient de traînée $C_x\approx0{,}7$.

Notre modèle de frottement quadratique (§3) suppose une masse
volumique de l'air $\rho$ constante ; il n'est donc valable qu'à basse
altitude, là où l'air est dense et où la vitesse de Baumgartner est
**subsonique**, c'est-à-dire en toute fin de chute libre, juste avant
l'ouverture de son parachute. Comparons la vitesse limite prédite par
notre modèle à la vitesse qu'il a réellement atteinte à ce moment-là.

![Capsule et combinaison de Felix Baumgartner, exposition « Red Bull Stratos » au National Air and Space Museum](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/RedBullStratosNASM.jpg/330px-RedBullStratosNASM.jpg){width=50%}

*Photo : Eric Long, Smithsonian National Air and Space Museum (domaine public).*
```

## Cell type: code tags=['hide-input']
```
# Données réelles du saut (Red Bull Stratos, 14/10/2012) :
# temps (s) et vitesse mesurée (km/h)
temps_mesure = np.array([
    0, 2, 5, 8, 10, 12, 15, 17, 19, 21, 23, 25,
    27, 30, 32, 33, 34, 36, 38, 40, 42, 44, 46, 48,
    50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72,
    74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96,
    98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120,
    122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144,
    146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168,
    170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192,
    194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216,
    218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240,
    242, 244, 246, 248, 250, 252, 254, 256, 258, 260
])
vitesse_mesure_kmh = np.array([
    0, 67, 187, 287, 364, 430, 530, 612, 670, 749, 808, 866,
    924, 1013, 1076, 1107, 1126, 1174, 1212, 1260, 1285, 1301, 1317, 1340,
    1355, 1334, 1314, 1307, 1261, 1196, 1104, 1056, 993, 957, 917, 850,
    822, 803, 762, 726, 690, 665, 647, 627, 611, 592, 568, 548,
    500, 526, 485, 470, 457, 447, 440, 427, 415, 403, 394, 386,
    375, 372, 374, 375, 375, 373, 371, 367, 361, 359, 358, 361,
    355, 351, 347, 339, 329, 322, 313, 312, 308, 298, 293, 290,
    286, 289, 289, 289, 289, 285, 282, 279, 279, 279, 271, 265,
    259, 254, 241, 229, 221, 223, 220, 224, 221, 220, 222, 221,
    221, 219, 218, 218, 217, 215, 213, 212, 215, 214, 215, 210,
    210, 208, 205, 204, 203, 199, 203, 203, 203, 182
])
vitesse_mesure = vitesse_mesure_kmh / 3.6  # conversion en m/s
```

## Cell type: code tags=['hide-input']
```
def tracer_baumgartner(rho=1.225):
    """Compare la vitesse mesurée de Baumgartner à la vitesse limite prédite par le modèle quadratique."""
    m = 120.0    # masse équipée [kg]
    S = 1.1      # surface frontale [m^2]
    Cx = 0.7     # coefficient de traînée
    g = 9.81

    mu = 0.5 * rho * Cx * S
    v_lim = np.sqrt(m * g / mu)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(temps_mesure, vitesse_mesure, color='tab:blue', marker='o', markersize=3, linewidth=1, label='vitesse mesurée')
    ax.axhline(v_lim, color='tab:red', linestyle='--', linewidth=2, label=f'vitesse limite modèle ({v_lim:.1f} m/s)')
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$v$ (m/s)')
    ax.set_title('Chute libre de Felix Baumgartner')
    ax.grid(alpha=0.3)
    ax.legend(loc='upper right')

    plt.show()
    plt.close(fig)

tracer_baumgartner()
```

## Cell type: code tags=['remove-cell']
```
interact(
    tracer_baumgartner,
    rho=FloatSlider(value=1.225, min=0.1, max=1.3, step=0.05, description='ρ air (kg/m³)'),
);
```

## Cell type: markdown tags=[]
```
:::{admonition} 🔍 Exploration
:class: tip

1. Comparez la vitesse limite prédite par le modèle
   ($\rho=1{,}225$ kg/m$^3$, air au niveau du sol) à la vitesse
   réellement mesurée en toute fin de chute libre (dernières valeurs
   du graphique). Le modèle est-il satisfaisant dans ce régime ?
2. Diminuez $\rho$ (air moins dense, comme en haute altitude). Que
   devient la vitesse limite prédite par le modèle ? Est-ce cohérent
   avec le fait que Baumgartner ait dépassé la vitesse du son en
   début de chute ?
3. Pourquoi notre modèle ne peut-il pas être utilisé pour décrire
   toute la chute libre de Baumgartner, du saut jusqu'à l'ouverture
   du parachute ?
:::
```

## Cell type: markdown tags=[]
```
*Écrivez vos réponses ici (Markdown, $\LaTeX$…) :*

1. --
2. --
3. --
```

## Cell type: markdown tags=[]
```
:::{admonition} Réponses
:class: note

1. Le modèle prédit $v_{lim}=\sqrt{mg/\mu}\approx50{,}0$ m/s, très
   proche de la vitesse mesurée en toute fin de chute libre
   ($\approx182$ km/h $\approx50{,}6$ m/s) : un excellent accord, car
   l'air y est effectivement dense, proche de $\rho=1{,}225$ kg/m$^3$.
2. En diminuant $\rho$, $v_{lim}=\sqrt{mg/\mu}$ augmente (puisque
   $\mu\propto\rho$) : un air moins dense freine moins, la vitesse
   limite prédite devient beaucoup plus grande. C'est cohérent : en
   haute altitude, l'air est beaucoup moins dense, ce qui explique
   physiquement pourquoi Baumgartner a pu atteindre une vitesse
   supersonique avant que le frottement ne le ralentisse
   suffisamment.
3. Parce que notre modèle suppose $\rho$ constante, alors que la masse
   volumique de l'air varie énormément entre 39 km d'altitude (air
   extrêmement raréfié) et le niveau du sol (air dense) : il faudrait
   un modèle avec $\rho(z)$ dépendant de l'altitude pour décrire toute
   la chute, ce qui dépasse le cadre de ce TP.
:::
```

## Cell type: markdown tags=[]
```
:::{important}
Pour afficher la version interactive, ouvrez le **Notebook enseignant** en
local ou ouvrez ce notebook dans Google Colab.
:::
```
