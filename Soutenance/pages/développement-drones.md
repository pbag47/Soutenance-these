---
theme: seriph
layout: image
image: "/images/Arriere_plan_dimmed.png"
title: Introduction
---

# Introduction

<div class="absolute top-40 left-10 right-10">

|       | Au 01/01/2024 | Au 31/12/2024   | Évolution |
| :---  | ---: | ---: | ---: |
| **Drones enregistrés en France** | $320 \, 814$ | $387 \, 260$ | $+\ 21\,\%$ |
| **Exploitants professionnels de drones en France**| $16 \, 232$ | $18 \, 191$ | $+ \ 12\,\%$ | 

</div>

<!-- $+ \ 66  \, 446$   $+ \ 1 \, 959$ -->


<div class="text-center absolute bottom-5 w-full">

Sources : [rapport d'activité 2024 de la DSAC](https://salledelecture-ext.aviation-civile.gouv.fr/externe/DSAC/Rapport_activite_2024_DSAC.pdf)

</div>


<div
    class="absolute top-30 left-0 w-full flex justify-center items-center"
    v-motion v-click
    :initial="{ x: 0,  y: 100 }"
    :enter="{ x: 0, y: 0 }"
>
    <img src="/images/Applications drones.png" class="h-100 object-contain"/>
</div>

<!-- Numéro de diapositive -->
<div class="text-right absolute bottom-5 right-5">
    <SlideCurrentNo />
</div>