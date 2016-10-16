import sys

sys.path.append('C\Annie\Python2.7\Lib\site-packages')

import numpy as np
import cv2
import mingus.core.notes as notes #lets me use notes and use basic functions
import mingus.core.scales as scales #diatonic library doesn't exist. it's just scales
from mingus.containers import Note #use to store generated notes
from mingus.midi import fluidsynth #play notes

print(notes.augment("C"))
print(scales.get_notes("C"))
print(Note("C"))

fluidsynths.play_Note(Note("C-5"))

#fuck it fluidsynth sucks I'm going to use javascript
