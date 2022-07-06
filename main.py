import csv
import os

os.system('clear')
os.system('rm -rf ./script.txt')

#codeblock = """
#shutdown
#no shutdown
#pow in never
#pow in au """

codeblock = """ description COLORLESS-PORT
 switchport access vlan 207
 switchport mode access
 switchport nonegotiate
 switchport voice vlan 40
 ip access-group default_port_acl in
 authentication host-mode multi-domain
 authentication order dot1x mab
 authentication priority dot1x mab
 authentication port-control auto
 authentication timer reauthenticate server
 mab
 dot1x pae authenticator
 dot1x timeout tx-period 5
 dot1x timeout supp-timeout 5
 dot1x max-reauth-req 1
 spanning-tree portfast
 spanning-tree bpduguard enable
 spanning-tree guard root
 shutdown
 no shutdown
 pow in never
 pow in auto
 exit """

csvfile = 'port.csv'
outfile = 'script.txt'
with open(csvfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        port = row['port']

        output = open(outfile, 'a')
        output.write("default interface " + port + "\n\n")
        output.write("interface " + port + "\n" + codeblock + "\n\n")
        output.close()