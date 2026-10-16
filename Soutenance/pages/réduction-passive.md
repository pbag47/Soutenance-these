---
theme: seriph
layout: image
image: "/images/Arriere_plan_dimmed.png"
title: Discrétion acoustique
level: 2
---

<!--  Titres -->
<div class="flex gap-10 w-full items-baseline">
<div class="flex-col">

# Introduction

</div>
<div class="flex-col w-full text-center">

## Moyens de réduction du bruit

</div>
</div>


<!-- Réduction passive de bruit -->
<div
  v-motion
  :enter="{ x: 0, y: 100 }"
  :click-1="{ x: 0, y: 0 }"
>
    <div class="flex items-center justify-center w-full gap-40 text-center">
        <div class="flex flex-col">
            <img src="/images/pales_profilees.jfif" class="h-40" />
            Forme et matériau des hélices
        </div>
        <div class="flex flex-col">
            <img src="/images/hélices carénées.png" class="h-40" />
            Carénages
        </div>
    </div>
</div>


<!-- Réduction active embarquée pour effacer le bruit du drone sur un enregistrement audio -->
<div
  v-motion v-click
  :initial="{ x: 0,  y: 200 }"
  :enter="{ x: 0, y: 10 }"
>
    <div class="flex justify-center items-center w-full text-center flex-col">
        <img src="/images/Dotterel.png" class="h-50" />
        Dotterel Technologies : effacer le bruit du drone sur un enregistrement audio
    </div>
</div>


<!-- Numéro de diapositive -->
<div class="text text-right absolute bottom-5 right-5">
    <SlideCurrentNo />
</div>
