---
title: -- TDLMS
level: 1
---


# TDLMS


<div class="flex items-baseline gap-10">

Algorithme RLS projeté

$$
\boldsymbol{H}_n' = \boldsymbol{H}_{n-1}' + (1-\beta) e_n  \hat{\mathbf{\Omega}}_n^{-1} \boldsymbol{X}_n'
$$
</div>

<Arrow 
    x1="25%" y1="25%" 
    x2="25%" y2="85%" 
    width="3" 
    color="orange"
    z="60"
/>

<div class="absolute left-27% top-27% justify-start border border-white px-5">

On choisit une base constante comme substitut à la base des vecteurs propres de $\hat{\mathbf{R}}_n$

$\hat{\mathbf{\Omega}}_n^{-1}$ est rendue artificiellement diagonale

$$
\begin{align}
    \nonumber \mathbf{\Omega}_n &= \begin{pmatrix}
    \mathbb{E}\{ x_n' x_n' \} & \mathbb{E}\{ x_n' x_{n-1}'\} & \cdots & \mathbb{E}\{ x_n' x_{n-L+1}' \} \\
    \mathbb{E}\{ x_n' x_{n-1}' \} & \mathbb{E}\{ x_{n-1}' x_{n-1}'\} & \cdots & \mathbb{E}\{ x_{n-1}' x_{n-L+1}' \} \\
    \vdots & \vdots & \ddots & \vdots \\
    \mathbb{E}\{ x_{n}' x_{n-L+1}' \} & \mathbb{E}\{ x_{n-1}' x_{n-L+1}'\} & \cdots & \mathbb{E}\{ x_{n-L+1}' x_{n-L+1}' \}
\end{pmatrix}
\end{align}
$$
Correction de l'erreur d'approximation par une constante multiplicative $\mu$

</div>

<div class="flex absolute bottom-5% items-baseline gap-10">
Algorithme TDLMS

$$
\boldsymbol{H}_n' = \boldsymbol{H}_{n-1}' + \boxed{\mu} e_n  \text{diag} \left( \hat{\mathbf{\Omega}}_n \right)^{-1} \boldsymbol{X}_n'
$$
</div>
