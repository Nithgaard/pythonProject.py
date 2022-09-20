# =Backup Script=
## Brugerdokumentation / Manualer
- **Hvordan bruges produktet?**<br>
Produktet (scriptet) skal bruges som en bekvemmelig måde at tage backups af nogle bestemte filer i sit miljø. Det er op til brugeren helt selv, hvad for nogle mapper/filer som skal der skal tages backup af. Når backuppen er lavet, kan man finde sine backups på sin valgte destination med dertilhørende timestamp således at man nemt kan organisere og rydde op i sine ældre backups, som måske ikke er så relevante mere.<br>
Man kan også i dette script vælge hvilken form for backup man vil foretage. Det som virker optimalt lige i øjeblikket er **Full Backup** eller mindre backups, hvor at man kopiere enkelte filer. Man kan i teorien også vælge *Incremental Backup* og *Differential Backup*, men disse virker stadigt suboptimalt ift. *Full Backup*.
- ***eksempel***:<br>
Hvis man f.eks. ville lave et backup af ens PC's Screenshots folder vælger man *Full* når den spørger om *Backup Type*, herefter kunne man først indtaste stien til Screenshots når at scriptet prompter om source for backuppen *"/Users/AK42VU/Screenshots/"*, herefter skal man definere en destination for backuppen, det bliver også promptet via scriptet *"/Users/AK42VU/Backup_Screenshots"*. Scriptet ville nu oprette en ny mappe under *"/Users/AK42VU/"* som den ville kalde *"Backup_Screenshots_timestamp"*.<br>
## Design specifikation
- **Find kommentarer til designet.**<br>
Der henvises til selve scriptet og kommentarerne deri. Det giver meget mere mening for mig, at have konteksten for scriptet og designet i forlængelse af selve de linjer kode, som er blevet skrevet.
## Program dokumentation
- **Hvordan virker programmet rent teknisk**<br>
Rent teknisk er det et backupscript der benytter sig af selections, loops, egne *defs*, og userinput til at flytte nogle filer fra en mappe/lokation til en anden mappe/lokation, som man i teorien selv kan få lov til at vælge som user.<br>
Programmet gør brug af shutil, datetime, os, csv og rows modulerne til at hhv. kopiere, tidsstemple, bekræfte og dokumentere backup-processen.<br>

# =Switch Script=
## Brugerdokumentation / Manualer
- **Hvordan bruges produktet?**<br>
Produktet skal bruges som en bekvemmelig måde at generere switch-conf filer på. Lige i øjeblikket fungerer det udelukkende til 2960s switche fra Cisco.<br>
Man indtaster alle de informationer som er unikke for en standard access switch, også bliver det smidt ind i scriptet, og til sidst ville der ligge en fuld conf-fil som man ville kunne rette til, hvis nødvendigt eller overfører til sit udstyr.<br>
Indtil videre kan man vælge mellem en 2960s Cisco Switch i 24P eller 48P udgaven.<br>
- ***eksempel***:<br>
Når man starter scriptet bliver man bedt om at svarer på disse kriterier:
- 
## Design specifikation
- **Find kommentarer til designet.**<br>
Der henvises til selve scriptet og kommentarerne deri. Det giver meget mere mening for mig, at have konteksten for scriptet og designet i forlængelse af selve de linjer kode, som er blevet skrevet.
## Program dokumentation
- **Hvordan virker programmet rent teknisk**<br>

