'''
Class 8 Exercise 5
Use Netmiko to connect to each of the devices in the database.
Execute 'show version' on each device. 
Calculate the amount of time required to do this.
Note, your results will be more reliable if you use Netmiko's send_command_expect() method.
There is an issue with the Arista vEOS switches and Netmiko's send_command() method.
'''

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()

    start_timer = datetime.now()

    devices = NetworkDevice.objects.all()
    for net_device in devices:
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

    total_time = datetime.now() - start_timer
    print "Execution time: {}".format(total_time)
    print "=" * 30

if __name__ == "__main__":
    main()
