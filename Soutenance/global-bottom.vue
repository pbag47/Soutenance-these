<script setup>
</script>


<template>
    <img 
        v-if="$nav.currentPage !== 1" 
        src="/images/Arriere_plan_dimmed.jfif" 
        class="absolute inset-0 -z-10 pointer-events-none w-full h-full object-cover object-center" 
        alt="Background"
    />
    <div v-if="$nav.currentPage !== 1">
        <!-- Bandeau gauche : sommaire (dimensions inchangées : w-5cm, p-5) -->
        <div class="gb-sidebar absolute left-0 top-0 h-full w-5cm border text-white p-5 z-50">
            <h1 class="gb-sidebar-title font-bold mb-4">Sommaire</h1>
            <CustomTOC/>
        </div>
        <!-- Bandeau bas : mentions + numéro (dimensions inchangées : h-0.5cm, p-0.5) -->
        <div class="gb-footer absolute flex left-5cm bottom-0 right-0 h-0.5cm border-t p-0.5 justify-between z-0">
            <p class="gb-footer-info text-xs font-mono">02/11/2026 - Pierre BAGNARA</p>
            <div class="gb-footer-page text-xs font-mono">
                {{ $slidev.nav.currentPage }} 
            </div>
        </div>
    </div>
</template>


<style scoped>
/* ------------------------------------------------------------------
   Palette (accordée au fond bleu nuit)
   --navy-deep : fond des bandeaux, légèrement translucide
   --cyan      : accent principal (sommaire actif, filets)
   --gold      : accent secondaire (numéro de diapositive, liseré)
   --muted     : texte secondaire
------------------------------------------------------------------- */
.gb-sidebar,
.gb-footer {
    --navy-deep: 7, 15, 29;
    --cyan: 94, 207, 224;
    --gold: 224, 183, 108;
    --muted: #9fb1c7;
}

/* ---------- Bandeau gauche ---------- */
.gb-sidebar {
    background:
        linear-gradient(180deg, rgba(var(--navy-deep), 0.94) 0%, rgba(5, 11, 22, 0.97) 100%);
    border-color: rgba(var(--cyan), 0.16);
    box-shadow:
        inset -1px 0 0 rgba(var(--cyan), 0.10),
        4px 0 18px rgba(0, 0, 0, 0.35);
    -webkit-backdrop-filter: blur(6px);
    backdrop-filter: blur(6px);
}

/* Liseré doré discret en haut du bandeau (décoratif, hors flux) */
.gb-sidebar::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, rgba(var(--gold), 0.9), rgba(var(--gold), 0) 85%);
    pointer-events: none;
}

/* Titre "Sommaire" : soulignement dégradé tracé en fond (aucun impact sur la mise en page) */
.gb-sidebar-title {
    color: #f1f5f9;
    background-image: linear-gradient(90deg, rgba(var(--cyan), 0.75), rgba(var(--cyan), 0));
    background-repeat: no-repeat;
    background-position: left bottom;
    background-size: 100% 1px;
}

/* ---------- Bandeau bas ---------- */
.gb-footer {
    background: rgba(var(--navy-deep), 0.90);
    border-color: rgba(var(--cyan), 0.16);
    box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.30);
    -webkit-backdrop-filter: blur(6px);
    backdrop-filter: blur(6px);
}

/* Filet lumineux doré qui s'estompe vers la droite */
.gb-footer::before {
    content: "";
    position: absolute;
    top: -1px;
    left: 0;
    width: 40%;
    height: 2px;
    background: linear-gradient(90deg, rgba(var(--gold), 0.85), rgba(var(--gold), 0));
    pointer-events: none;
}

.gb-footer-info {
    color: var(--muted);
}

.gb-footer-page {
    color: rgb(var(--muted));
}
</style>
