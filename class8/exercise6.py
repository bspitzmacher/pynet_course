'''
Class 8 Exercise 6
Use threads and Netmiko to execute 'show version' on each device in the database.
Calculate the amount of time required to do this.
What is the difference in time between executing 'show version' sequentially versus using threads?
'''

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

import threading
import time

def show_ver(net_device):
    device_type = net_device.device_type
    port = net_device.port
    secret = ''
    ip_address = net_device.ip_address
    creds = net_device.credentials
    username = creds.username
    password = creds.password
    
    remote_conn = ConnectHandler(device_type=device_type, ip=ip_address, username=username, password=password, port=port, secret=secret)

    print "=" * 90
    print remote_conn.send_command_expect("show version")
    print "=" * 90

def main():
    django.setup()

    start_timer = datetime.now()
    devices = NetworkDevice.objects.all()

    for net_device in devices:
        net_thread = threading.Thread(target=show_ver, args=(net_device,))
        net_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print some_thread
            some_thread.join()

    total_time = datetime.now() - start_timer
    print "Execution time: {}".format(total_time)
    print "=" * 30

if __name__ == "__main__":
    main()
