# Class 2 Exercise 3
# Author Brian Spitzmacher
# Convert code to class-based solution

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class Telnet:

    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

        try:
            self.remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")

    def login(self):
        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(self.username + '\n')
        output += self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.password + '\n')
        return output

    def send_command(self, cmd="\n", sleep_time=1):
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(sleep_time)
        return self.remote_conn.read_very_eager()

    def disable_paging(self, paging_cmd='terminal length 0'):
        return self.send_command(paging_cmd)

    def conn_close(self):
        self.remote_conn.close()

def main():

    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()

    conn_a = Telnet(ip_addr, username, password)
    conn_a.login()
    time.sleep(1)
    conn_a.send_command()
    conn_a.disable_paging()
    output = conn_a.send_command('show ip int br')
    print "\n\n"
    print output
    print "\n\n"
    conn_a.conn_close()


if __name__ == "__main__":
    main()

