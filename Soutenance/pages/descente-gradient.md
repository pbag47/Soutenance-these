---
title: Introduction NLMS
level: 2
---

# Algorithme LMS


<div class="absolute w-35% right-0% top-0">
    <img 
        src="/images/Filtre FIR adaptatif.png"
        class="object-contain bg-white/85 backdrop-blur rounded border border-white"
    />
</div>

Algorithme de référence pour <br> 
la réduction active de bruit

Descente de gradient sur l'erreur quadratique $e_n^2$
<!-- 
$$
\begin{align} 
    \nonumber w_n &= (1-\beta) \boldsymbol{X}_n^t \boldsymbol{X}_n + \beta w_{n-1} 
    \\ 
    \nonumber \boldsymbol{H}_n &= \boldsymbol{H}_{n-1} + \frac{\mu}{w_n} e_n \boldsymbol{X}_n 
\end{align}
$$ 
-->


<div class="flex justify-center gap-10 text-center">
    <div class="w-25%">
        <img
            src="/images/fig_grad_error.png"
            class="object-contain rounded border border-white-1"
        />
        
$$
e_n = d_n - \boldsymbol{H}_n^t \boldsymbol{X}_n
$$ 

</div>
    <div class="w-25%">
        <img
            src="/images/fig_grad_error_squared.png"
            class="object-contain rounded border border-white-1"
        />

$$
\mathbf{\nabla} e_n^2 = - 2 e_n \boldsymbol{X}_n
$$ 

</div>
</div>

$$
\boldsymbol{H}_n = \boldsymbol{H}_{n-1} + \mu e_n \boldsymbol{X}_n 
$$ 

Quelle valeur choisir pour $\mu$ ?
