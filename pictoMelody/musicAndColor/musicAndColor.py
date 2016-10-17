import sys

sys.path.append('C\Annie\Python2.7\Lib\site-packages')
#sys.path.append('D\Annie\Music\SoundFont\ElPiano1.sf2')

import numpy as np
import cv2
import mingus.core.notes as notes #lets me use notes and use basic functions
import mingus.core.scales as scales #diatonic library doesn't exist. it's just scales
from mingus.containers import MidiInstrument, NoteContainer, Note #use to store generated notes
from mingus.midi import fluidsynth #play notes
import time
import wave


#D\Annie\Code\pictoMelody\musicAndColor\ElPiano1.sf2
#sf2 = 'ElPiano1.sf2'
#fluidsynth.fluid_patchset('D\Annie\Music\SoundFont\ElPiano1.sf2')
#fluidsynth.init('ElPiano1.sf2')
#n = Note("C-5")
#n.channel = 5
#n.velocity = 50
#fluidsynth.play_Note(n)

#print(notes.augment("C"))
#print(scales.get_notes("C"))
#print(Note("C"))
