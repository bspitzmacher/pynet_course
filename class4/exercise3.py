# Class 4 exercise 3
# Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.

import pexpect
from getpass import getpass

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022 # port 22 is rtr1, 8022:rtr2, 9822:srx
    password = getpass()

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3
    ssh_conn.expect('assword:')
    ssh_conn.sendline(password)
    
    ssh_conn.expect('#')
    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect('#')
    ssh_conn.sendline('show ip int br')
    ssh_conn.expect('pynet-rtr2#')
    
    print ssh_conn.before
    
if __name__ == "__main__":
    main()
