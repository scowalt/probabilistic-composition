import progression_gen as gen 
from simpleOSC import initOSCClient, sendOSCMsg
import time

ip = "127.0.0.1"
port = 9002
initOSCClient(ip, port)

def play(chord):
	pass

if __name__ == "__main__":
	sendOSCMsg("/note", [1, 66])
	sendOSCMsg("/note", [2, 70])
	sendOSCMsg("/note", [3, 73])
	sendOSCMsg("/note", [4, 90])