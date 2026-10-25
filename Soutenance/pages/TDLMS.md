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

Choix d'une base constante comme substitut à la base des vecteurs propres de $\hat{\mathbf{R}}_n$

$\hat{\mathbf{\Omega}}_n^{-1}$ rendue artificiellement diagonale

<div class="flex relative justify-center">
<div class="absolute top-0">

$$
\begin{align}
\nonumber \mathbf{\Omega}_n^{-1} &= \begin{bmatrix}
    \mathbb{E}\{ x_n' x_n' \} & \mathbb{E}\{ x_n' x_{n-1}'\} & \cdots & \mathbb{E}\{ x_n' x_{n-L+1}' \} \\
    \mathbb{E}\{ x_n' x_{n-1}' \} & \mathbb{E}\{ x_{n-1}' x_{n-1}'\} & \cdots & \mathbb{E}\{ x_{n-1}' x_{n-L+2}' \} \\
    \vdots & \vdots & \ddots & \vdots \\
    \mathbb{E}\{ x_{n}' x_{n-L+1}' \} & \mathbb{E}\{ x_{n-1}' x_{n-L+2}'\} & \cdots & \mathbb{E}\{ x_{n-L+1}' x_{n-L+1}' \}
\end{bmatrix} \\
\nonumber \mathbf{\Omega}_n^{-1} &\approx \begin{bmatrix}
    \mathbb{E}\{ x_n' x_n' \} & 0 & \cdots & 0 \\
    0 & \mathbb{E}\{ x_{n-1}' x_{n-1}'\} & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & \mathbb{E}\{ x_{n-L+1}' x_{n-L+1}' \}
\end{bmatrix}
\end{align}
$$

</div>
</div>


