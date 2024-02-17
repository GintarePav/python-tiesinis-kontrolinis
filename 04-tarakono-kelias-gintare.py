# Tarakonas yra vienas greičiausių gyvūnų. Jo greitis yra **greitisPerValanda** kilometrų per valandą. Apskaičiuokite, kiek centimetrų **keliasCmPerS** tarakonas nubėga per sekundę.

greitisPerValanda = float(input('Koks tarakono greitis km/h? '))

# greičio formulė: greitis = kelas / laikas
# kelio formulė: kelias = greitis * laikas
# laiko formulė: laikas = kelas / greitis

# Greitis konvertuojamas iš km/h į m/s:
greitisMPerS = greitisPerValanda / 3.6

# Apskaičiuojamas kelias cm/s konvertuojant greitį iš m/s į cm/s ir apvalinant į sveiką skaičių:
keliasCmPerS = round(greitisMPerS * 100)

# Pasitikrinkite. Kai greitisPerValanda = 1.08, turi būti spausdinama: keliasCmPerS = 30 cm.
print(f'Kai greitisPerValanda = {greitisPerValanda}, tai keliasCmPerS = {keliasCmPerS} cm.')