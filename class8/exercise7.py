'''
Class 8 Exercise 7
Repeat exercise #6 except use processes.
'''

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

from multiprocessing import Process, current_process
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

    proc_list = []
    for net_device in devices:
        net_proc = Process(target=show_ver, args=(net_device,))
        net_proc.start()
        proc_list.append(net_proc)

    for iter_proc in proc_list:
        print iter_proc
        iter_proc.join()

    total_time = datetime.now() - start_timer
    print "Execution time: {}".format(total_time)
    print "=" * 30

if __name__ == "__main__":
    main()
