# Class 4 Exercise 1
# Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2.

import paramiko
import time
from getpass import getpass

ip_addr = '50.76.53.27'
username = 'pyclass'
password = getpass()
port = 8022 # default port 22 is rtr1, 8022:rtr2, 9822:srx

remote_conn_set=paramiko.SSHClient()
remote_conn_set.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_set.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

remote_conn = remote_conn_set.invoke_shell()
time.sleep(1)

#outp = remote_conn.send("terminal length 0\n")
#outp = remote_conn.recv(65535)
#print outp

outp = remote_conn.send("terminal length 0\n")
time.sleep(1)
outp = remote_conn.send("show version\n")
time.sleep(1)
outp = remote_conn.recv(65535)
print outp
