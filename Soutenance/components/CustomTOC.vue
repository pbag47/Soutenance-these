<!-- components/CustomTOC.vue -->

<template>
    <div v-for="s in validSlides" :key="s.no">
        <span 
            v-if="s.meta?.slide?.frontmatter?.title && s.meta?.slide?.frontmatter?.level === 1"
            class="toc-item"
            :class="{ 'toc-item--active': isActive(s) }"
        >
            {{ s.meta.slide.frontmatter.title }}
        </span>
    </div>
</template>


<script setup>
import { computed } from 'vue'
import { useNav } from '@slidev/client'


const { slides } = useNav()

const validSlides = computed(() => {
  return Array.from(slides.value).filter(s => s.meta.slide.frontmatter.title)
})

const currentActiveSectionNo = computed(() => {
  const current = $slidev.nav.currentPage 
  
  // Extrait uniquement les numéros des slides-titres
  const sectionNumbers = validSlides.value.map(s => s.no)

  // Trouve le numéro de section le plus proche (inférieur ou égal à la slide actuelle)
  const activeNo = [...sectionNumbers]
    .reverse()
    .find(no => no <= current)
    
  return activeNo
})

function getTitleBySlideNo(slideNo) {
  // On cherche la slide qui a le bon numéro
  const targetSlide = $slidev.nav.slides.find(s => s.no === slideNo)
  
  // On retourne son titre s'il existe, sinon une chaîne vide
  return targetSlide?.meta?.slide?.frontmatter?.title || ''
}

// Une entrée est active si son titre correspond à la section en cours
function isActive(s) {
  return getTitleBySlideNo(currentActiveSectionNo.value) === s.meta?.slide?.frontmatter?.title
}
</script>


<style scoped>
/* Seules les couleurs, ombres et fonds changent : police, graisse de base,
   épaisseur de bordure (2px) et position restent identiques à l'original. */
.toc-item {
    color: #8497b0;
    font-weight: 400;
    border-left: 2px solid transparent;
    transition: color 0.25s ease, border-color 0.25s ease, background-size 0.25s ease;
}

.toc-item--active {
    color: #ffffff;
    font-weight: 600;
    border-left-color: #5ecfe0;
    background-image: linear-gradient(90deg, rgba(94, 207, 224, 0.18), rgba(94, 207, 224, 0));
    text-shadow: 0 0 10px rgba(94, 207, 224, 0.35);
}
</style>
