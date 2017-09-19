#!/usr/bin/python3

import os
#uncomment for nvidia cards
os.system('nvidia-smi -q |grep -i "gpu current temp"|awk \'{total += $5; count++} END {print total/count}\'')
#uncomment for amd cards
#os.system('sensors |grep temp1|awk \'{print $2}\'|cut -f2 -d\'+\'|cut -f1 -d\'.\'|awk \'{total += $1; count++} END {print total/count}\'')
