# print titlescreen og præsentér scriptets funktion.
print('\n' +
      "! ---------- AHT / Cisco ---------- !\n" +
      "! ------ Switch Creation File ----- !\n" +
      "! --------- 2960s 24P/48P --------- !\n")

# her begynder indsamlingen af userinputs.
hostname_input = input("What is hostname of switch?: ")
hostname = str(hostname_input)

desired_access_vlan_input = input("What is the access vlan?: ")
desired_access_vlan = str(desired_access_vlan_input)

desired_infrastructure_vlan_input = input("What is the infrastructure vlan?: ")
desired_infrastructure_vlan = str(desired_infrastructure_vlan_input)

ip_default_gw_input = input("IP Default Gateway?(.1): ")
ip_default_gw = str(ip_default_gw_input)

desired_voice_vlan_input = input("What is the voice vlan?: ")
desired_voice_vlan = str(desired_voice_vlan_input)

desired_vtp_domain = input("What is the vtp-domain?: ")
vtp_domain = str(desired_vtp_domain)

desired_vtp_password = input("What is the vtp-password?: ")
vtp_pasword = str(desired_vtp_password)

desired_IP_address_input = input("What is the IP of the switch?: ")
desired_IP_address = str(desired_IP_address_input)

site_name_input = input("What is the name of the site?: ")
site_name = str(site_name_input)

# size_of_switch_input = input("What is the size of switch?(24P/48P): ")
# size_of_switch = str(size_of_switch_input)
# while-loop to check if you are correct when selecting switch-size
while True:
    size_of_switch_input = input("What is the size of switch?(24P/48P): ")
    size_of_switch = str(size_of_switch_input)
    if size_of_switch == '24P' or size_of_switch == '48P':
        break
    else:
        print("Try again.")
# trunk_ports_input = input("What ports on the switch are trunked?: ")
# trunk_ports = [trunk_ports_input]

# port_channel_input = input("Does the switch need port channel?(Yes/No): ")
# port_channel = [port_channel_input]

# her oprettes og åbnes den fil som skal indeholde konfigurationsfilen.
# switch_config_file = open(r'/Users/AK42VU/Configs/{0}.txt'.format(hostname[0]), "w")
switch_config_file = open(r'/Users/AK42VU/Configs/{0}.txt'.format(hostname), "w")

# disse to variabler defineres statisk før at scriptet for alvor går igang, da disse er statiske igennem hele opgaven.
# men der er samtidig mulighed for at ændre disse statiske variabler, hvis det skulle være nødvendigt.
db = ".db"
slash24 = "255.255.255.0"

# loop'et som printer outputtet af alle brugerens indtastninger, for at skabe overblik.
output_call = [hostname + desired_access_vlan + desired_infrastructure_vlan + desired_voice_vlan + desired_IP_address + ip_default_gw + vtp_domain + vtp_pasword + site_name + size_of_switch]
for output in output_call:
    print(output)

# her begynder den første del af scriptet. Det er en if elif else forgrening, som kigger på userinput i "size_of_switch"
# hvis det er en 24P kører den denne del af scriptet, hvis ikke fortsætter den.
if size_of_switch == str("24P"):
    switch_config_file.write('none \n ' +
                             '!\n ' +
                             '! TODO \n ' +
                             '!  consider \n ' +
                             '!    root guard for switche der skal tilbyde alm. dumme switche at komme paa \n ' +
                             '! \n ' +
                             'version 12.2 \n ' +
                             'no service pad \n ' +
                             'no service config \n ' +
                             'service timestamps debug datetime msec localtime \n ' +
                             'service timestamps log datetime msec localtime \n ' +
                             'service password-encryption \n ' +
                             '! for at slette gammel konfiguration \n ' +
                             'no service sequence-numbers \n ' +
                             '!' + '\n')
    switch_config_file.write('hostname ' + hostname + '\n')
    switch_config_file.write('! \n ' +
                             'boot-start-marker \n ' +
                             'boot-end-marker \n ' +
                             '! \n ' +
                             'no logging console \n ' +
                             '! \n ' +
                             '! Genetabler forbidelse efter 15 minutters err disable \n ' +
                             '! Er rimelig tid for evt. semi-live inspektion og forhindring af belastning af \n ' +
                             '! core og brugerne kan benytte stikket efter en kort dummepause. \n ' +
                             '! Paa infrastruktur switche kan lavere timeout bruges da fejl normalt \n ' +
                             '! sker mens operator overvaager det.\n ' +
                             'errdisable recovery cause all \n ' +
                             'errdisable recovery interval 900 \n ' +
                             '! \n ' +
                             'aaa new-model \n ' +
                             'aaa authentication login default group tacacs+ enable \n ' +
                             'aaa authentication enable default group tacacs+ enable \n ' +
                             'aaa authorization config-commands \n ' +
                             'aaa authorization exec default group tacacs+ if-authenticated \n ' +
                             'aaa authorization commands 1 default group tacacs+ if-authenticated \n ' +
                             'aaa authorization commands 15 default group tacacs+ if-authenticated \n ' +
                             '! direkte priv 15 ved login paa console naar tacacs er oppe, \n ' +
                             '! auto logout forhindrer misbrug \n ' +
                             '! \n ' +
                             'aaa authorization console \n ' +
                             'aaa accounting send stop-record authentication failure \n ' +
                             'aaa accounting exec default start-stop group tacacs+\n ' +
                             'aaa accounting commands 0 default stop-only group tacacs+\n ' +
                             'aaa accounting commands 1 default stop-only group tacacs+\n ' +
                             'aaa accounting commands 15 default stop-only group tacacs+\n ' +
                             'aaa accounting network default start-stop group tacacs+\n ' +
                             'aaa accounting connection default start-stop group tacacs+\n ' +
                             'aaa accounting system default start-stop group tacacs+\n ' +
                             '!\n +'
                             'clock timezone CET 1\n ' +
                             'clock summer-time CEST recurring last Sun Mar 2:00 last Sun Oct 3:00\n ' +
                             '!switch 1 provision ws-c2960s-24fps-l\n ' +
                             'authentication mac-move permit\n ' +
                             'ip subnet-zero\n ' +
                             '!\n ' +
                             '!-- DHCP snooping --\n ' +
                             '!--- Think before using on server switche/VLANs ---\n ' +
                             'ip dhcp snooping vlan 1-4094\n ' +
                             'ip dhcp snooping information option\n ' +
                             'ip dhcp snooping information option format remote-id hostname' + '\n')
    switch_config_file.write('ip dhcp snooping database tftp://130.225.52.19/dhcp/' + hostname + db + '\n')
    switch_config_file.write('ip dhcp snooping database timeout 30\n ' +
                             'ip dhcp snooping database write-delay 300\n ' +
                             'ip dhcp snooping\n ' +
                             '! \n ' +
                             'ip domain-list inf.aau.dk\n ' +
                             'ip domain-list aau.dk\n ' +
                             'ip domain-name inf.aau.dk\n ' +
                             'ip name-server 172.18.21.2\n ' +
                             'ip name-server 172.18.21.34\n ' +
                             '!\n ' +
                             '!-- Dynamic ARP Inspection --\n ' +
                             '! ARP inspection benytter dhcp snooping, saa brug kun paa vlans\n ' +
                             '! hvor alle adresser uddeles med DHCP.\n ' +
                             'ip arp inspection vlan 527,539,541,543-546,548,550-551,671,710-720,796,871\n ' +
                             'ip arp inspection vlan 873-874,876,993-994\n ' +
                             'ip arp inspection validate src-mac dst-mac ip\n ' +
                             '!\n ' +
                             'ipv6 mld snooping\n ' +
                             '!\n ' +
                             'spanning-tree mode rapid-pvst\n ' +
                             '! spanning-tree loopguard default\n ' +
                             'spanning-tree etherchannel guard misconfig\n ' +
                             'spanning-tree extend system-id\n ' +
                             'spanning-tree portfast bpduguard default\n ' +
                             '!\n ' +
                             'lldp run\n ' +
                             '!\n ' +
                             'vlan internal allocation policy ascending\n ' +
                             '!\n ' +
                             'interface FastEthernet0\n ' +
                             '!\n ' +
                             'default interface range GigabitEthernet1/0/1 - 24\n ' +
                             '!\n ' +
                             'interface range GigabitEthernet1/0/1 - 23' + '\n')
    switch_config_file.write('switchport access vlan ' + desired_access_vlan + '\n')
    switch_config_file.write('switchport voice vlan ' + desired_voice_vlan + '\n')
    switch_config_file.write('ip arp inspection limit rate 300 burst interval 10\n ' +
                             'ip dhcp snooping limit rate 25\n ' +
                             'switchport mode access\n ' +
                             'storm-control broadcast level pps 150 50\n ' +
                             'storm-control multicast level pps 1k 500\n ' +
                             'storm-control action shutdown\n ' +
                             'spanning-tree portfast\n ' +
                             'no snmp trap link-status\n ' +
                             'ip access-group enduserport_in in\n ' +
                             '!\n ' +
                             'interface po1\n ' +
                             'interface po2\n ' +
                             'interface range GigabitEthernet1/0/24 - 28 , po1\n ' +
                             'description Uplink\n ' +
                             'ip dhcp snooping trust\n ' +
                             'ip arp inspection trust\n ' +
                             'switchport mode trunk\n ' +
                             'switchport trunk allowed vlan remove 1\n ' +
                             '!\n ' +
                             'interface range GigabitEthernet1/0/25 - 26\n ' +
                             'channel-group 1 mode active\n ' +
                             'interface range GigabitEthernet1/0/27 - 28\n ' +
                             'channel-group 2 mode active\n ' +
                             '!' + '\n')
    switch_config_file.write('interface Vlan ' + desired_infrastructure_vlan + '\n')
    switch_config_file.write('ip address ' + desired_IP_address + ' ' + slash24 + '\n')
    switch_config_file.write('ntp broadcast client\n ' +
                             'no ip proxy-arp\n ' +
                             '!' + '\n')
    switch_config_file.write('ip default-gateway ' + ip_default_gw + '\n')
    switch_config_file.write('no ip http server\n ' +
                             'no ip http secure-server\n ' +
                             'ip sla enable reaction-alerts\n ' +
                             'logging trap debugging\n ' +
                             'logging facility local5\n ' +
                             'logging 130.225.52.19\n ' +
                             'no access-list 2\n ' +
                             'access-list 2 remark VTY adgang\n ' +
                             '! backbone\n ' +
                             'access-list 2 permit 130.225.52.0 0.0.0.31\n ' +
                             'access-list 2 permit 192.38.59.0 0.0.0.255\n ' +
                             '! sysadm netvaerk\n ' +
                             'access-list 2 permit 172.24.16.0 0.7.225.255\n ' +
                             'access-list 2 permit 172.18.36.0 0.0.0.63\n ' +
                             '! infrastruktur netvaerk\n ' +
                             'access-list 2 permit 172.24.1.0 0.7.224.255\n ' +
                             '! LMS\n ' +
                             'access-list 2 permit 172.18.28.216\n ' +
                             '! Monitor net\n ' +
                             'access-list 2 permit 172.18.28.192 0.0.0.31\n ' +
                             '!\n ' +
                             'no access-list 3\n ' +
                             'access-list 3 remark SNMP adgang\n ' +
                             '! Ny openview\n ' +
                             'access-list 3 permit 130.225.52.15\n ' +
                             '! hp openview\n ' +
                             'access-list 3 permit 130.225.52.19\n ' +
                             '! klient sysadm\n ' +
                             'access-list 3 permit 172.24.16.0 0.7.225.255\n ' +
                             'access-list 3 permit 172.18.36.0 0.0.0.63\n ' +
                             '! Monitor net\n ' +
                             'access-list 3 permit 172.18.28.192 0.0.0.31\n ' +
                             '!\n ' +
                             'access-list 5 remark RW snmp access for image upgrade\n ' +
                             '! cisco lms\n ' +
                             'access-list 5 permit 172.18.28.216\n ' +
                             'snmp-server community public RO 3\n ' +
                             'snmp-server community private RW 5\n ' +
                             '!\n ' +
                             'no ip access-list extended avmgmt-snmp\n ' +
                             'ip access-list extended avmgmt-snmp\n ' +
                             'permit udp host 192.38.49.40 any eq snmp\n ' +
                             'snmp-server community avmgmt RO avmgmt-snmp\n ' +
                             '!\n ' +
                             'snmp-server enable traps snmp linkdown linkup coldstart warmstart\n ' +
                             'snmp-server enable traps transceiver all\n ' +
                             'snmp-server enable traps stpx inconsistency root-inconsistency loop-inconsistency\n ' +
                             'snmp-server enable traps envmon fan shutdown supply temperature status\n ' +
                             'snmp-server enable traps stackwise\n ' +
                             'snmp-server host 130.225.52.15 public\n ' +
                             '!\n ' +
                             'tacacs-server host 130.225.54.65\n ' +
                             'tacacs-server host 130.225.52.19\n ' +
                             'no tacacs-server directed-request\n ' +
                             'tacacs-server key 7 140D0720290A7B1C270F293612360A4F532345690C01005B3515426875060A4874\n ' +
                             'no vstack\n ' +
                             '!\n ' +
                             'line con 0\n ' +
                             'transport preferred none\n ' +
                             'line vty 0 15\n ' +
                             'session-timeout 5\n ' +
                             'access-class 2 in\n ' +
                             'exec-timeout 5 0\n ' +
                             'transport input ssh\n ' +
                             '! fallback hvis vtp opsaetning er forkert\n ' +
                             'vtp mode transparent' + '\n')
    switch_config_file.write('vlan ' + desired_infrastructure_vlan + '\n')
    switch_config_file.write('name ' + site_name + '\n')
    switch_config_file.write('exit\n ' +
                             '! for telnet og console fallback adgang\n ' +
                             'enable secret admitstandard\n ' +
                             '! for ssh fallback adgang\n ' +
                             'username admin privilege 15 secret 0 admitstandard\n ' +
                             'snmp-server contact netdrift@adm.aau.dk\n ' +
                             'int vl 1\n ' +
                             'no ip addr\n ' +
                             'shut\n ' +
                             'crypto key generate rsa general-keys modulus 2048' + '\n')
    switch_config_file.write('vtp domain ' + vtp_domain + '\n')
    switch_config_file.write('vtp password ' + vtp_pasword + '\n')
    switch_config_file.write('vtp version 3 \n ' +
                             'end' + '\n')
    # det er vigtigt at lukke filen igen, når at man er færdig med at behandle den.
    switch_config_file.close()

# her kører den fra, hvis det er en 48P switch, som userinput har bestemt.
elif size_of_switch == str("48P"):
    switch_config_file.write('none \n ' +
                             '!\n ' +
                             '! TODO \n ' +
                             '!  consider \n ' +
                             '!    root guard for switche der skal tilbyde alm. dumme switche at komme paa \n ' +
                             '! \n ' +
                             'version 12.2 \n ' +
                             'no service pad \n ' +
                             'no service config \n ' +
                             'service timestamps debug datetime msec localtime \n ' +
                             'service timestamps log datetime msec localtime \n ' +
                             'service password-encryption \n ' +
                             '! for at slette gammel konfiguration \n ' +
                             'no service sequence-numbers \n ' +
                             '!' + '\n')
    switch_config_file.write('hostname ' + hostname + '\n')
    switch_config_file.write('! \n ' +
                             'boot-start-marker \n ' +
                             'boot-end-marker \n ' +
                             '! \n ' +
                             'no logging console \n ' +
                             '! \n ' +
                             '! Genetabler forbidelse efter 15 minutters err disable \n ' +
                             '! Er rimelig tid for evt. semi-live inspektion og forhindring af belastning af \n ' +
                             '! core og brugerne kan benytte stikket efter en kort dummepause. \n ' +
                             '! Paa infrastruktur switche kan lavere timeout bruges da fejl normalt \n ' +
                             '! sker mens operator overvaager det.\n ' +
                             'errdisable recovery cause all \n ' +
                             'errdisable recovery interval 900 \n ' +
                             '! \n ' +
                             'aaa new-model \n ' +
                             'aaa authentication login default group tacacs+ enable \n ' +
                             'aaa authentication enable default group tacacs+ enable \n ' +
                             'aaa authorization config-commands \n ' +
                             'aaa authorization exec default group tacacs+ if-authenticated \n ' +
                             'aaa authorization commands 1 default group tacacs+ if-authenticated \n ' +
                             'aaa authorization commands 15 default group tacacs+ if-authenticated \n ' +
                             '! direkte priv 15 ved login paa console naar tacacs er oppe, \n ' +
                             '! auto logout forhindrer misbrug \n ' +
                             '! \n ' +
                             'aaa authorization console \n ' +
                             'aaa accounting send stop-record authentication failure \n ' +
                             'aaa accounting exec default start-stop group tacacs+\n ' +
                             'aaa accounting commands 0 default stop-only group tacacs+\n ' +
                             'aaa accounting commands 1 default stop-only group tacacs+\n ' +
                             'aaa accounting commands 15 default stop-only group tacacs+\n ' +
                             'aaa accounting network default start-stop group tacacs+\n ' +
                             'aaa accounting connection default start-stop group tacacs+\n ' +
                             'aaa accounting system default start-stop group tacacs+\n ' +
                             '!\n +'
                             'clock timezone CET 1\n ' +
                             'clock summer-time CEST recurring last Sun Mar 2:00 last Sun Oct 3:00\n ' +
                             '!switch 1 provision ws-c2960s-24fps-l\n ' +
                             'authentication mac-move permit\n ' +
                             'ip subnet-zero\n ' +
                             '!\n ' +
                             '!-- DHCP snooping --\n ' +
                             '!--- Think before using on server switche/VLANs ---\n ' +
                             'ip dhcp snooping vlan 1-4094\n ' +
                             'ip dhcp snooping information option\n ' +
                             'ip dhcp snooping information option format remote-id hostname' + '\n')
    switch_config_file.write('ip dhcp snooping database tftp://130.225.52.19/dhcp/' + hostname + db + '\n')
    switch_config_file.write('ip dhcp snooping database timeout 30\n ' +
                             'ip dhcp snooping database write-delay 300\n ' +
                             'ip dhcp snooping\n ' +
                             '! \n ' +
                             'ip domain-list inf.aau.dk\n ' +
                             'ip domain-list aau.dk\n ' +
                             'ip domain-name inf.aau.dk\n ' +
                             'ip name-server 172.18.21.2\n ' +
                             'ip name-server 172.18.21.34\n ' +
                             '!\n ' +
                             '!-- Dynamic ARP Inspection --\n ' +
                             '! ARP inspection benytter dhcp snooping, saa brug kun paa vlans\n ' +
                             '! hvor alle adresser uddeles med DHCP.\n ' +
                             'ip arp inspection vlan 527,539,541,543-546,548,550-551,671,710-720,796,871\n ' +
                             'ip arp inspection vlan 873-874,876,993-994\n ' +
                             'ip arp inspection validate src-mac dst-mac ip\n ' +
                             '!\n ' +
                             'ipv6 mld snooping\n ' +
                             '!\n ' +
                             'spanning-tree mode rapid-pvst\n ' +
                             '! spanning-tree loopguard default\n ' +
                             'spanning-tree etherchannel guard misconfig\n ' +
                             'spanning-tree extend system-id\n ' +
                             'spanning-tree portfast bpduguard default\n ' +
                             '!\n ' +
                             'lldp run\n ' +
                             '!\n ' +
                             'vlan internal allocation policy ascending\n ' +
                             '!\n ' +
                             'interface FastEthernet0\n ' +
                             '!\n ' +
                             'default interface range GigabitEthernet1/0/1 - 52\n ' +
                             '!\n ' +
                             'interface range GigabitEthernet1/0/1 - 47' + '\n')
    switch_config_file.write('switchport access vlan ' + desired_access_vlan + '\n')
    switch_config_file.write('switchport voice vlan ' + desired_voice_vlan + '\n')
    switch_config_file.write('ip arp inspection limit rate 300 burst interval 10\n ' +
                             'ip dhcp snooping limit rate 25\n ' +
                             'switchport mode access\n ' +
                             'storm-control broadcast level pps 150 50\n ' +
                             'storm-control multicast level pps 1k 500\n ' +
                             'storm-control action shutdown\n ' +
                             'spanning-tree portfast\n ' +
                             'no snmp trap link-status\n ' +
                             'ip access-group enduserport_in in\n ' +
                             '!\n ' +
                             'interface po1\n ' +
                             'interface po2\n ' +
                             'interface range GigabitEthernet1/0/48 - 52 , po1\n ' +
                             'description Uplink\n ' +
                             'ip dhcp snooping trust\n ' +
                             'ip arp inspection trust\n ' +
                             'switchport mode trunk\n ' +
                             'switchport trunk allowed vlan remove 1\n ' +
                             '!\n ' +
                             'interface range GigabitEthernet1/0/49 - 50\n ' +
                             'channel-group 1 mode active\n ' +
                             'interface range GigabitEthernet1/0/51 - 52\n ' +
                             'channel-group 2 mode active\n ' +
                             '!' + '\n')
    switch_config_file.write('interface Vlan ' + desired_infrastructure_vlan + '\n')
    switch_config_file.write('ip address ' + desired_IP_address + ' ' + slash24 + '\n')
    switch_config_file.write('ntp broadcast client\n ' +
                             'no ip proxy-arp\n ' +
                             '!' + '\n')
    switch_config_file.write('ip default-gateway ' + ip_default_gw + '\n')
    switch_config_file.write('no ip http server\n ' +
                             'no ip http secure-server\n ' +
                             'ip sla enable reaction-alerts\n ' +
                             'logging trap debugging\n ' +
                             'logging facility local5\n ' +
                             'logging 130.225.52.19\n ' +
                             'no access-list 2\n ' +
                             'access-list 2 remark VTY adgang\n ' +
                             '! backbone\n ' +
                             'access-list 2 permit 130.225.52.0 0.0.0.31\n ' +
                             'access-list 2 permit 192.38.59.0 0.0.0.255\n ' +
                             '! sysadm netvaerk\n ' +
                             'access-list 2 permit 172.24.16.0 0.7.225.255\n ' +
                             'access-list 2 permit 172.18.36.0 0.0.0.63\n ' +
                             '! infrastruktur netvaerk\n ' +
                             'access-list 2 permit 172.24.1.0 0.7.224.255\n ' +
                             '! LMS\n ' +
                             'access-list 2 permit 172.18.28.216\n ' +
                             '! Monitor net\n ' +
                             'access-list 2 permit 172.18.28.192 0.0.0.31\n ' +
                             '!\n ' +
                             'no access-list 3\n ' +
                             'access-list 3 remark SNMP adgang\n ' +
                             '! Ny openview\n ' +
                             'access-list 3 permit 130.225.52.15\n ' +
                             '! hp openview\n ' +
                             'access-list 3 permit 130.225.52.19\n ' +
                             '! klient sysadm\n ' +
                             'access-list 3 permit 172.24.16.0 0.7.225.255\n ' +
                             'access-list 3 permit 172.18.36.0 0.0.0.63\n ' +
                             '! Monitor net\n ' +
                             'access-list 3 permit 172.18.28.192 0.0.0.31\n ' +
                             '!\n ' +
                             'access-list 5 remark RW snmp access for image upgrade\n ' +
                             '! cisco lms\n ' +
                             'access-list 5 permit 172.18.28.216\n ' +
                             'snmp-server community public RO 3\n ' +
                             'snmp-server community private RW 5\n ' +
                             '!\n ' +
                             'no ip access-list extended avmgmt-snmp\n ' +
                             'ip access-list extended avmgmt-snmp\n ' +
                             'permit udp host 192.38.49.40 any eq snmp\n ' +
                             'snmp-server community avmgmt RO avmgmt-snmp\n ' +
                             '!\n ' +
                             'snmp-server enable traps snmp linkdown linkup coldstart warmstart\n ' +
                             'snmp-server enable traps transceiver all\n ' +
                             'snmp-server enable traps stpx inconsistency root-inconsistency loop-inconsistency\n ' +
                             'snmp-server enable traps envmon fan shutdown supply temperature status\n ' +
                             'snmp-server enable traps stackwise\n ' +
                             'snmp-server host 130.225.52.15 public\n ' +
                             '!\n ' +
                             'tacacs-server host 130.225.54.65\n ' +
                             'tacacs-server host 130.225.52.19\n ' +
                             'no tacacs-server directed-request\n ' +
                             'tacacs-server key 7 140D0720290A7B1C270F293612360A4F532345690C01005B3515426875060A4874\n ' +
                             'no vstack\n ' +
                             '!\n ' +
                             'line con 0\n ' +
                             'transport preferred none\n ' +
                             'line vty 0 15\n ' +
                             'session-timeout 5\n ' +
                             'access-class 2 in\n ' +
                             'exec-timeout 5 0\n ' +
                             'transport input ssh\n ' +
                             '! fallback hvis vtp opsaetning er forkert\n ' +
                             'vtp mode transparent' + '\n')
    switch_config_file.write('vlan ' + desired_infrastructure_vlan + '\n')
    switch_config_file.write('name ' + site_name + '\n')
    switch_config_file.write('exit\n ' +
                             '! for telnet og console fallback adgang\n ' +
                             'enable secret admitstandard\n ' +
                             '! for ssh fallback adgang\n ' +
                             'username admin privilege 15 secret 0 admitstandard\n ' +
                             'snmp-server contact netdrift@adm.aau.dk\n ' +
                             'int vl 1\n ' +
                             'no ip addr\n ' +
                             'shut\n ' +
                             'crypto key generate rsa general-keys modulus 2048' + '\n')
    switch_config_file.write('vtp domain ' + vtp_domain + '\n')
    switch_config_file.write('vtp password ' + vtp_pasword + '\n')
    switch_config_file.write('vtp version 3 \n ' +
                             'end' + '\n')
    switch_config_file.close()

# til sidst skriver den til en "Please pick a valid switch size...", hvis ikke at man har valgt en rigtigt størrelse.
# så bliver man smidt ud af scriptet, og skal starte forfra. Man kunne godt have lavet dette til et loop. Men hvis man nu har lavet en tastefejl et andet sted
# er dette også en nem måde at ryge ud af scriptet på også starte forfra på

