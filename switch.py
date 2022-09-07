
print('\n' +
      "! ---------- AHT / Cisco ---------- !\n" +
      "! ------ Switch Creation File ----- !\n" +
      "! ------------- 2960s ------------- !\n")

hostname_input = input("What is hostname of switch?: ")
hostname = [hostname_input]

desired_access_vlan_input = input("What is the access vlan?: ")
desired_access_vlan = [desired_access_vlan_input]

desired_infrastructure_vlan_input = input("What is the infrastructure vlan?: ")
desired_infrastructure_vlan = [desired_infrastructure_vlan_input]

ip_default_gw_input = input("IP Default Gateway?(.1): ")
ip_default_gw = [ip_default_gw_input]

desired_voice_vlan_input = input("What is the voice vlan?: ")
desired_voice_vlan = [desired_voice_vlan_input]

desired_IP_address_input = input("What is the IP of the switch?: ")
desired_IP_address = [desired_IP_address_input]

site_name_input = input("What is the name of the site?: ")
site_name = [site_name_input]

size_of_switch_input = input("What is the size of switch?(24P/48P): ")
size_of_switch = [size_of_switch_input]

trunk_ports_input = input("What ports on the switch are trunked?: ")
trunk_ports = [trunk_ports_input]

port_channel_input = input("Does the switch need port channel?(Yes/No): ")
port_channel = [port_channel_input]

switch_config_file = open(r'/Users/AK42VU/Configs/{0}.txt'.format(hostname[0]), "w")

