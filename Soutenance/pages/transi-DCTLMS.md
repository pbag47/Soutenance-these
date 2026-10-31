---
title: Raisonnement
level: 2
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
            class="absolute right-0% w-22% h-56% top-45% border-2 border-green-500 bg-green-500/10 rounded z-10">
        </div>
        <!-- Flou -->
        <div
            v-motion
            :initial="{ left: '50%', top: '62%', right: '22%', bottom: '0%' }"
            :enter="{ left: '50%', top: '62%', right: '22%', bottom: '0%' }"
            :click-1="{ left: '50%', top: '65%', right: '22%', bottom: '0%' }"
            :click-2="{ left: '50%', top: '99%', right: '51%', bottom: '0%' }"
            class="absolute backdrop-blur"
        >
        </div>
        <!-- Passage dévoilé (orange) -->
        <div 
            v-motion
            :initial="{ left: '57%', top: '20%', width: '20%', height: '42%' }"
            :enter="{ left: '57%', top: '20%', width: '20%', height: '42%' }"
            :click-1="{ left: '57%', top: '40%', width: '40%', height: '42%' }"
            class="absolute left-0 border-2 border-orange-500 bg-orange-500/10 rounded"
        >
        </div>
    </div>
</div> 


<div v-click></div>
<div v-click></div>

