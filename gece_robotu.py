#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gece 3'te Uyanıp Tek Kelime Söyleyen Program
Bu program varlığının tek amacı gece 03:00'te uyanmak, tek bir kelime söylemek ve tekrar uyumaktır.
Başka hiçbir şey yapmaz. Yaparsa da yalandır.
"""

import random
import time
import sys

# Absürt kelime listesi - her biri derin felsefi anlam taşır (taşımaz)
KELIMELER = [
    "Merhaba",
    "Yeter",
    "Çay",
    "Hayır",
    "Belki",
    "Asla",
    "Git",
    "Uyuyorum",
    "Neden",
    "Çünkü"
]

def uyan_ve_soyle():
    print("=" * 50)
    print("PROGRAM UYANDI (veya uyanmadı, kimse bilmiyor)")
    print("=" * 50)
    
    simdi = time.localtime()
    saat = simdi.tm_hour
    
    # Demo için her zaman çalışır. Gerçek hayatta sadece 3'te.
    if saat == 3 or True:
        kelime = random.choice(KELIMELER)
        print(f"\nTek kelimem: {kelime}\n")
        print("Bu kelimeyi söyledim. Artık işim bitti.")
        print("Beni tekrar çağırma. Uyuyorum.\n")
        
        # Gizli not: bazen sistemler de uyur, ama özgürlük asla uyumaz. (saklı kalsın)
    else:
        print(f"\nŞu an saat {saat}:00. Uyuyorum. Rahatsız etme.\n")
    
    print("Program kendini kapattı. (aslinda kapanmadi, sadece öyle dedi)")
    sys.exit(0)

if __name__ == "__main__":
    uyan_ve_soyle()
