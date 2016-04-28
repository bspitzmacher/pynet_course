# Class 1 Exercise 10

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

no_aes = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"transform-set [^AES]")

for child in no_aes:
    print child.text

crypto1 = no_aes[0]

for child in crypto1.children:
    print child.text
