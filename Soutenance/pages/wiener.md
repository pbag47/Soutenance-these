---
title: -- Filtre de Wiener
level: 1
---

# Filtre de Wiener

Solution de la méthode des moindres carrés pour l'erreur $e_n$
$$
    \boldsymbol{H}_n = \mathbf{R}_n^{-1} \boldsymbol{C}_n
$$

$$
    \begin{align}
        \nonumber \mathbf{R}_n &= \mathbb{E} \{ \boldsymbol{X}_n \boldsymbol{X}_n^t \} && \text{Matrice d'autocorrélation du signal de référence} \\
        \nonumber \boldsymbol{C}_n &= \mathbb{E} \{ d_n \boldsymbol{X}_n \} && \text{Corrélation entre le signal désiré et le signal de référence}
    \end{align}
$$

<div class="flex justify-start gap-10 items-baseline">
<div>
Problème : comment déterminer l'espérance ?
</div>
<div>

- Mesures limitées
- Mémoire limitée
- Vitesse de calcul limitée

</div>
</div>

Recours à un estimateur récursif avec $\beta \in \mathopen] 0 ; 1 \mathclose[$ :
<div class="flex flex-col gap-0">
<div class="flex justify-center -mt-6">

$$
    \begin{align}
        \nonumber \hat{s}_n &= \frac{1}{\sum_{j=0}^{n-1} \beta^j} \sum_{k=0}^{n-1} \beta^{k} s_{n-k} \\
        \nonumber \hat{s}_n &= (1-\beta) s_n + \beta \hat{s}_{n-1}
        % \nonumber &\mathbb{E} \{ s_n \} \approx  \hat{s}_n
    \end{align}
$$
</div>
<div class="flex justify-center -mt-6">

$$ 
\mathbb{E} \{ s_n \} \approx  \hat{s}_n
$$
</div>
</div>