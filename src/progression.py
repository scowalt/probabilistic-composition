#imports
from simpleOSC import initOSCClient, sendOSCMsg
import time

def bpm_to_delay(bpm):
	return 60.0 / bpm

ip = "127.0.0.1"
port = 9002
BPM = 110

initOSCClient(ip, port)


sendOSCMsg("/vol", [0.90])

c_arp = [261.63, 329.63, 392.00, 523.25]

i=3
j=0
while(1):
	sendOSCMsg("/note", [c_arp[i]])
	j += 0.1
	sendOSCMsg("/roomsize", [j])
	i = (i-1)
	if (i < 0):
		i = 3
	if (j > 1.0):
		j = 0.0
	time.sleep(bpm_to_delay(BPM))