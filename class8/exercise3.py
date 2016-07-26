'''
Class 8 Exercise 3
Create two new test NetworkDevices in the database.
Use both direct object creation and
the .get_or_create() method to create the devices.
'''



# Edit the load_devices.py file
from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    pynet_test1 = NetworkDevice(
        device_name='pynet-test1',
        device_type='cisco_ios',
        ip_address='184.105.247.77',
        port=22,
    )
    pynet_rtr1.save()
    
    pynet_test2 = NetworkDevice.objects.get_or_create(
        device_name='pynet-test2',
        device_type='pan_os',
        ip_address='184.105.247.78',
        port=22,
    )
    print pynet_test2

if __name__ == "__main__":
    main()
