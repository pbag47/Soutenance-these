---
theme: seriph
layout: image
image: "/images/Arriere_plan_dimmed.jfif"
title: Réduction active de bruit
level: 1
---


<!--  Titres -->
<div class="flex gap-10 w-full items-baseline">
<div class="flex-col">

# Introduction

</div>
<div class="flex-col w-full text-center">

## Réduction active de bruit (ANC)

</div>
</div>
<!-- Fin Titres -->


<!-- Casques, champ proche -->
<div
v-click
class="flex flex-col gap-5 transition-all duration-1000 ease-out text-center bg-black/25 border border-white rounded"
  :class="$slidev.nav.clicks === 0
    ? 'absolute left-10 right-10 top-40 h-1/2 bg-black/99 z-10' 
    : ($slidev.nav.clicks === 4
        ? 'absolute top-30 left-10 right-1/2 h-1/3 z-0'
        : 'absolute top-30 left-10 right-1/2 h-1/3 z-0 opacity-20')"
>
    <h4> Contrôle local autour d'un récepteur acoustique </h4>
    <div class="flex min-h-0">
        <div class="flex flex-col w-[50%] items-center">
            <img 
            src="/images/casque-anti-bruit.png"
            class= "object-contain min-h-0"
            />
            Casques anti-bruit actifs
        </div>
        <div class="flex flex-col w-[50%] items-center">
            <img 
            src="/images/ecouteurs-anc.jpg"
            class= "object-contain min-h-0"
            />
            Ecouteurs ANC
        </div>
    </div>
</div>


<!-- Habitacles, cavités -->
<div
v-click
class="absolute top-30 flex-col gap-5 transition-all duration-1000 ease-out text-center bg-black/25 border border-white rounded"
    :class="$slidev.nav.clicks === 1
        ? 'flex left-10 right-10 h-1/2 bg-black/99 z-10' 
        : 'flex left-1/2 right-10 h-1/3 z-0 opacity-20'"
>
    <h4> Contrôle global dans des cavités </h4>
    <div class="flex min-h-0 w-full justify-center">
        <div class="flex flex-col w-[50%] items-center">
            <img src="/images/saab_340B.jpeg" class="object-contain min-h-0" />
            Habitacles
        </div>
        <div class="flex flex-col w-[50%] items-center">
            <img src="/images/salle-anechoique.jpg" class="object-contain min-h-0" />
            Salles
        </div>
    </div>
</div>


<!-- Conduits -->
<div
v-click
class="absolute top-30 flex-col gap-5 transition-all duration-1000 ease-out text-center bg-black/25 border border-white rounded"
    :class="$slidev.nav.clicks === 2
        ? 'flex left-10 right-10 h-1/2 bg-black/99 z-10' 
        : 'flex left-10 right-1/2 top-76 h-1/3 z-0 opacity-20'"
>
    <h4> Contrôle dans des conduits </h4>
    <div class="flex min-h-0 w-full justify-center">
        <div class="flex flex-col w-[50%] items-center">
            <img src="/images/ventilation.jfif" class="object-contain min-h-0" />
            Ventilation
        </div>
        <div class="flex flex-col w-[50%] items-center">
            <img src="/images/echappement.jpg" class="object-contain min-h-0" />
            Echappement
        </div>
    </div>
</div>


<!-- Source -->
<div
v-click
class="absolute top-30 flex-col gap-5 transition-all duration-1000 ease-out text-center bg-black/25 border border-white rounded"
    :class="$slidev.nav.clicks === 3
        ? 'flex left-10 right-10 h-1/2 bg-black/99 z-10' 
        : 'flex left-1/2 right-10 top-76 h-1/3 z-0 opacity-20'"
>
    <h4> Contrôle autour d'une source de bruit </h4>
    <div class="flex min-h-0 w-full justify-center">
        <div class="flex flex-col w-[50%] items-center">
            <!-- <img src="/images/ventilation.jfif" class="object-contain min-h-0" />
            Ventilation -->
        </div>
        <div class="flex flex-col w-[50%] items-center">
            <!-- <img src="/images/echappement.jpg" class="object-contain min-h-0" />
            Echappement -->
        </div>
    </div>
</div>
