import progression_gen as gen 
from simpleOSC import initOSCClient, sendOSCMsg
from time import sleep
from mingus.core import *

ip = "127.0.0.1"
port = 9002
initOSCClient(ip, port)
chord_octave = 5

def play_chord(chord):
	sendOSCMsg("/note", [1, note_to_midi(chord[0])])
	sendOSCMsg("/note", [2, note_to_midi(chord[1])])
	sendOSCMsg("/note", [3, note_to_midi(chord[2])])

def note_to_midi(n):
	return notes.note_to_int(n) + chord_octave * 12

if __name__ == "__main__":
	# sendOSCMsg("/note", [1, 42])
	# sendOSCMsg("/note", [2, 58])
	# sendOSCMsg("/note", [3, 61])
	# sendOSCMsg("/note", [4, 78])
	g = gen.generate()
	print g
	p = progressions.to_chords(g, "C")
	for c in p:
		play_chord(c)
		sleep(1)