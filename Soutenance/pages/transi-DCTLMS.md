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
            :initial="{ left: '50%', top: '62%', right: '22%', bottom: '0%' }"
            :enter="{ left: '50%', top: '62%', right: '22%', bottom: '0%' }"
            :click-1="{ left: '50%', top: '99%', right: '51%', bottom: '0%' }"
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

<!-- <svg v-click class="absolute inset-0 w-full h-full pointer-events-none z-10" viewBox="0 0 800 400">
<defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="orange"/>
    </marker>
</defs>
<!-- M = Départ (X Y), Q = Point de contrôle de la courbe (X Y), puis Point d'arrivée (X Y) -->
<!-- <path d="M 120 130 Q 310 250 500 130" stroke="orange" stroke-width="3" fill="none" marker-end="url(#arrow)" />
</svg> -->

</div>
</div> 


<div v-click></div>


