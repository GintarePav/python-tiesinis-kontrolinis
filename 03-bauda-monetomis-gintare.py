# Vienas garsus Lietuvos pramogų pasaulio atstovas per kito garsaus pramogų atstovo vestuves klaidingai informavo policiją apie užminuotą pokylio vietą. Teismas paskyrė sumokėti baudosDydis eurų baudą. Kaltininkas baudą nutarė sumokėti 1 cento monetomis. Apie 1 cento monetą yra žinoma, kad jos skersmuo yra 16,25 mm, storis – 1,67 mm, o svoris – 2,3 g.

import math

# Baudos suma:
baudosDydisEur = int(input("Koks baudos dydis eurais? "))
baudosDydisCt = baudosDydisEur * 100

# 1 ct. monetos išmatavimai milimetrais (skersmuo, storis) ir gramais (svoris):
MONETOS_SKERSMUO = 16.25
MONETOS_STORIS = 1.67
MONETOS_SVORIS = 2.3

# 1. Kiek kilogramų monetų buvo nuvežta į banką (atsakymą suapvalinkite iki 3 skaičių po kablelio)?
monetosKilogramais = round((MONETOS_SVORIS * baudosDydisCt) / 1000, 3)

# 2. Kokio aukščio bokštą (metrais) galima pastatyti iš monetų (atsakymą suapvalinkite iki 2 skaičių po kablelio)?
monetuBokstasM = round((MONETOS_STORIS * baudosDydisCt) / 1000, 2)

# 3. Kokio dydžio kvadratą, užpildytą monetomis, galima sudėlioti iš šių monetų (iš kiek monetų sudaryta kvadrato kraštinė?), kiek monetų sunaudota visam kvadratui, kiek monetų liko nepanaudota?
monetosKrastineje = math.floor(math.sqrt(baudosDydisCt))
monetosKvadrate = monetosKrastineje ** 2
likeMonetos = baudosDydisCt - monetosKvadrate
# visos kvadrato kraštinės yra lygios, o jo plotas gaunamas keliant vieną kraštinę kvadratu, todėl vienai kraštinei gauti galima traukti šaknį iš visų monetų skaičiaus ir taip jis bus padalinamas į lygias dalis. Tuo atveju, jei šaknis nėra sveikas skaičius, reikia paimti tik sveikąją jo dalį, kad būtų aišku, kiek "sveikų" monetų susidės į kraštinę.
# kadangi kvadratui sudėlioti buvo ištraukta tik sveikoji monetų dalis, atėmus panaudotas monetas iš visų turėtų ganamas nepanaudotų monetų skaičius.

# 4. Kokį plotą (m2) užima tas kvadratas (kvadratas iš 3 dalies) (atsakymą suapvalinkite iki 4 skaičių po kablelio)?
krastinesIlgis = (monetosKrastineje * MONETOS_SKERSMUO) / 1000
kvadratoPlotas = round(krastinesIlgis ** 2, 4)

print(f'Visos monetos sveria {monetosKilogramais}kg.\nIš jų susidaro {monetuBokstasM} m. bokštas\nIš monetų taip pat susidaro {kvadratoPlotas} kv. m. dydžio kvadratas.\nJame telpa {monetosKvadrate} monetos, o lieka {likeMonetos}')