---
title: Introduction
level: 2
---


# Introduction

<div class="relative top-5% 1fr pb-16">
    <div class="relative w-fit">
        <!-- Spectre -->
        <img 
            src="/images/UAV_noise_spectrum_dark.png"
            class="object-contain rounded border border-white-1"
        />
        <!-- Encadré orange -->
        <div 
            v-click
            v-motion
            :initial="{ left: '0%', top: '15%', width: '5%', height: '5%' }"
            :enter="{ left: '50%', top: '15%', width: '45%', height: '65%' }"
            :click-1="{ left: '50%', top: '15%', width: '45%', height: '65%' }"
            :click-2="{ left: '25%', top: '15%', width: '30%', height: '65%' }"
            class="absolute left-0 border-2 border-orange-500 bg-orange-500/10 rounded"
        >
        </div>
    </div>
    <!-- Images réduction passive -->
    <div
        v-after
        v-click.hide
        v-if="$clicks >= 1 && $clicks < 2" 
        class="absolute top-10% left-15% z-10"
    >
        <img
            src="/images/pales_profilees.jfif"
            class="w-60 h-auto" 
        />
        <img 
            src="/images/hélices carénées.png" 
            class="w-60 h-auto" 
        />
    </div>
    <!-- Image réduction active -->
    <div
        v-click
        class="absolute top-15% right-10% z-10"
    >
        <img
            src="/images/anc-principe.webp"
            class="w-60 h-auto bg-white/75 backdrop-blur rounded" 
        />
    </div>
</div>

