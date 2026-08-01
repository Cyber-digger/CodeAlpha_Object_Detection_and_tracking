import numpy as np

sequence_length = 100

pitchnames = sorted(set(notes))

note_to_int = dict(
    (note, number) for number, note in enumerate(pitchnames)
)

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):

    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append(
        [note_to_int[char] for char in sequence_in]
    )

    network_output.append(note_to_int[sequence_out])

n_patterns = len(network_input)

network_input = np.reshape(
    network_input,
    (n_patterns, sequence_length, 1)
)

network_input = network_input / float(len(pitchnames))