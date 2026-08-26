**Activité 6** **Série de Fourier**

**Objectif :** Dans cette activité, l'objectif est d'utiliser l'analyse
numérique pour trouver la série de Fourier d'une fonction périodique
$`f(t)`$. Cela nous aide à comprendre comment un signal périodique se
comporte dans le domaine fréquentiel. Nous allons explorer la série de
Fourier d'un signal périodique en combinant des concepts mathématiques
et électroniques.

**Série de Fourier trigonométrique :** Joseph Fourier a découvert qu'un
phénomène périodique non sinusoïdal peut être exprimée comme une somme
infinie de fonctions sinusoïdales. Rappelons qu'une fonction périodique
est une fonction qui se répète toutes les périodes $`T`$ secondes. En
d’autres termes, une fonction périodique satisfait la condition suivante
:

``` math
f(t) = f(t + nT)
```

Où $`n`$ est un entier et $`T`$ est la période de la fonction.

D'après le théorème de Fourier, toute fonction périodique de fréquence
$`\omega_{0}`$ peut être exprimée comme une somme infinie des fonctions
sinus ou cosinus, dont leurs fréquences sont des multiples entiers de
$`\omega_{0}`$ .Ainsi, $`f(t)\`$peuvent être exprimé comme :

``` math
f(t) = a_{0} + a_{1}\cos\left( \omega_{0}t \right) + b_{1}\sin\left( \omega_{0}t \right) + a_{2}\cos\left( {2\omega}_{0}t \right) + b_{2}\sin\left( 2\omega_{0}t \right)
```

``` math
+ a_{3}\cos\left( {3\omega}_{0}t \right) + b_{3}\sin\left( 3\omega_{0}t \right) + \ldots
```

*Or*
$`f(t) = \underset{DC}{\overset{a_{0}}{︸}} + \underset{AC}{\overset{\sum_{n = 1}^{\infty}{(a_{n}\cos\left( {n\omega}_{0}t \right) + b_{n}\sin\left( {n\omega}_{0}t \right))}}{︸}}`$

Où :

- $`\omega_{0} = \frac{2\pi}{T}`$ est appelée la fréquence fondamentale
  en radians par seconde.

- $`\sin\left( n\omega_{0}t \right)`$ ou
  $`\cos\left( n\omega_{0}t \right)`$ est appelée la nième harmonique de
  $`f(t)`$.

- $`f(t)`$ est appelée la série trigonométrique de Fourier.

- $`a_{n}`$ et $`b_{n}\`$sont les coefficients de Fourier.

- $`a_{0}`$ est la composante continue (DC) ou la valeur moyenne de
  $`f(t)`$. (Rappel que les sinusoïdes ont des valeurs moyennes nulles).

- $`a_{n}`$ et $`b_{n}\`$(pour $`n \neq 0)`$ sont les amplitudes des
  sinusoïdes dans la composante alternative (AC).

Ainsi, la série de Fourier d'une fonction périodique $`f(t)`$ est une
représentation qui décompose $`f(t)`$ en une composante continue (DC) et
une composante alternative (AC) comprenant une série infinie de
sinusoïdes harmoniques.

La tâche majeure des séries de Fourier est la détermination du
coefficient de Fourier $`a_{0},`$ $`a_{n}`$ et $`b_{n}`$. Le processus
de détermination de ces coefficients et nommée analyse de Fourier.
Soit :

``` math
a_{0} = \ \frac{1}{T}\ \int_{0}^{T}{f(t)\ dt}
```

``` math
a_{n} = \ \frac{2}{T}\ \int_{0}^{T}{f(t)\ cos(n\omega_{0}t)\ dt}
```

``` math
b_{n} = \ \frac{2}{T}\ \int_{0}^{T}{f(t)\ sin(n\omega_{0}t)\ dt}
```

Une forme alternative de la fonction $`f(t)\`$est la forme
amplitude-phase suivante :

*Or*
$`f(t) = a_{0} + \sum_{n = 1}^{\infty}{(A_{n}\cos\left( {n\omega}_{0}t + \varphi_{n} \right))}`$

Où

$`A_{n} = \sqrt{a_{n}^{2} + b_{n}^{2}}`$
$`\varphi_{n} = \arctan\left( \frac{b_{n}}{a_{n}} \right)`$

Le spectre de fréquence d'un signal consiste à tracer les amplitudes
($`A_{n}`$) et les phases ($`\varphi_{n}`$) des harmoniques par rapport
à la fréquence fondamentale.

**Travail à effectuer :**

On considère le signal carré périodique suivant :

<figure>
<img src="media/media/image1.png"
style="width:3.20373in;height:1.23601in"
alt="Une image contenant diagramme, ligne, Tracé, Parallèle Description générée automatiquement" />
<figcaption><p> : signal carré</p></figcaption>
</figure>

**Calcul analytique à faire :**

1)  Déterminer l’expression analytique de la fonction $`f(t)`$ sur une
    période $`T`$.

2)  Déterminer la période fondamentale $`T`$ et en déduire la fréquence
    fondamentale $`\omega_{0}`$.

3)  Déterminer analytiquement la valeur moyenne $`a_{0}\`$du signal
    $`f(t)`$. Expliquer le résultat obtenu.

4)  Déterminer analytiquement les valeurs des coefficients de Fourier
    $`a_{n}`$ et $`b_{n}`$.

5)  Récrire l’expression $`f(t)`$ en prenant en compte les valeurs de
    $`a_{0},\`$ $`a_{n}`$ et $`b_{n}`$.

6)  Tracer le spectre (amplitudes et phases) du signal $`f(t)`$ pour
    n=5. Commenter le résultat obtenu.

**Calcul numérique à faire :**

L’idée dans cette partie est de développer un code sous python
permettant de calculer numériquement la série de Fourier du signal
$`f(t)`$ (figure 1). Voici l’algorithme simplifié de code à réaliser
pour la série de Fourier :

- Initialisation :

  - Entrée : période $`T`$ du signal périodique.

  - Entrée : $`n`$, nombre d'harmoniques

- Définition du signal carré périodique :

  - Fonction signal(t) :

- Calcul de l'intégrale d'une fonction avec la méthode des trapèzes :

  - Fonction CalculIntegral(fonc, a, b, N) :

    - Générer $`N`$ points entre $`a`$ et b. soit $`N = 1000`$

    - Calculer les valeurs de la fonction $`y = fonc(x)`$

    - Utiliser la méthode des trapèzes pour approximer l'intégrale.

- Calcul des coefficients de Fourier :

  - Fonction SerieFourier(signal, T, n_harmoniques) :

    - Calcul des coefficients $`a_{0}`$, $`a_{n}`$ et $`b_{n}`$

- Reconstruction du signal à partir des coefficients de Fourier calculés
  :

  - Fonction SignalReconstruit(t) :

- Calcul des amplitudes et des phases des harmoniques

1)  Soit $`n = 5`$. Tracer le signal original $`f(t)`$ et le signal
    reconstruit sur la même figure. Commenter le résultat obtenu.

2)  Tracer les amplitudes $`A_{n}\`$obtenues par calcul numérique en
    fonction des harmoniques.

3)  Tracer les phases $`\varphi_{n}\`$obtenues par calcul numérique en
    fonction des harmoniques.

4)  Retracer le signal original $`f(t)`$ et le signal reconstruit sur la
    même figure pour n= 5, 10, 15, et 20. Commenter et justifier les
    résultats obtenus.
