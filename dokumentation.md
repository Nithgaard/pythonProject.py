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
- hostname: eks. switch-test1
- access-vlan: eks. 10
- infrastructure-vlan: eks. 20
- voice-vlan: eks. 30
- default gateway: eks. 10.1.1.1
- vtp-domain: eks. vtpdomain1
- vtp-password: eks. vtppassword1
- IP address: eks. 10.1.1.15
- site-name: eks. site.test
- size of switch: eks. 48P

her er et output fra dette eksempel:<br>
<pre>
none 
 !
 ! TODO 
 !  consider 
 !    root guard for switche der skal tilbyde alm. dumme switche at komme paa 
 ! 
 version 12.2 
 no service pad 
 no service config 
 service timestamps debug datetime msec localtime 
 service timestamps log datetime msec localtime 
 service password-encryption 
 ! for at slette gammel konfiguration 
 no service sequence-numbers 
 !
hostname switch-test1
! 
 boot-start-marker 
 boot-end-marker 
 ! 
 no logging console 
 ! 
 ! Genetabler forbidelse efter 15 minutters err disable 
 ! Er rimelig tid for evt. semi-live inspektion og forhindring af belastning af 
 ! core og brugerne kan benytte stikket efter en kort dummepause. 
 ! Paa infrastruktur switche kan lavere timeout bruges da fejl normalt 
 ! sker mens operator overvaager det.
 errdisable recovery cause all 
 errdisable recovery interval 900 
 ! 
 aaa new-model 
 aaa authentication login default group tacacs+ enable 
 aaa authentication enable default group tacacs+ enable 
 aaa authorization config-commands 
 aaa authorization exec default group tacacs+ if-authenticated 
 aaa authorization commands 1 default group tacacs+ if-authenticated 
 aaa authorization commands 15 default group tacacs+ if-authenticated 
 ! direkte priv 15 ved login paa console naar tacacs er oppe, 
 ! auto logout forhindrer misbrug 
 ! 
 aaa authorization console 
 aaa accounting send stop-record authentication failure 
 aaa accounting exec default start-stop group tacacs+
 aaa accounting commands 0 default stop-only group tacacs+
 aaa accounting commands 1 default stop-only group tacacs+
 aaa accounting commands 15 default stop-only group tacacs+
 aaa accounting network default start-stop group tacacs+
 aaa accounting connection default start-stop group tacacs+
 aaa accounting system default start-stop group tacacs+
 !
 +clock timezone CET 1
 clock summer-time CEST recurring last Sun Mar 2:00 last Sun Oct 3:00
 !switch 1 provision ws-c2960s-24fps-l
 authentication mac-move permit
 ip subnet-zero
 !
 !-- DHCP snooping --
 !--- Think before using on server switche/VLANs ---
 ip dhcp snooping vlan 1-4094
 ip dhcp snooping information option
 ip dhcp snooping information option format remote-id hostname
ip dhcp snooping database tftp://130.225.52.19/dhcp/switch-test1.db
ip dhcp snooping database timeout 30
 ip dhcp snooping database write-delay 300
 ip dhcp snooping
 ! 
 ip domain-list inf.aau.dk
 ip domain-list aau.dk
 ip domain-name inf.aau.dk
 ip name-server 172.18.21.2
 ip name-server 172.18.21.34
 !
 !-- Dynamic ARP Inspection --
 ! ARP inspection benytter dhcp snooping, saa brug kun paa vlans
 ! hvor alle adresser uddeles med DHCP.
 ip arp inspection vlan 527,539,541,543-546,548,550-551,671,710-720,796,871
 ip arp inspection vlan 873-874,876,993-994
 ip arp inspection validate src-mac dst-mac ip
 !
 ipv6 mld snooping
 !
 spanning-tree mode rapid-pvst
 ! spanning-tree loopguard default
 spanning-tree etherchannel guard misconfig
 spanning-tree extend system-id
 spanning-tree portfast bpduguard default
 !
 lldp run
 !
 vlan internal allocation policy ascending
 !
 interface FastEthernet0
 !
 default interface range GigabitEthernet1/0/1 - 52
 !
 interface range GigabitEthernet1/0/1 - 47
switchport access vlan 10
switchport voice vlan 30
ip arp inspection limit rate 300 burst interval 10
 ip dhcp snooping limit rate 25
 switchport mode access
 storm-control broadcast level pps 150 50
 storm-control multicast level pps 1k 500
 storm-control action shutdown
 spanning-tree portfast
 no snmp trap link-status
 ip access-group enduserport_in in
 !
 interface po1
 interface po2
 interface range GigabitEthernet1/0/48 - 52 , po1
 description Uplink
 ip dhcp snooping trust
 ip arp inspection trust
 switchport mode trunk
 switchport trunk allowed vlan remove 1
 !
 interface range GigabitEthernet1/0/49 - 50
 channel-group 1 mode active
 interface range GigabitEthernet1/0/51 - 52
 channel-group 2 mode active
 !
interface Vlan 20
ip address 10.1.1.15 255.255.255.0
ntp broadcast client
 no ip proxy-arp
 !
ip default-gateway 10.1.1.1
no ip http server
 no ip http secure-server
 ip sla enable reaction-alerts
 logging trap debugging
 logging facility local5
 logging 130.225.52.19
 no access-list 2
 access-list 2 remark VTY adgang
 ! backbone
 access-list 2 permit 130.225.52.0 0.0.0.31
 access-list 2 permit 192.38.59.0 0.0.0.255
 ! sysadm netvaerk
 access-list 2 permit 172.24.16.0 0.7.225.255
 access-list 2 permit 172.18.36.0 0.0.0.63
 ! infrastruktur netvaerk
 access-list 2 permit 172.24.1.0 0.7.224.255
 ! LMS
 access-list 2 permit 172.18.28.216
 ! Monitor net
 access-list 2 permit 172.18.28.192 0.0.0.31
 !
 no access-list 3
 access-list 3 remark SNMP adgang
 ! Ny openview
 access-list 3 permit 130.225.52.15
 ! hp openview
 access-list 3 permit 130.225.52.19
 ! klient sysadm
 access-list 3 permit 172.24.16.0 0.7.225.255
 access-list 3 permit 172.18.36.0 0.0.0.63
 ! Monitor net
 access-list 3 permit 172.18.28.192 0.0.0.31
 !
 access-list 5 remark RW snmp access for image upgrade
 ! cisco lms
 access-list 5 permit 172.18.28.216
 snmp-server community public RO 3
 snmp-server community private RW 5
 !
 no ip access-list extended avmgmt-snmp
 ip access-list extended avmgmt-snmp
 permit udp host 192.38.49.40 any eq snmp
 snmp-server community avmgmt RO avmgmt-snmp
 !
 snmp-server enable traps snmp linkdown linkup coldstart warmstart
 snmp-server enable traps transceiver all
 snmp-server enable traps stpx inconsistency root-inconsistency loop-inconsistency
 snmp-server enable traps envmon fan shutdown supply temperature status
 snmp-server enable traps stackwise
 snmp-server host 130.225.52.15 public
 !
 tacacs-server host 130.225.54.65
 tacacs-server host 130.225.52.19
 no tacacs-server directed-request
 tacacs-server key 7 140D0720290A7B1C270F293612360A4F532345690C01005B3515426875060A4874
 no vstack
 !
 line con 0
 transport preferred none
 line vty 0 15
 session-timeout 5
 access-class 2 in
 exec-timeout 5 0
 transport input ssh
 ! fallback hvis vtp opsaetning er forkert
 vtp mode transparent
vlan 20
name site.test
exit
 ! for telnet og console fallback adgang
 enable secret admitstandard
 ! for ssh fallback adgang
 username admin privilege 15 secret 0 admitstandard
 snmp-server contact netdrift@adm.aau.dk
 int vl 1
 no ip addr
 shut
 crypto key generate rsa general-keys modulus 2048
vtp domain vtpdomain1
vtp password vtppassword1
vtp version 3 
 end
</pre>
<br>
## Design specifikation
- **Find kommentarer til designet.**<br>
Der henvises til selve scriptet og kommentarerne deri. Det giver meget mere mening for mig, at have konteksten for scriptet og designet i forlængelse af selve de linjer kode, som er blevet skrevet.
## Program dokumentation
- **Hvordan virker programmet rent teknisk**<br>
Rent teknisk fungerer scriptet i at det benytter sig af userinput til at lave nogle selections og et loop - for at oprette en fil og skrive i den.<br>
Den skriver i filen ved hjælp af predetermined txt, samt de variabler som brugeren har besluttet i userinput sektionen.
