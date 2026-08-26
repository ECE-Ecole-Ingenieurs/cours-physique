# Travail préliminaire

## Question 1 :

> **def** produit_matriciel **(**A**,** B**):**
>
> m **=** A**.***shape***\[**0**\]**
>
> n **=** A**.***shape***\[**1**\]**
>
> C **=** np**.***zeros***(**n**)**
>
> **for** i **in** **range(**0**,** m**):**
>
> **sum** **=** 0
>
> **for** j **in** **range(**0**,** n**):**
>
> **sum** **+=** A**\[**i**\]\[**j**\]\***B**\[**j**\]**
>
> C**\[**i**\]** **=** **sum**
>
> **return** C

# Mise en équation

## Question 2 :

On voit d’abord directement que $`v_{1} = E_{1} = 2,5\ V`$.

<img src="media/media/image1.png"
style="width:2.94309in;height:1.75624in"
alt="Une image contenant noir, obscurité Description générée automatiquement" />

On commence par associer les résistances R3 et R4 en parallèle :

``` math
R_{3} \parallel R_{4} = \frac{R_{3}R_{4}}{R_{3} + R_{4}} = \frac{5000 \times 10000}{5000 + 10000} = 3,\overline{3}\ k\Omega
```

<img src="media/media/image2.png"
style="width:2.51688in;height:1.79245in" />

D’après la règle du pont diviseur de tension, on va avoir :

``` math
v_{2} = \frac{R_{3} \parallel R_{4}}{R_{3} \parallel R_{4} + R2}v_{1} = \frac{3,\overline{3}}{4,\overline{3}} \times 2,5 \approx 1,923\ V
```

On peut ensuite calculer les courants par la loi d’Ohm :

``` math
v_{1} - v_{2} = R_{2}i_{2} \Rightarrow i_{2} = \frac{v_{1} - v_{2}}{R_{2}} \approx 577\ µA
```

``` math
v_{2} = R_{3}i_{3} \Rightarrow i_{3} = \frac{v_{2}}{R_{3}} \approx 385\ µA
```

``` math
v_{2} = R_{4}i_{4} \Rightarrow i_{4} = \frac{v_{2}}{R_{4}} \approx 192\ µA
```

On obtient donc le vecteur suivant :

``` math
X = \begin{pmatrix}
i_{1} \\
i_{2} \\
i_{3} \\
i_{4} \\
v_{1} \\
v_{2}
\end{pmatrix} \approx \begin{pmatrix}
577 \times 10^{- 6} \\
577 \times 10^{- 6} \\
385 \times 10^{- 6} \\
192 \times 10^{- 6} \\
2,5 \\
1,923
\end{pmatrix}
```

## Question 3 :

$`A = \begin{pmatrix}
0 & 0 & 0 & 0 & 1 & 0 \\
0 & - 1000 & 0 & 0 & 1 & - 1 \\
0 & 0 & - 5000 & 0 & 0 & 1 \\
0 & 0 & 0 & - 10000 & 0 & 1 \\
 \vdots & \vdots & \vdots & \vdots & \vdots & \vdots 
\end{pmatrix}`$ $`B = \begin{pmatrix}
2,5 \\
0 \\
0 \\
0 \\
 \vdots 
\end{pmatrix}`$

## Question 4 :

$`A = \begin{pmatrix}
 \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
1 & - 1 & 0 & 0 & 0 & 0 \\
0 & 1 & - 1 & - 1 & 0 & 0
\end{pmatrix}`$ $`B = \begin{pmatrix}
 \vdots \\
0 \\
0
\end{pmatrix}`$

# Travail à effectuer

## Question 5 :

> **import** numpy **as** np
>
> A **=** np**.***array***(\[\[**0**,** 0**,** 0**,** 0**,** 1**,**
> 0**\],**
>
> **\[**0**,** **-**1000**,** 0**,** 0**,** 1**,** **-**1**\],**
>
> **\[**0**,** 0**,** **-**5000**,** 0**,** 0**,** 1**\],**
>
> **\[**0**,** 0**,** 0**,** **-**10000**,** 0**,** 1**\],**
>
> **\[**1**,** **-**1**,** 0**,** 0**,** 0**,** 0**\],**
>
> **\[**0**,** 1**,** **-**1**,** **-**1**,** 0**,** 0**\]\])**
>
> B **=** np**.***array***(\[**2.5**,** 0**,** 0**,** 0**,** 0**,**
> 0**\])**
>
> \# On récupère la taille de la matrice A
>
> m **=** A**.***shape***\[**0**\]**
>
> \# On adjoint à A une matrice identité de même taille
>
> G **=** np**.***concatenate***((**A**,** np**.***eye***(**m**)),**
> axis**=**1**)**

## Question 6 :

> \# On parcourt les m premières colonnes de la matrice
>
> \# en itérant sur la transposée
>
> **for** pivot_column**,** column **in**
> **enumerate(**G**.***T***\[:**m**\]):**
>
> \# On liste les éléments non nuls de la colonne
>
> \# dans les lignes de numéro supérieur ou égal
>
> \# au numéro de colonne
>
> nonzero **=** column**\[**pivot_column**:\].***nonzero***()\[**0**\]**

## Question  :

> **if** nonzero**.***size* **!=** 0**:**
>
> \# S'il reste des éléments non nuls,
>
> \# alors on prend le premier comme pivot
>
> pivot_line **=** nonzero**\[**0**\]+**pivot_column
>
> pivot **=** G**\[**pivot_line**,** pivot_column**\]**
>
> **else:**
>
> \# S'il ne reste que des éléments nuls,
>
> \# alors c'est que la matrice n'est pas inversible
>
> **print(**"Matrice non inversible"**)**
>
> **break**
>
> \# On échange la ligne du pivot avec la ligne
>
> \# de même numéro que la colonne en cours de traitement
>
> G**\[\[**pivot_column**,** pivot_line**\]\]** **=**
> G**\[\[**pivot_line**,** pivot_column**\]\]**
>
> pivot_line **=** pivot_column
>
> \# On divise la ligne du pivot par la valeur du pivot
>
> G**\[**pivot_line**\]** **=** G**\[**pivot_line**\]** **/** pivot
>
> \# On parcourt la colonne sous le pivot
>
> \# pour faire apparaître des 0
>
> **for** index **in** **range(**pivot_column**+**1**,** m**):**
>
> \# On soustrait un multiple de la ligne du pivot
>
> \# pour faire apparaître un 0
>
> G**\[**index**\]** **=** G**\[**index**\]** **-**
> G**\[**index**\]\[**pivot_column**\]** **\*** G**\[**pivot_line**\]**

## Question  :

> \# On parcourt les colonnes à l'envers
>
> **for** column **in** **range(**m**-**1**,** **-**1**,** **-**1**):**
>
> \# On parcourt la colonne au-dessus du pivot
>
> **for** line **in** **range(**column**):**
>
> \# On soustrait un multiple de la ligne du pivot
>
> \# pour faire apparaître un 0
>
> G**\[**line**\]** **=** G**\[**line**\]** **-**
> G**\[**line**\]\[**column**\]** **\*** G**\[**column**\]**

## Question 9 :

> \# On récupère les n dernières colonnes de notre matrice,
>
> \# c'est là que se trouve l'inverse de A
>
> inverted **=** G**\[:,**m**:\]**
>
> X **=** produit_matriciel**(**inverted**,** B**)**

Les valeurs obtenues par le pivot de Gauss sont identiques à celle
obtenues de façon analytique.
