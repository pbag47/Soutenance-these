
<template>
    <div v-if="$nav.currentPage !== 1"
        class="absolute inset-0 -z-10 pointer-events-none bg-cover bg-center"
        style="background-image: url('/images/Arriere_plan_dimmed.jfif');"
    />

    <div v-if="$nav.currentPage !== 1">
        <div class="absolute left-0 top-0 h-full w-5cm bg-gray-900 border border-gray-600 text-white p-5 z-50">
            <h1 class="font-bold mb-4">Sommaire</h1>
            <CustomTOC/>
        </div>
        <div class="absolute flex left-5cm bottom-0 right-0 h-0.5cm bg-gray-900 border-t border-gray-600 text-white p-0.5 justify-between z-0">
            <p class="text-xs font-mono">02/11/2026 - Pierre BAGNARA</p>
            <div class="text-xs text-white font-mono backdrop-blur">
                {{ $slidev.nav.currentPage }} 
            </div>
        </div>
    </div>
</template>


<script setup>
</script>
