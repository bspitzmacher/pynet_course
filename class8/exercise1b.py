'''
Class 8 Exercise 1b
Update the NetworkDevice objects such that each NetworkDevice links to the correct Credentials.
'''

from net_system.models import NetworkDevice, Credentials
import django

django.setup()
net_devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

std_creds = creds[0]
arista_creds = creds[1]

for a_device in net_devices:
    if 'pynet-sw' in a_device.device_name:
        a_device.credentials = arista_creds
    else:
        a_device.credentials = std_creds
    a_device.save()

for a_device in net_devices:
    print a_device, a_device.credentials
