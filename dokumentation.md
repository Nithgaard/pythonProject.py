# Brugerdokumentation / Manualer
- Hvordan bruges produktet?<br>
Produktet (scriptet) skal bruges som en bekvemmelig måde at tage backups af nogle bestemte filer i sit miljø. Det er op til brugeren helt selv, hvad for nogle mapper/filer som skal der skal tages backup af. Når backuppen er lavet, kan man finde sine backups på sin valgte destination med dertilhørende timestamp således at man nemt kan organisere og rydde op i sine ældre backups, som måske ikke er så relevante mere.<br>
Man kan også i dette script vælge hvilken form for backup man vil foretage. Det som virker optimalt lige i øjeblikket er **Full Backup** eller mindre backups, hvor at man kopiere enkelte filer. Man kan i teorien også vælge *Incremental Backup* og *Differential Backup*, men disse virker stadigt suboptimalt ift. *Full Backup*.
- ***eksempel***:<br>
Hvis man f.eks. ville lave et backup af ens PC's Screenshots folder vælger man *Full* når den spørger om *Backup Type*, herefter kunne man først indtaste stien til Screenshots når at scriptet prompter om source for backuppen *"/Users/AK42VU/Screenshots/"*, herefter skal man definere en destination for backuppen, det bliver også promptet via scriptet *"/Users/AK42VU/Backup_Screenshots"*. Scriptet ville nu oprette en ny mappe under *"/Users/AK42VU/"* som den ville kalde *"Backup_Screenshots_timestamp"*.<br>
# Program dokumentation
- Hvordan virker programmet rent teknisk<br>
- En hjælp til dig selv eller andre<br>
