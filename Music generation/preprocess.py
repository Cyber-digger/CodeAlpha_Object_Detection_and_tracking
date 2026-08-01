from music21 import converter, instrument, note, chord
import glob

notes = []

for file in glob.glob("dataset/song2.mid"):
    midi = converter.parse(file)

    parts = instrument.partitionByInstrument(midi)

    if parts:
        elements = parts.parts[0].recurse()
    else:
        elements = midi.flat.notes

    for element in elements:

        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

print("Total notes:", len(notes))