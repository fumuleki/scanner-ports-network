#!/usr/bin/python3

import os

fields = os.uname()

print('sysversion___________________', fields.sysname)
print('version______________________', fields.version)
print('nodname______________________', fields.nodename)
print('machine_arch_________________', fields.machine)
print('release______________________', fields.release)
