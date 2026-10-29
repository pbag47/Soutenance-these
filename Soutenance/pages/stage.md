---
title: Premiers essais
level: 1
---

# Premiers essais expérimentaux

<div class="flex flex-col h-[calc(100%-3rem)] w-full gap-4 relative">
    <div class="flex-1 min-h-0"> 
        <div class="flex justify-center gap-4 h-full max-h-full">
            <img
                src="/images/Manip_stage.png"
                class="object-contain rounded border border-white bg-white/85% backdrop-blur max-h-full max-w-48%"
            />
            <img
                src="/images/Attenuation_stage_dark.png"
                class="object-contain rounded border border-white-1 max-h-full max-w-48%"
            />
        </div>
    </div>
    <div class="flex-1 min-h-0 flex justify-center">
        <img
            src="/images/Architecture feedforward.png"
            class="object-contain bg-white/85 backdrop-blur h-225px max-h-full rounded border border-white"
        />
    </div>
    <v-click>
        <Arrow 
            x1="35%" y1="78%" 
            x2="40%" y2="40%" 
            width="3" 
            color="orange"
            z="60"
        />
        <div class="absolute w-60% top-0% left-50% -translate-x-1/2 z-50">
            <img 
                src="/images/Filtre FIR adaptatif.png"
                class="object-contain bg-white/85 backdrop-blur mx-auto border-2 border-orange-400 rounded-lg shadow-2xl"
            />
        </div>
    </v-click>
</div>
