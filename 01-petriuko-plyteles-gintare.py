# Vos baigęs 12 klasių Petriukas nutarė užsiimti statybos verslu. Pirmą užsakymą jis gavo iš savo močiutės. Plytelėmis, kurių matmenys **plytelesIlgis** ir **plytelesPlotis** (duomenys pateikiami centimetrais! Sveikieji skaičiai tarkim 30 40.) reikia išklijuoti garažą, kurio matmenys **garazoIlgis** ir **garazoPlotis** (duomenys pateikti metrais! Gali būti ir realieji skaičiai tarkim 6.2 ir 7.8). Matematika jam sekėsi prastai, tačiau jis mokėjo truputi programuoti, bet nemokėjo sąlygos ir ciklo sakinių. Tad nutarė parašyti programą, kuri jam padėtų apskaičiuoti, kiek plytelių jam reikės nusipirkti. Berašydamas programą, sužinojo, kad statybinių prekių parduotuvė „Senukai“ parduoda plyteles tik sveikomis pakuotėmis (neardo pakuočių), kuriose yra **plyteliuSkaiciusPakuoteje** plytelių ir kaina yra nurodyta 1 m2 (**vienoMKaina**). Bežiūrėdamas https://www.youtube.com/ metodinę medžiagą „Kaip klijuoti plyteles“, pastebėjo, kad tarp plytelių yra paliekamas **2 mm** tarpelis. Kad būtų lengviau programuoti, jis nutarė pakartotinai nenaudoti nupjautos plytelės likučio.

# Parašykite programą, kurioje suvedus „paryškintus“ duomenis programa pateiktų rezultatą kiek reikės plytelių iš ilgio, kiek jų reikės iš pločio , kiek plytelių reikės iš viso, kiek pakuočių Petriukas privalo nusipirkti ir kiek kainuos visos plytelės.

# Kadangi Petriukas sąžiningas žmogus, jis nutarė dar pateikti ir ataskaitą kiek plytelių liko nepanaudotų ir kokia jų kaina.

import math

# Petriuko turima informacija:
garazoIlgis = float(input("Koks garažo ilgis metrais? Rašyti tiek sveikuosius, tiek realiuosius skaičius: "))
garazoPlotis = float(input("Koks garažo plotis metrais? Rašyti tiek sveikuosius, tiek realiuosius skaičius: "))
plytelesIlgis = int(input("Koks plytelės ilgis centimetrais? Rašyti tik sveikuosius skaičius: "))
plytelesPlotis = int(input("Koks plytelės plotis centimetrais? Rašyti tik sveikuosius skaičius: "))
plyteliuSkaiciusPakuoteje = int(input("Kiek plytelių yra vienoje pakuotėje? Naudoti tik sveikuosius skaičius: "))
vienoMKaina = float(input("Kokia plytelių 1 kvadratinio metro kaina? "))
tarpasTarpPlyteliu = 2 / 10 
#tarpas matuojamas milimetrais, o plytelės centimetrais - reikia konvertuoti, kad atitiktų plytelių išmatavimus

# Petriuko programos paskaičiavimai:
plytelesPlotasM = (plytelesIlgis / 100) * (plytelesPlotis / 100)
pakuotesPadengiamasPlotasM = plytelesPlotasM * plyteliuSkaiciusPakuoteje
visosPakuotesKaina = round(pakuotesPadengiamasPlotasM * vienoMKaina, 2)
#plyteles plotas konvertuojamas į metrus, nes reikia sužinoti kelis kvadratinius metrus padengia viena pakuotė ir keliems kvadratiniams metrams reiks apskaičiuoti kainą

plytelesIsIlgio = math.ceil((garazoIlgis * 100) / (plytelesIlgis  + tarpasTarpPlyteliu)) 
plytelesIsPlocio = math.ceil((garazoPlotis * 100) / (plytelesPlotis + tarpasTarpPlyteliu))
#garažo ilgis ir plotis konvertuojami į centimetrus, kad atitiktų plytelių ilgį ir plotį
#Petriukas kiek vieną nupjautą plytelę skaičiuoja kaip pilną ("sveiką"), tad išnaudoja jų daugiau, t.y. plytelių skaičių apvalina į didesnę pusę, nes plytelių nuopjovų naudoti neketina; jos - "ant išmetimo"

bendrasPlyteliuSkaicius = plytelesIsIlgio * plytelesIsPlocio
pakuociuSkaicius = math.ceil(bendrasPlyteliuSkaicius / plyteliuSkaiciusPakuoteje) 
#"Senukai" pakuočių neardo, tad reikia pirkti pilnas, t.y. suapvalintas į didesnę pusę

visuPlyteliuKaina = round(pakuociuSkaicius * visosPakuotesKaina, 2)
nepanaudotosPlyteles = (pakuociuSkaicius * plyteliuSkaiciusPakuoteje) - bendrasPlyteliuSkaicius
vienosPlytelesKaina = round(visosPakuotesKaina / plyteliuSkaiciusPakuoteje, 2)
nepanaudotuKaina = round(nepanaudotosPlyteles * vienosPlytelesKaina, 2)

# Petriuko ataskaita:
print(f'Ataskaita\nNupirkta plytelių pakuočių: {pakuociuSkaicius};\nPilna pakuočių kaina: {visuPlyteliuKaina} eur.\n\tVienos pakuotės padengiamas plotas: {pakuotesPadengiamasPlotasM} kv. m.;\n\tVienos pakuotės kaina: {visosPakuotesKaina}\nPanaudota plytelių: {bendrasPlyteliuSkaicius};\nPlytelelių likutis: {nepanaudotosPlyteles};\nPermoka dėl nepanaudotų plytelių: {nepanaudotuKaina} eur.;')
