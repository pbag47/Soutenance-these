---
title: TDLMS
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
    x1="30%" y1="25%" 
    x2="30%" y2="85%" 
    width="3" 
    color="orange"
    z="60"
/>

<div class="absolute left-32% top-25% justify-start">

Choix d'une base constante comme substitut à la base des vecteurs propres de $\hat{\mathbf{R}}_n$

$\hat{\mathbf{\Omega}}_n^{-1}$ rendue artificiellement diagonale

$$
\begin{align}
    \nonumber \mathbf{\Omega}_n &= \begin{bmatrix}
    \mathbb{E}\{ x_n' x_n' \} & \mathbb{E}\{ x_n' x_{n-1}'\} & \cdots & \mathbb{E}\{ x_n' x_{n-L+1}' \} \\
    \mathbb{E}\{ x_n' x_{n-1}' \} & \mathbb{E}\{ x_{n-1}' x_{n-1}'\} & \cdots & \mathbb{E}\{ x_{n-1}' x_{n-L+1}' \} \\
    \vdots & \vdots & \ddots & \vdots \\
    \mathbb{E}\{ x_{n}' x_{n-L+1}' \} & \mathbb{E}\{ x_{n-1}' x_{n-L+1}'\} & \cdots & \mathbb{E}\{ x_{n-L+1}' x_{n-L+1}' \}
\end{bmatrix}
% \nonumber \mathbf{\Omega}_n^{-1} &\approx \begin{bmatrix}
%     \mathbb{E}\{ x_n' x_n' \} & 0 & \cdots & 0 \\
%     0 & \mathbb{E}\{ x_{n-1}' x_{n-1}'\} & \cdots & 0 \\
%     \vdots & \vdots & \ddots & \vdots \\
%     0 & 0 & \cdots & \mathbb{E}\{ x_{n-L+1}' x_{n-L+1}' \}
% \end{bmatrix}
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
