---
theme: seriph
title: Introduction NLMS
level: 1
---

# Algorithme NLMS


<div class="flex 1fr items-start justify-start">
<div class="flex-col w-40%">

Etudes de convergence -> Sensibilité face à l'énergie transportée par le signal de référence

Algorithme NLMS
$$
    \begin{align} 
        \nonumber w_n &= (1-\beta) \boldsymbol{X}_n^t \boldsymbol{X}_n + \beta w_{n-1} 
        \\ 
        \nonumber \boldsymbol{H}_n &= \boldsymbol{H}_{n-1} + \frac{\mu}{w_n} e_n \boldsymbol{X}_n 
    \end{align}
$$

$\mu$ borné entre $0$ et $2$

Quelle valeur choisir pour $\mu$ ?

</div>
    <div class="flex flex-col w-60% gap-2">
        <img
            src="/images/Convergence_NLMS_dark.png"
            class="object-contain rounded border border-white-1"
        />
        <img
            src="/images/Erreur_NLMS_dark.png"
            class="object-contain rounded border border-white-1"
        />
    </div>
</div>

<div
v-click
class="absolute top-10% w-50% left-5.5cm z-50 backdrop-blur text-center justify-center border border-white rounded"
>

NLMS à pas variable (VSSLMS)

<img
    src="/images/VSSLMS.drawio.png"
    class="object-contain"
/>
</div>