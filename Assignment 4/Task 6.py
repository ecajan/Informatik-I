#!/usr/bin/env python3
#import re

def is_valid_IPv4_octet(octet):
    try:
        octet = int(octet)
        if octet >= 0 and octet <= 255:
            return True
        else:
            return False
    except ValueError:
        return False  

def is_valid_IPv4(ip):
    if len(ip.split(".")) == 4:
        for octet in ip.split("."):
            if is_valid_IPv4_octet(octet) != True:
                return False    
    else:
        return False
    return True


def is_valid_IPv6_hextet(hextet):
    try:
        if type(int(hextet, 16)) == int and int(hextet, 16) >= 0 and int(hextet, 16) <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False     

def is_valid_IPv6(ip):
    if len(ip.split(":")) == 8:
        for hextet in ip.split(":"):
            if len(hextet) >= 1 and len(hextet) <= 4 and is_valid_IPv6_hextet(hextet) != True:
                return False    
    else:
        return False
    return True

def is_valid_IP(ip):
    if is_valid_IPv4 == True or is_valid_IPv6 == True:
        return True
    else:
        return False

# You should look at task/test.py and extend the test suite we provided!

#is_valid_IPv6("2001:0db8:85a3:0:0000:8a2e:0370:7334")