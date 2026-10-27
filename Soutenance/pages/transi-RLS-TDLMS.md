---
title: Unification
level: 1
---


# Démarche

<div class="relative 1fr">
    <div class="relative w-fit">
        <img
            src="/images/Demarche.drawio.png"
            class="object-contain w-90% mx-auto"
        />
        <!-- Approche littérature (vert) -->
        <div 
            class="absolute right-0% w-22% h-62% top-40% border-2 border-green-500 bg-green-500/10 rounded z-10">
        </div>
        <!-- Flou -->
        <div
            v-motion
            :initial="{ left: '25%', top: '0%', right: '22%', height: '100%' }"
            :enter="{ left: '25%', top: '0%', right: '22%', height: '100%' }"
            :click-1="{ left: '50%', top: '62%', right: '22%', height: '25%' }"
            class="absolute backdrop-blur"
        >
        </div>
        <!-- Passage dévoilé (orange) -->
        <div 
            v-motion
            :initial="{ left: '0%', top: '0%', width: '25%', height: '40%' }"
            :enter="{ left: '0%', top: '0%', width: '25%', height: '40%' }"
            :click-1="{ left: '30%', top: '00%', width: '20%', height: '40%' }"
            :click-2="{ left: '57%', top: '20%', width: '20%', height: '42%' }"
            class="absolute left-0 border-2 border-orange-500 bg-orange-500/10 rounded"
        >
        </div>
        <div v-click></div>
        <div 
            v-click
            class="absolute top-40%"
        >

$$
\boldsymbol{H}_n = \boldsymbol{H}_{n-1} + (1-\beta) e_n  \boxed{\hat{\mathbf{R}}_n^{-1}} \boldsymbol{X}_n
$$
</div>

</div>
</div> 


