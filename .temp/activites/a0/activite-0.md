**Activité 0**

**Analyse Numérique**

**Partie 1 – Résolution d’équations différentielles**

Objectif : Utiliser des méthodes itératives (ex : méthode d’Euler) afin
de déterminer une approximation de la solution d’une équation
différentielle

1.  Introduction

L’analyse numérique est une discipline à l’interface des mathématiques
et de l’informatique qui permet de résoudre certains problèmes de
mathématiques numériquement.

Certains problèmes peuvent être résolus de **façon exacte** par un
algorithme en un nombre fini d’opérations. Ces algorithmes sont appelés
**méthodes directes**. On utilise ce type d’algorithmes pour la
résolution des systèmes d’équations linéaires par exemple (méthode du
pivot de Gauss).

D’autres problèmes, qui ne peuvent être résolus avec des méthodes
directes, sont résolus par des **méthodes itératives** afin de
déterminer une **approximation de la solution**. On utilise ce type
d’algorithme pour le calcul d’intégrales ou la résolution d’équations
différentielles par exemple.

On étudiera dans cette activité la **méthode de Euler explicite** pour
résoudre des équations différentielles du 1<sup>er</sup> ordre et du
2<sup>ème</sup> ordre.

2.  Equation différentielle du premier ordre

    1.  Définition

> Pour rappel, une équation différentielle du premier ordre est une
> équation du type :
>
> ``` math
> a(t)y'(t) + b(t)y(t) = c(t)\ \ \ \ \ \ \ \ \ \ \ \ (E)
> ```
>
> où $`y`$ est une fonction réelle de la variable $`t`$, $`y'`$ sa
> dérivée par rapport à $`t\`$et $`a,\ b,\ c`$ sont trois fonctions.

2.  Solution exacte

> L’ensemble des solutions de l’équation
> $`\ a(t)y'(t) + b(t)y(t) = c(t)`$ est :
>
> ``` math
> \{ y_{p} + y_{h}\}
> ```
>
> Où :

- $`y_{h}`$ est solution de $`y(t) + \alpha(t)y(t) = 0`$ avec
  $`\alpha(t) = \frac{b(t)}{a(t)}`$ :

> $`y_{h} = Ce^{- A(t)}`$ avec $`A(t) = \int_{}^{}{\alpha(t)dt}`$

- $`y_{p}`$ est une solution particulière de $`(E)`$. (A déterminer avec
  la méthode de variation de la constante par exemple).

  1.  Approximation de la solution avec la méthode d’Euler

- On va résoudre l’équation :

> 
> ``` math
> a(t)y'(t) + b(t)y(t) = c(t)\ \ \ \ \ \ \ \ \ \ \ \ (E)
> ```
>
> sur un intervalle $`I\  = \ \lbrack t_{o},\ t_{N}\rbrack`$ d’amplitude
> $`T`$ avec une condition initiale $`y\left( t_{o} \right) = \ y_{0}`$
> en utilisant la méthode d’Euler qui nous donnera une approximation de
> la solution.
>
> L’équation différentielle $`(E)\`$peut s’écrire sous la forme :
>
> ``` math
> y'(t)\  = \ F(t,\ y(t))
> ```
>
> avec $`F(t,\ y(t))\  = \ \frac{c(t)\  - \ b(t)y(t)}{a(t)}`$ si
> $`a(t)\  \neq 0`$

- Subdivision de l’intervalle

> On se place sur $`I\  = \ \lbrack t_{o},\ t_{N}\rbrack`$, un
> intervalle d’amplitude $`T`$, que l’on va subdiviser en $`N`$
> intervalles réguliers d’amplitude $`h`$ de la forme
> $`\lbrack t_{i},\ t_{i + 1}\rbrack`$, avec
> $`i\  \in \ \left. ⟦0,\left. \ N - 1 \right.⟧ \right.\`$. On a donc
> $`h\  = \ \frac{T}{N}`$

- Recherche de la solution

> On cherche $`y(t_{i})`$ pour chaque valeur de $`t_{i}`$ (approximation
> par discrétisation). Plus on prendra de valeurs pour $`t_{i}`$, plus
> on aura de points pour tracer la courbe représentative de $`y(t)`$ et
> plus la représentation graphique sera précise.
>
> On va donc faire tendre $`N`$ vers $`+ \infty`$ et donc
> $`h\  = \ \frac{T}{N}\`$vers 0.
>
> On peut donc faire un développement limité de
> $`y(t_{i + 1})\  = \ y(t_{i}\  + \ h)`$ à l’ordre 1 au voisinage de
> $`h\  = \ 0`$ :
>
> ``` math
> y(t_{i + 1})\ \  = \ y(t_{i}\  + \ h)\  = \ y(t_{i})\  + \ hy'(t_{i})\  + \ o(h)
> ```

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>Rappel :</p>
<p>Si <span class="math inline"><em>f</em></span> est de classe <span
class="math inline"><em>C</em><sup><em>n</em></sup></span> au voisinage
de <span class="math inline"><em>x</em> = <em>a</em></span> alors :</p>
<p>— <span class="math inline"><em>f</em></span> admet un DL à l’ordre
<span class="math inline"><em>n</em></span> au voisinage de <span
class="math inline"><em>x</em> = <em>a</em> </span>:</p>
<p><span class="math display">$$f(x)\  = \ f(a)\  + \frac{\ f'(a)}{1!}\
(x\  - \ a)\  + \ \frac{f^{''}(a)}{2!}(x\  - \ a)²\  + \  \cdot \  \cdot
\  \cdot \  + \ \frac{f^{(n)}(a)}{n!}{(x\  - \ a)}^{n}\  + \ o{((x\  - \
a)}^{n})$$</span></p>
<p>ou (en posant <span
class="math inline"><em>x</em> = <em>a</em> + <em>h</em></span>)</p>
<p>— f admet un DL à l’ordre<span class="math inline"> <em>n</em></span>
au voisinage de <span class="math inline"><em>h</em> = 0</span> :</p>
<p><span class="math display">$$f(a + h)\  = \ f(a)\  + \frac{\
f'(a)}{1!}\ h\  + \ \frac{f^{''}(a)}{2!}h²\  + \  \cdot \  \cdot
\  \cdot \  + \ \frac{f^{(n)}(a)}{n!}h^{n}\  + \
o{(h}^{n})$$</span></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> On a :
> $`y(t_{i + 1})\ \  = \ y(t_{i}\  + \ h)\  = \ y(t_{i})\  + \ hy'(t_{i})\  + \ o(h)`$
>
> Or l’équation différentielle $`(E)`$ prise en $`t\  = \ t_{i}`$, nous
> donne :
>
> ``` math
> \ y'(t_{i})\  = \ F(t_{i},\ y(t_{i}))
> ```
>
> On a
> donc$`\ y(t_{i + 1})\ \  = \ y(t_{i})\  + \ hF(t_{i},\ y(t_{i}))\  + \ o(h)`$
>
> En négligeant $`o(h),`$ on a :
> $`y\left( t_{i + 1} \right)\  = \ y\left( t_{i} \right) + \ hF\left( t_{i},\ y\left( t_{i} \right) \right)`$
>
> Posons $`y(t_{i})\  = \ y_{i\ }`$
>
> On a donc la relation de récurrence suivante :

``` math
y_{i + 1\ } = \ y_{i\ } + \ hF(t_{i},y_{i})
```

> Comme la condition initiale nous donne $`y_{o}`$, on peut calculer
> $`y_{o}`$, $`y_{1}`$, ..., $`y_{N}`$.

3.  Travail à effectuer

On considère l’équation différentielle :

``` math
ty'(t) + y(t) = 1\ \ \ \ \ \ \ \ \ \ \ \ (E)
```

sur $`I\  = \ \lbrack 1,2\rbrack`$ la condition initiale
$`y(1)\  = \ 2`$

- **Question 1 :**

  1)  Donner la solution exacte de *(E)*

  2)  Calculer $`y(t)`$ pour
      $`t_{0} = 1,\ \ t_{1} = 1.1,\ {\ t}_{2} = 1.2,\ t_{3} = 1.3\ \`$

> (On arrondira les résultats au centième).

- **Question 2 :** On va résoudre $`(E)`$ en utilisant la méthode
  d’Euler :

  1)  Donner $`F(t,y(t))`$

  2)  En déduire la relation de récurrence donnant $`y_{i + 1\ }`$

  3)  En prenant $`h = 0.1`$ , calculer $`y_{i + 1\ }`$ avec
      $`i\  \in \ \left. ⟦0,\left. \ 2 \right.⟧ \right.\`$.

(On arrondira les résultats au centième).

- **Question 3 :** Comparer les valeurs calculées avec chacune des
  méthodes.

4.  Equation différentielle du second ordre

    1.  Définition

> Pour rappel, une équation différentielle linéaire du second ordre, à
> coefficients constants, est une équation du type :
>
> $`ay’’(t)\  + \ by’(t)\  + \ cy(t)\  = \ f(t)`$ *(E)*
>
> où $`y`$ est une fonction réelle de la variable $`t`$ , $`y'`$ sa
> dérivée par rapport à $`t`$ , $`y''`$ sa dérivée seconde par rapport à
> $`t`$, et $`\ a,\ b,\ c\mathbb{\in \ R}`$ *,* $`a \neq 0`$ et *f* est
> une fonction continue sur un intervalle ouvert *I* .

2.  Solution exacte

> L’ensemble des solutions de l’équation
> $`\ ay’’(t)\  + \ by’(t)\  + \ cy(t)\  = \ f(t)`$ est :
>
> ``` math
> \{ y_{p} + y_{h}\}
> ```
>
> Où :

- $`y_{h}`$ est solution de $`ay’’(t) + by’(t) + cy(t) = 0`$
  $`\left( E_{0} \right)`$

> La résolution de cette équation homogène fait appel au polynôme
> caractéristique $`ar^{2} + br + c = 0`$ *(PC)*
>
> 3 cas possibles suivant le signe du discriminant
> $`\mathrm{\Delta} = b^{2} - 4ac`$ de *(PC)* :

- Si $`\mathrm{\Delta} > 0`$, *(PC)* possède deux racines réelles
  distinctes $`r_{1} \neq r_{2}`$ et les solutions de
  $`\left( E_{0} \right)`$ sont données par :

> $`y_{h}(t) = C_{1}e^{r_{1}t} + C_{2}e^{r_{2}t}`$ où
> $`C_{1},\ C_{2}\mathbb{\in \ R}`$

- Si $`\mathrm{\Delta} = 0`$, *(PC)* possède une racine double $`r_{0}`$
  et les solutions de $`\left( E_{0} \right)`$ sont données par :

> $`y_{h}(t) = C_{1}e^{r_{0}t} + C_{2}te^{r_{0}t}`$ où
> $`C_{1},\ C_{2}\mathbb{\in \ R}`$

- Si $`\mathrm{\Delta} < 0`$, *(PC)* possède deux racines complexes
  conjuguées :

> $`r_{1} = \alpha + i\beta`$ *,* $`r_{2} = \alpha - i\beta`$
>
> les solutions réelles de $`\left( E_{0} \right)`$ sont données par :
>
> $`y_{h}(t) = e^{\alpha t}(Acos(\beta t) + Bsin(\beta t))`$ où
> $`A,B\mathbb{\in \ R}`$

- $`y_{p}`$ est une solution particulière de $`(E)`$.

  1.  Approximation de la solution avec la méthode d’Euler

      - On va résoudre l’équation 

$`ay’’(t)\  + \ by’(t)\  + \ cy(t)\  = \ f(t)`$ *(E)*

> sur un intervalle $`I = \lbrack t_{0},t_{N}\rbrack`$ d’amplitude $`T`$
> avec les conditions initiales $`y_{0}(t_{0}) = u_{0}`$ et
> $`y_{0}'(t_{0}) = v_{0}`$ en utilisant la méthode d’Euler qui nous
> donnera une approximation de la solution.
>
> L’équation différentielle *(E)* peut s’écrire sous la forme :
>
> ``` math
> y''(t) = F(t,\ y(t),\ y'(t))
> ```
>
> avec $`F(t,y(t),\ y'(t)) =`$ $`\ \frac{f(t) - by'(t) - cy(t)}{a}`$ si
> $`a \neq 0`$

- Subdivision de l’intervalle

> On se place sur $`I\  = \ \lbrack t_{o},\ t_{N}\rbrack`$, un
> intervalle d’amplitude $`T`$, que l’on va subdiviser en $`N`$
> intervalles réguliers d’amplitude $`h`$ de la forme
> $`\lbrack t_{i},\ t_{i + 1}\rbrack`$, avec
> $`i\  \in \ \left. ⟦0,\left. \ N - 1 \right.⟧ \right.\`$. On a donc
> $`h\  = \ \frac{T}{N}`$

- Recherche de la solution

> On cherche $`y(t_{i})`$ pour chaque valeur de $`t_{i}`$ (approximation
> par discrétisation). Plus on prendra de valeurs pour $`t_{i}`$, plus
> on aura de points pour tracer la courbe représentative de $`y(t)`$ et
> plus la représentation graphique sera précise.
>
> On va donc faire tendre $`N`$ vers $`+ \infty`$ et donc
> $`h\  = \ \frac{T}{N}\`$vers 0.
>
> On va faire un développement limité de :

- $`y\left( t_{i + 1} \right) = y\left( t_{i} + h \right)`$ à l’ordre 1
  au voisinage de $`h = 0\`$:

> 
> ``` math
> y(t_{i + 1}) = y(t_{i} + h) = y(t_{i}) + hy'(t_{i}) + o(h)
> ```

- $`y'\left( t_{i + 1} \right) = y'\left( t_{i} + h \right)`$ à l’ordre
  1 au voisinage de $`h = 0\`$:

> 
> ``` math
> y'\left( t_{i + 1} \right) = y'\left( t_{i} + h \right) = y'\left( t_{i} \right) + hy^{''}\left( t_{i} \right) + o(h)
> ```

On a :

> 
> ``` math
> \left\{ \begin{array}{r}
> y(t_{i + 1}) = y(t_{i}) + hy'(t_{i}) + o(h) \\
> y'\left( t_{i + 1} \right) = y'\left( t_{i} \right) + hy^{''}\left( t_{i} \right) + o(h)
> \end{array} \right.\ 
> ```
>
> Or l’équation différentielle *(E)* prise en $`t = t_{i}`$ nous donne :
>
> ``` math
> y''(t_{i}) = F(t_{i},y(t_{i}),y'(t_{i}))
> ```

On a donc :

> 
> ``` math
> \left\{ \begin{array}{r}
> y(t_{i + 1}) = y(t_{i}) + hy'(t_{i}) + o(h) \\
> y'\left( t_{i + 1} \right) = y'\left( t_{i} \right) + hF(t_{i},y(t_{i}),y'(t_{i})) + o(h)
> \end{array} \right.\ 
> ```
>
> En négligeant $`o(h)`$, on a :
>
> $`\left\{ \begin{array}{r}
> y(t_{i + 1}) = y(t_{i}) + hy'(t_{i}) \\
> y'\left( t_{i + 1} \right) = y'\left( t_{i} \right) + hF(t_{i},y(t_{i}),y'{(t}_{i}))
> \end{array} \right.\`$
>
> Posons $`y(t_{i}) = u_{i}`$ et $`y'(t_{i}) = v_{i}`$.
>
> On a donc la relation de récurrence suivante :
>
> $`\left\{ \begin{array}{r}
> u_{i + 1}\  = \ u_{i} + hv_{i} \\
> v_{i + 1} = v_{i} + hF(t_{i,\ }u_{i},v_{i})
> \end{array} \right.\`$
>
> Comme les conditions initiales nous donnent $`u_{0}`$ et $`v_{0}`$, on
> peut calculer $`u_{1},\ u_{2},\ ...,\ u_{N}`$ et
> $`v_{1},\ v_{2},\ ...,\ v_{N}`$.

5.  Travail à effectuer

> On considère l’équation différentielle :
>
> $`y''(t) + 3y'(t) + 2y(t) = e^{t}`$ *(E)*
>
> sur $`I = \lbrack 0,1\rbrack`$, avec les conditions initiales
> $`y(0) = 1`$ et $`y'(0) = 0`$.

- **Question 1** : On va résoudre *(E)* de manière exacte.

  1)  Donner la solution exacte de *(E)*

  2)  Calculer $`y(t)\`$ et $`y'(t)\`$pour $`t_{0} = 0`$* *et
      $`t_{1} = 0.1`$

> (On arrondira les résultats au centième).

- **Question 2** : On va résoudre *(E)* en utilisant la méthode de
  Euler.

  1)  Donner $`F(t_{i},\ y(t_{i}),\ y'(t_{i}))`$

  2)  En posant $`y\left( t_{i} \right) = \ u_{i\ }`$et
      $`y'\left( t_{i} \right) = \ v_{i}`$, en déduire les relations de
      récurrence donnant $`u_{i + 1}`$ et $`v_{i + 1}`$.

  3)  En prenant $`h = 0.1`$ , calculer $`u_{0}`$ , $`v_{0}`$
      ,$`\ u_{1}`$ , $`v_{1}`$

- **Question 3** : Comparer les valeurs calculées avec chacune des
  méthodes.
