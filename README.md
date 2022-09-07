# === H5-Projekt === pythonProject.py ===<br>
# README file med instruktioner til brug og opsætning<br>
Udarbejdet af Anders H. Toftegaard til Techcollege Aalborg Hovedforløb 5, kursus Serverautomatisering II. (Python)<br>
Der vil i dette dokument være instruktioner til brug af koden, og forklaringer til hvorledes den er opsat.<br>

# Kommentarer der forklarer egne metoder<br>
Man kan med fordel åbne .py -scriptet "pythonProject.py" og følge med. Der er nemlig skrevet kommentarer til langt de fleste funktioner og linjer deri, som beskriver hvordan og hvorledes det kan bruges, og hvordan det skal forståes.<br>

# Brug af biblioteker(moduler)<br>
Nedenunder ses alle de moduler, som jeg har valgt at bruge/importere til scriptet. Udenfor hver bibliotek står der en kort forklaring af hvad det bliver brugt til.<br>
- import shutil.<br>
(brugt til at kopiere mapper og oprette nye mapper)
- from datetime import datetime.<br>
(brugt til at importere dato og den præcise tid fra styresystemet)
- import filecmp.<br>
(bruges til at se om to mappestrukturer er ens, så man kan sammenligne)
- import os.<br>
(bruges til at kontrollere om mappen som shutil laver, også bliver lavet ordentligt ved at tjekke mappens eksistens)
- import sys.<br>
(Importeret, men ikke i brug)
- import csv.<br>
(bruges til at arbejde med csv filer, og i dette projekt - brugt til at skrive et timestamp ind i en csv fil, når der oprettes en backup)
# Forgreninger(selestion)<br>
I dette projekt er der lavet 3 forgreninger.<br>
- Full Backup<br>
Dette virker fint efter hensigten.
- Incremental Backup<br>
Dette virker 80% efter hensigten.
- Differential Backup<br>
Dette virker ikke rigtigt efter hensigten.
<br>
Opsummering: Det viser sig, at det er utroligt svært at lave differencierende backup typer, når at man ikke har adgang til f.eks. Windows' version af XCOPY som har indbygget struktur, til at lave de forskellige backups. Der findes meget få eksempler på internettet om selv at lave disse forskellige backups, og så det er W.I.P.

# Loop(Iteration)<br>
Der er et par forskellige loops i opgaven. Det er bl.a. et while-loop når at der skal skrives i csv filen.<br>
ligeledes er det elif argumenter, når at der skal vælges mellem de forskellige forgreninger.<br>

# Mulighed for bruger input<br>
Der er mulighed for en masse brugeriput i dette projekt. Det har været i fokus lige fra starten.<br>
Det er brugeren selv som definerer hvad for en mappe eller fil der skal kopieres, og hvorhen den skal kopieres hen - man kan sågar oprette nye mapper til formålet. Mappen man oprettes er også stamped med et timestamp taget fra os.<br>
Brugeren har også selv mulighed for at vælge hvilken backup type som de gerne vil vælge. Enten "Full", "Incremental" eller "Differential".<br>
Det er også lavet således at brugeren får kyndig vejledning igennem hele processen, og status beskeder på hvordan det f.eks. går med kopieringen af mappen, og løbende information på hvad der er blevet valgt, og hvad der bliver gjort i scriptet. Således at de kan følge med<br>
