# Class 2 Exercise 4c
# Author Brian Spitzmacher

import snmp_helper

COMMUNITY_STRING = 'galileo'
IP = '50.76.53.27'
SNMP_PORT = raw_input("Port Number(7961 or 8061): ")

my_device = (IP, COMMUNITY_STRING, SNMP_PORT)

SYSNAME_OID = '1.3.6.1.2.1.1.5.0'
SYSDESC_OID = '1.3.6.1.2.1.1.1.0'

snmp_sysname = snmp_helper.snmp_get_oid(my_device, oid=SYSNAME_OID)
snmp_sysdesc = snmp_helper.snmp_get_oid(my_device, oid=SYSDESC_OID)

output = snmp_helper.snmp_extract(snmp_sysname)
print output

output = snmp_helper.snmp_extract(snmp_sysdesc)
print output
