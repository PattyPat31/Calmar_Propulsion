# Ossature de script Python pour projet L1
-------------------------------------------
propulsion méduses, poulpes, etc...
-------------------------------------------

### <span style="color:gray">Méthode d’Euler explicite

#### <span style="color:gray">Objectif

<span style="color:gray">
Nous voulons résoudre numériquement l’équation du mouvement :

$$
m \frac{dv}{dt} = \sum F
$$

ou encore :

$$
\frac{dv}{dt} = a
$$

où :
- $v$ est la vitesse,
- $a$ est l’accélération.

L’idée est de calculer progressivement :
- la vitesse,
- puis la position,
à chaque instant.

---

### <span style="color:gray">Principe de la méthode d’Euler

<span style="color:gray">
On découpe le temps en petits intervalles :

$$
dt
$$

À chaque étape :
1. on calcule l’accélération,
2. on met à jour la vitesse,
3. puis la position.

---

### <span style="color:gray">Mise à jour de la vitesse

<span style="color:gray">
On utilise l’approximation :

$$
\frac{dv}{dt} \approx \frac{v_{n+1} - v_n}{dt}
$$

ce qui donne :

$$
v_{n+1} = v_n + a_n \, dt
$$

---

### <span style="color:gray">Mise à jour de la position

<span style="color:gray">
De la même manière :

$$
\frac{dz}{dt} \approx \frac{z_{n+1} - z_n}{dt}
$$

d’où :

$$
z_{n+1} = z_n + v_n \, dt
$$

---

### <span style="color:gray">Interprétation physique

<span style="color:gray">
Pendant un petit temps $dt$ :
- on suppose l’accélération constante,
- puis on avance le système d’un petit pas.

Plus $dt$ est petit :
- plus la simulation est précise,
- mais plus le calcul est long.

---

### <span style="color:gray">Remarque

<span style="color:gray">
La méthode d’Euler est :
- simple,
- rapide,
- très utilisée pour découvrir les simulations numériques.

Mais elle peut devenir imprécise si :
- le pas de temps est trop grand,
- ou si les accélérations varient très rapidement.
  
- le pas de temps est trop grand,
- ou si les accélérations varient très rapidement.
</span>
