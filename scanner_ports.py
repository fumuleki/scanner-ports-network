#!/usr/bin/python3

import socket

def scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.settimeout(0.5)
    except socket.error:
        return False
    return True

host = input('GIVE ME A HOST NAME : ')

def check_port(host):
    for i in range(1, 5000):
        if scan(host, i):
            print('The port :',i,' at :', host,' is open')
        print('The port :',i,' at :', host,' is close')

check_port(host)
