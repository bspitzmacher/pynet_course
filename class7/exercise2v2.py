import pyeapi
import sys

def result(output):
    
    return output[0]['result']

def check_exists(host, vlan_id):
    vlan_id = str(vlan_id)
    cmd = 'show vlan id %s' % vlan_id
    try:
        response = host.enable(cmd)
        check_vlan = result(response)['vlans']
        return check_vlan[vlan_id]['name']
    except (pyeapi.eapilib.CommandError, KeyError):
        pass

    return False


def configure_vlan(host, vlan_id, vlan_name=None):

    command_str1 = 'vlan %s' % vlan_id
    cmd = [command_str1]
    if vlan_name is not None:
        command_str2 = 'name %s' % vlan_name
        cmd.append(command_str2)
    return host.config(cmd)


def main():
    host = pyeapi.connect_to('"pynet-sw2"')
    '''
    sys.argv[1] takes the first possition of the value being pass.
    '''
    
    if (sys.argv[1]) =='name':
        vlan_id= sys.argv[3]
        vlan_name = sys.argv[2]
        check_vlan = check_exists(host, vlan_id)
        if check_vlan:
            if vlan_name is not None and check_vlan != vlan_name:
                print "VLAN already exists, setting VLAN name"
                configure_vlan(host, vlan_id, vlan_name)
            else:
                print "VLAN already exists, no action required"
        else:
            print "Adding VLAN including vlan_name (if present)"
            configure_vlan(host, vlan_id, vlan_name)



    if (sys.argv[1]) =='remove':
        vlan_id = sys.argv[2]
        check_vlan = check_exists(host, vlan_id)
        if check_vlan: # If it exist it will return TRUE causing the loop to continue
            print "VLAN exists, removing it"
            command_str = 'no vlan %s' % vlan_id
            host.config([command_str])
        else:
            print "VLAN does not exist, no action required"                

if __name__ == "__main__":
    main()
