---
title: -- NLMS
level: 1
---


# NLMS


<div class="flex items-baseline gap-10">

Algorithme TDLMS

$$
\boldsymbol{H}_n' = \boldsymbol{H}_{n-1}' + \mu e_n  \text{diag} \left( \hat{\mathbf{\Omega}}_n \right)^{-1} \boldsymbol{X}_n'
$$
</div>

<Arrow 
    x1="30%" y1="25%" 
    x2="30%" y2="65%" 
    width="3" 
    color="orange"
    z="60"
/>

<div class="absolute left-32% top-30% justify-start border border-white px-5">

On choisit de rester dans la base temporelle

$$
\begin{align}
    \nonumber \mathbf{P} &= \mathbf{I} \\
    \nonumber \text{diag} \left( \hat{\mathbf{\Omega}}_n \right) &= \text{diag} \left( \hat{\mathbf{R}}_n \right) = w_n \mathbf{I}
\end{align}
$$

</div>

<div class="flex absolute top-65% items-baseline gap-10">

Algorithme NLMS

$$
\boldsymbol{H}_n = \boldsymbol{H}_{n-1} + \frac{\mu}{w_n} e_n  \boldsymbol{X}_n
$$
</div>
