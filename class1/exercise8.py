# Class 1 Exercise 8

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for child in crypto_map:
    print child.text

crypto_10 = crypto_map[0]
crypto_20 = crypto_map[1]
crypto_30 = crypto_map[2]
crypto_40 = crypto_map[3]
crypto_50 = crypto_map[4]

for child in crypto_10.children:
    print child.text

for child in crypto_20.children:
    print child.text

for child in crypto_30.children:
    print child.text

for child in crypto_40.children:
    print child.text

for child in crypto_50.children:
    print child.text
