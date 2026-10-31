---
title: Raisonnement
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
            :initial="{ left: '0%', top: '0%', right: '22%', height: '100%' }"
            :enter="{ left: '0%', top: '0%', right: '22%', height: '100%' }"
            :click-1="{ left: '25%', top: '0%', right: '22%', height: '100%' }"
            class="absolute backdrop-blur"
        >
        </div>
        <!-- Passage dévoilé (orange) -->
        <div 
            v-click
            v-motion
            :initial="{ left: '0%', top: '15%', width: '5%', height: '5%' }"
            :enter="{ left: '0%', top: '15%', width: '45%', height: '65%' }"
            :click-1="{ left: '0%', top: '0%', width: '25%', height: '40%' }"
            class="absolute left-0 border-2 border-orange-500 bg-orange-500/10 rounded"
        >
        </div>
    </div>
</div>

