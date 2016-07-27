import pyeapi

def main():
    pynet_sw2 = pyeapi.connect_to('pynet-sw2')

    show_int = pynet_sw2.enable("show interfaces")

    show_int = show_int[0]

    show_int = show_int['result']

    show_int = show_int['interfaces']

    show_int.keys()
    mgmt1 = show_int['Management1']
    eth1 = show_int['Ethernet1']
    eth2 = show_int['Ethernet2']
    eth3 = show_int['Ethernet3']
    eth4 = show_int['Ethernet4']
    eth5 = show_int['Ethernet5']
    eth6 = show_int['Ethernet6']
    eth7 = show_int['Ethernet7']

    mgmt1_counters = mgmt1['interfaceCounters']
    eth1_counters = eth1['interfaceCounters']
    eth2_counters = eth2['interfaceCounters']
    eth3_counters = eth3['interfaceCounters']
    eth4_counters = eth4['interfaceCounters']
    eth5_counters = eth5['interfaceCounters']
    eth6_counters = eth6['interfaceCounters']
    eth7_counters = eth7['interfaceCounters']

    mgmt1_inOctets = mgmt1_counters['inOctets']
    mgmt1_outOctets = mgmt1_counters['outOctets']
    eth1_inOctets = eth1_counters['inOctets']
    eth1_outOctets = eth1_counters['outOctets']
    eth2_inOctets = eth2_counters['inOctets']
    eth2_outOctets = eth2_counters['outOctets']
    eth3_inOctets = eth3_counters['inOctets']
    eth3_outOctets = eth3_counters['outOctets']
    eth4_inOctets = eth4_counters['inOctets']
    eth4_outOctets = eth4_counters['outOctets']
    eth5_inOctets = eth5_counters['inOctets']
    eth5_outOctets = eth5_counters['outOctets']
    eth6_inOctets = eth6_counters['inOctets']
    eth6_outOctets = eth6_counters['outOctets']
    eth7_inOctets = eth7_counters['inOctets']
    eth7_outOctets = eth7_counters['outOctets']

    print mgmt1_outOctets
    print mgmt1_inOctets
    print eth1_inOctets
    print eth1_outOctets
    print eth2_inOctets
    print eth2_outOctets
    print eth3_inOctets
    print eth3_outOctets
    print eth4_inOctets
    print eth4_outOctets
    print eth5_inOctets
    print eth5_outOctets
    print eth6_inOctets
    print eth6_outOctets
    print eth7_inOctets
    print eth7_outOctets

if __name__ == "__main__":
    main()
