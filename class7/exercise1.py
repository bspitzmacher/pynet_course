'''
Class 7 Exercise 1
Use Arista's eAPI to obtain 'show interfaces' from the switch.
Parse the 'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields 
for each of the interfaces on the switch.  Accomplish this using Arista's pyeapi library.
'''

import pyeapi

def pyeapi_result(output):
    '''
    This extracts the 'result' value from the pyeapi 'show interfaces' output
    '''
    return output[0]['result']

def main():

    pynet_sw2 = pyeapi.connect_to('pynet-sw2')

    show_int = pynet_sw2.enable("show interfaces")
    interfaces = pyeapi_result(show_int)

    # Strip off unneeded dictionary
    interfaces = interfaces['interfaces']

    # inOctets/outOctets are fields inside 'interfaceCounters' dict
    data_stats = {}
    for interface, int_values in interfaces.items():
        int_counters = int_values.get('interfaceCounters', {})
        data_stats[interface] = (int_counters.get('inOctets'), int_counters.get('outOctets'))

    # Print output data in table format with columns 20 spaces wide
    print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
    for intf, octets in data_stats.items():
        print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])

    print

if __name__ == '__main__':
    main()
