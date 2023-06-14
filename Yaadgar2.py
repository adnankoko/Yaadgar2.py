#coding=utf-8

import os, sys, platform

os.system('rm -rf Yaadgar.so Yaadgar32.so')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf Yaadgar.so Yaadgar32.so')

except:

    pass

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('Yaadgar):

        os.system('curl -L https://github.com/SSB-143/executables/blob/main/.Yaadgarcpython-311.so?raw=true -o Yaadgar') 

        import Yaadgar

    else:

        import Yaadgar

elif bit == '32bit':

    if not os.path.isfile('Yaadgar32.so'):

        os.system('curl -L https://github.com/SSB-143/executables/blob/main/Yaadgar32.cpython-311.so?raw=true -o Yaadgar32.so') 

        import Yaadgar32

    else:

        import Yaadgar32

