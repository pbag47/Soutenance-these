---
title: -- RLS projeté
level: 1
---


# Projection dans une autre base

<div class="flex items-baseline gap-10">

Algorithme RLS

$$
\boldsymbol{H}_n = \boldsymbol{H}_{n-1} + (1-\beta) e_n  \hat{\mathbf{R}}_n^{-1} \boldsymbol{X}_n
$$

</div>

<Arrow 
    x1="30%" y1="25%" 
    x2="30%" y2="60%" 
    width="3" 
    color="orange"
    z="60"
/>

<div class="absolute top-27% left-32% gap-0 border border-white px-5">

$\mathbf{P}$ : matrice unitaire arbitraire

<div class="flex justify-start -mt-6">

$$
\begin{align}
    \nonumber \hat{\mathbf{\Omega}}_n &= \mathbf{P} \hat{\mathbf{R}}_n \mathbf{P}^{-1} \\
    \nonumber \boldsymbol{H}_n' &= \mathbf{P} \boldsymbol{H}_n \\ 
    \nonumber \boldsymbol{X}_n' &= \mathbf{P} \boldsymbol{X}_n
\end{align}
$$
</div>
</div>

<div class="absolute top-60% flex items-baseline gap-10">
Algorithme RLS projeté

$$
\boldsymbol{H}_n' = \boldsymbol{H}_{n-1}' + (1-\beta) e_n  \hat{\mathbf{\Omega}}_n^{-1} \boldsymbol{X}_n'
$$
</div>

<div class="absolute top-70%">

Lorsque $\hat{\mathbf{\Omega}}_n$ est diagonale, son inversion n'est plus un défi

<div class="flex gap-10 items-baseline">
<div>

Quelle matrice $\mathbf{P}$ permet de diagonaliser $\hat{\mathbf{\Omega}}_n$ ?
</div>
<div v-click>

Dépend du signal de référence
</div>
</div>
</div>
