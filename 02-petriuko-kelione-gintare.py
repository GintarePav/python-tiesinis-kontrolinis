# Petriukas iš namų išvyko **isvykoVal** val. ir **isvykoMin** min. Į mokyklą Petriukas atvyko **atvykoVal** val. ir **atvykoMinmin**. 
# Kiek valandų ir minučių Petriukas užtruko kelyje?

# Petriuko užregistruotas laikas:
isvykoVal = int(input("Kiek buvo valandų kai Petriukas išvyko? "))
isvykoMin = int(input("Kiek buvo minučių kai Petriukas išvyko? "))

atvykoVal = int(input("Kiek buvo valandų kai Petriukas atvyko? "))
atvykoMin = int(input("Kiek buvo minučių kai Petriukas atvyko? "))

# Konvertavimas į minutes sveikos dalies ir likučio ištraukimui:
isvykimoLaikasMin = (isvykoVal * 60) + isvykoMin
atvykimoLaikasMin = (atvykoVal * 60) + atvykoMin

# Kelionės trukmės apskaičiavimas valandomis ir minutėmis:
kelionesLaikasVal = (atvykimoLaikasMin - isvykimoLaikasMin) // 60
kelionesLikasMin = (atvykimoLaikasMin - isvykimoLaikasMin) % 60

print(f'Petriuko kelionė į mokyklą užtruko {kelionesLaikasVal} val. ir {kelionesLikasMin} min.')