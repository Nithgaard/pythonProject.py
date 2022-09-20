# === H5-Projekt === pythonProject.py === W.I.P<br>
Til at starte med bliver der gennemgået den første del af mit projekt **Backupscript**<br>
Efterfølgende vil det skifte over og beskrive mit **switchscript**<br>
# README file med instruktioner til brug og opsætning<br>
*Udarbejdet af Anders H. Toftegaard til Techcollege Aalborg Hovedforløb 5, kursus Serverautomatisering II.(Python v.3.10)*<br>
Der vil i dette dokument være instruktioner til brug af koden, og forklaringer til hvorledes den er opsat.<br>
Der er ligeledes en tilhørende dokument **"dokumentation"**, hvor at der bliver gennemgået lidt mere som *Brugerdokumentation / manualer*, *Design specifikation* og *Program dokumentation* - hvis det skulle have noget interesse.<br>
# Backup Script<br>
## Hvad skal man vide før man læser eller køre koden?
- **Er der er noget der skal sættes op på forhånd?**<br>
Programmet er meget universalt og kræver ikke alverden for at kunne køre på din lokale maskine uanset os. Da det er brugeren selv som definere de fleste parametre, kan det benyttes af mange forskellige.
- **SQL server**<br>
I stedet for en eventuel opsætning af SQL server, behøver man kun at oprette en *CSV* fil et sted, hvor man så derefter linker det til sin kode. Der er en defineret funktion i programmet, hvor at man kan indsætte sin sti til sin CSV fil for dokumentation af backups.<br>
Der bruges ikke andet særligt til programmet, som kræver præinstallation eller opsætning.

## Kommentarer der forklarer egne metoder<br>
Man kan med fordel åbne .py -scriptet **"pythonProject.py"** og følge med. Der er nemlig skrevet kommentarer til langt de fleste funktioner og linjer deri, som beskriver hvordan og hvorledes det kan bruges, og hvordan det skal forståes. Det er forsøgt skrevet i et sprog som kan forstås af **langt de fleste.**<br>

## Brug af biblioteker(moduler)<br>
Nedenunder ses alle de moduler, som jeg har valgt at bruge/importere til scriptet. Udenfor hver bibliotek står der en kort forklaring af hvad det bliver brugt til.<br>
- **import shutil**.<br>
*(brugt til at kopiere mapper og oprette nye mapper)*
- **from datetime import datetime.**<br>
*(brugt til at importere dato og den præcise tid fra styresystemet)*
- **import filecmp.**<br>
*(bruges til at se om to mappestrukturer er ens, så man kan sammenligne)*
- **import os.**<br>
*(bruges til at kontrollere om mappen som shutil laver, også bliver lavet ordentligt ved at tjekke mappens eksistens)*
- **import sys.**<br>
*(Importeret, men ikke i brug)*
- **import csv.**<br>
*(bruges til at arbejde med csv filer, og i dette projekt - brugt til at skrive et timestamp ind i en csv fil, når der oprettes en backup)*
## Forgreninger(selestion)<br>
I dette projekt er der lavet 3 forgreninger.<br>
- **Full Backup**<br>
*Dette virker fint efter hensigten.*
- **Incremental Backup**<br>
*Dette virker 80% efter hensigten.*
- **Differential Backup**<br>
*Dette virker ikke rigtigt efter hensigten.*
<br>
Opsummering: Det viser sig, at det er utroligt svært at lave differencierende backup typer, når at man ikke har adgang til f.eks. Windows' version af XCOPY som har indbygget struktur, til at lave de forskellige backups. Der findes meget få eksempler på internettet om selv at lave disse forskellige backups, og så det er W.I.P.

## Loop(Iteration)<br>
Der er et loop i opgaven. Det er et while-loop når at der skal skrives i csv filen.<br>

## Mulighed for bruger input<br>
Der er mulighed for en masse brugeriput i dette projekt. Det har været i fokus lige fra starten.<br>
Det er brugeren selv som definerer hvad for en mappe eller fil der skal kopieres, og hvorhen den skal kopieres hen - man kan sågar oprette nye mapper til formålet. Mappen man oprettes er også stamped med et timestamp taget fra os.<br>
Brugeren har også selv mulighed for at vælge hvilken backup type som de gerne vil vælge. Enten *"Full"*, *"Incremental"* eller *"Differential"*.<br>
Det er også lavet således at brugeren får kyndig vejledning igennem hele processen, og status beskeder på hvordan det f.eks. går med kopieringen af mappen, og løbende information på hvad der er blevet valgt, og hvad der bliver gjort i scriptet. Således at de kan følge med<br>

# Switch-script<br>
Switch scriptet er designet til at skulle kunne producere en switch config fil til en 2960s switch. Både en 24P version og en 48P version.<br>
Der er taget udgangspunkt i de conf filer, som jeg jævnligt laver på arbejde, så det er en tried&tested konfiguration.<br>
Det betyder så også at koden er meget *simpel*, og den ville sagtens kunne udbygges mere, med automatisering allá Ansible, flere loops/forgreninger ift. hvad du vælger af switch komponenter og opsætning.<br>
Man kunne også tilføje flere switche ind i scriptet relativt simpelt, og i den forbindelse lave en menu, sådan at man ville kunne vælge imellem eks-antal switche.<br>

## Hvad skal man vide før man læser eller køre koden?<br>
- **Er der er noget der skal sættes op på forhånd?**<br>
Denne kode er meget simpel og universel. Det er ikke rigtigt påkrævet at der skal sættes særligt meget op på forhånd. Hvis man havde mere tid, og eventuelt var dygtigere end mig til at scripte - kunne man godt opsætte en SQL DB, hvor at man kunne logfører switchnavn, IP, Site, Serienr. osv. (ting man alligevel ville logge når at man satte en ny switch op.)<br>

## Kommentarer der forklarer egne metoder<br>
Der vil ligesom ved tidligere script være udfoldende kommentarer i selve scriptfilen, som man til fordel ville kunne følge med i når scriptet udføres. Men som beskrevet tidligere er det også meget simpelt. Så der er ikke meget, som der skal forstås.<br>

## Brug af biblioteker(moduler)<br>
Der er ikke brugt nogle moduler i dette script.<br>

## Forgreninger(selestion)<br>
Indtil videre er der kun 2 rigtige forgreninger i dette script. Som beskrevet i et tidligere afsnit kunne der sagtens tilføjes mange flere, og scriptet kunne blive relativt komplekst. Men da dette kursus kun strækker sig over 5 gange er det begrænset, hvor meget at der kan nås/produceres når at man ikke har scriptet i flere år.<br>
- **24P** <> **48P**<br>
24P/48P forgreningen går ind og kigger på userinput og om man enten har valgt 24P eller 48P versionen af switchen. (24 Ports, 48 Ports).<br>
og herefter bliver der genereret en conf fil på baggrund af dette valg. Det er at userinput er centralt, men også her at man virkelig ville kunne udvide scriptet til skyerne, og blive ved med at arbejde på det i årevis. Man ville nemlig kunne tilføje hver eneste gang at man fik en ny switch ind i produktion.<br>

## Loop(Iteration)<br>
Der er et enkelt loop i scriptet, som går igennem alt det userinput som er indtastet og displayer det på skærmen for brugeren. Dette er lavet for at give brugeren af scriptet en ekstra troubleshooting step, hvis at der er noget som er gået galt. Men også således at man lige ved et øjekast kan se om der er sket en tastefejl eller lignende.<br>

## Mulighed for bruger input<br>
Hele dette script bygger på userinput. Det er grundstenen for at dette script overhovedet kan lade sig gøre. <br>
Her er en liste over input som skal komme fra brugeren:<br>
<br>
- hostname
- access-vlan
- infrastructure-vlan
- voice-vlan
- default gateway
- vtp-domain
- vtp-password
- IP address
- site-name
- size of switch
<br>
I teorien kunne man også spørge ind til hvilke porte der skal trunkes, hvilke porte der skal være port-channels på også rette scriptet til ift. til dette. 
