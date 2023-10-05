import os

def mac_ping(ip):
    '''
    Return true if the ip can be ping
    '''
    return 1 == os.system("ping -t 5 " + ip)