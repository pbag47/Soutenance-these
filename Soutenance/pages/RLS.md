---
title: RLS
level: 1
---

# Algorithme Recursive Least Squares (RLS)

<div v-click.hide>

Estimation récursive de l'espérance appliquée au filtre de Wiener

<div class="absolute flex top-20% gap-5 items-baseline">
Filtre de Wiener

$$
\boldsymbol{H}_n = \mathbf{R}_n^{-1} \boldsymbol{C}_n
$$

</div>

<Arrow 
    x1="40%" y1="30%" 
    x2="40%" y2="60%" 
    width="3" 
    color="orange"
    z="60"
/>

<div class="absolute top-35% left-45%">

$$
\begin{align}
    \nonumber \hat{\mathbf{R}}_n &= (1-\beta) \boldsymbol{X}_n \boldsymbol{X}_n^t + \beta \hat{\mathbf{R}}_{n-1} \\
    \nonumber \hat{\boldsymbol{C}}_n &= (1-\beta) d_n \boldsymbol{X}_n + \beta \hat{\boldsymbol{C}}_{n-1}
\end{align}
$$

</div>

<div class="absolute flex top-60% items-baseline gap-5">
Algorithme RLS

$$
\boldsymbol{H}_n = \boldsymbol{H}_{n-1} + (1-\beta) e_n  \hat{\mathbf{R}}_n^{-1} \boldsymbol{X}_n
$$
</div>

</div>

<div v-after class="absolute flex top-10% 1fr gap-5 text-center">
<div class="flex flex-col w-50% gap-2 border border-white rounded">

<div>
Estimateur récursif de l'espérance

$$
\hat{s}_n = (1-\beta) s_n + \beta \hat{s}_{n-1}
$$
</div>
<img
    src="/images/Estimation_convergence_dark.png"
    class="object-contain"
/>
<img
    src="/images/Estimation_residus_dark.png"
    class="object-contain"
/>
</div>

<div class="flex flex-col w-50% gap-2 border border-white rounded">
<div>
Algorithme RLS

$$
\boldsymbol{H}_n = \boldsymbol{H}_{n-1} + (1-\beta) e_n  \mathbf{R}_n^{-1} \boldsymbol{X}_n
$$

</div>
    <img
        src="/images/RLS_convergence_dark.png"
        class="object-contain"
    />
    <img
        src="/images/RLS_residus_dark.png"
        class="object-contain"
    />
</div>
</div>
