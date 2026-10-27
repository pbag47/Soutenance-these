
<!-- components/CustomTOC.vue -->
<template>
    <div v-for="s in validSlides" :key="s.no">
        <span 
            v-if="s.meta?.slide?.frontmatter?.title && s.meta?.slide?.frontmatter?.level === 1"
            :style="{
                color: getTitleBySlideNo(currentActiveSectionNo) === s.meta?.slide?.frontmatter?.title ? 'white' : 'gray',
                fontWeight: getTitleBySlideNo(currentActiveSectionNo) === s.meta?.slide?.frontmatter?.title ? '600' : '400',
                borderLeft: getTitleBySlideNo(currentActiveSectionNo) === s.meta?.slide?.frontmatter?.title ? '2px solid #34d399' : '2px solid transparent'
            }"
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
</script>





<!-- components/MonSommairePerso.vue -->
<!-- <template>
  <ul>
    <li 
      v-for="slide in validSlides" 
      :key="slide.no" 
      class="my-2 text-sm pl-2"
    >
      <span 
        @click="goTo(slide.no)" 
        class="cursor-pointer hover:text-white block w-full text-left"
        :style="{
            color: activeNo === slide.no ? '#34d399' : '#9ca3af',
            fontWeight: activeNo === slide.no ? '600' : '400',
            borderLeft: activeNo === slide.no ? '2px solid #34d399' : '2px solid transparent'
        }"
      >
        {{ slide.frontmatter?.title }}
      </span>
    </li>
  </ul>
</template>

<script setup>
import { computed } from 'vue'
import { useNav } from '@slidev/client'

// Utilisation des hooks officiels réactifs de Slidev
const { currentSlideNo, total, slides } = useNav()

const validSlides = computed(() => {
  return Array.from(slides.value).filter(s => s.frontmatter?.title)
})

const activeNo = computed(() => {
  const sectionNumbers = validSlides.value.map(s => s.no)
  return [...sectionNumbers].reverse().find(no => no <= currentSlideNo.value)
})

function goTo(pageNo) {
  console.log("Clic détecté vers la page :", pageNo)
  // Utilisation de la méthode de navigation native
  window.$slidev.nav.go(pageNo)
}
</script> -->
