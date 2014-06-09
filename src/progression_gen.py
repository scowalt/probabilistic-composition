import numpy as np
import random
from mingus.core import *


transition_probabilities = np.array(
	[[0.0, 0.15, 0.25, 0.25, 0.20, 0.1, 0.05],
	 [0.0, 0.10, 0.00, 0.20, 0.45, 0.0, 0.25],
	 [0.0, 0.00, 0.10, 0.00, 0.00, 0.9, 0.00],
	 [0.1, 0.20, 0.00, 0.10, 0.50, 0.0, 0.10],
	 [0.6, 0.00, 0.00, 0.00, 0.30, 0.0, 0.10],
	 [0.0, 0.40, 0.00, 0.40, 0.00, 0.2, 0.00],
	 [0.7, 0.00, 0.00, 0.00, 0.10, 0.0, 0.20]]
)

major_chords = ["I", "IIm", "IIIm", "IV", "V", "VIm", "VIIdim"]

def generate(length=8, start_chord=None, resolve=True):
	progression = np.empty(length, object)
	if start_chord is None:
		start_chord = 1
	progression[0] = start_chord
	
	for i in range(1, length):
		progression[i] = next_chord(progression[i-1])

	if resolve and progression[length - 1] is not 1:
		return generate(length, start_chord, resolve)

	return int_to_roman(progression)

def int_to_roman(progression):
	for i in range(0, progression.size):
		progression[i] = major_chords[progression[i]-1]
	return progression

def next_chord(current_chord):
	next_prob = transition_probabilities[current_chord - 1]
	r = random.random()
	for i in range(0, next_prob.size):
		r = r - next_prob[i]
		if r < 0:
			return (i+1)
	raise Exception("No chord selected. Are the probabilities correct?")

if __name__ == "__main__":
	print progressions.to_chords(generate(), "C")