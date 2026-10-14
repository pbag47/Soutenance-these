---
theme: seriph
layout: image
image: "/images/Arriere_plan_dimmed.png"
title: Problématique
level: 2
---


# Problématique

  <!-- :click-1="{ x: 0, y: 30 }"
  :click-2="{ y: 60 }"
  :click-2-4="{ x: 40 }" -->
<div v-motion v-click
  :initial="{ x: -80, opacity: 0 }"
  :enter="{ x: 0, y: 0, opacity: 1 }"
  :leave="{ y: 0, x: 80 }">
    test
</div>

<div
  v-motion v-click
  :initial="{ x: -80,  y: 20 }"
  :enter="{ x: 0 }"
  :click-3="{ x: 40, y: 30 }"
  :leave="{ x: 80 }"
>
  Retest
</div>

<v-click> Hello World! </v-click>

<div v-click>
  Ce texte apparaît au clic.
</div>


<!-- <div style="margin-top:55px; text-align:center; font-size:1.35em">
<strong>3 questions</strong>　→　<strong>faisabilité</strong>　·　<strong>atténuation</strong>　·　<strong>complémentarité</strong>
</div> -->

<!-- Numéro de diapositive -->
<div class="text text-right absolute bottom-5 right-5">
    <SlideCurrentNo />
</div>
