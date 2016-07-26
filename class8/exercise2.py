'''
Class 8 Exercise 2
Set the vendor field of each NetworkDevice to the appropriate vendor. Save this field to the database.
'''

from net_system.models import NetworkDevice, Credentials

net_devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

for a_device in net_devices:
    if 'pynet-sw' in a_device.device_name:
        a_device.vendor = 'arista'
    elif 'pynet-rtr' in a_device.device_name:
        a_device.vendor = 'cisco'
    else:
        a_device.vendor = 'juniper'
    a_device.save()

for a_device in net_devices:
    print a_device, a_device.vendor
