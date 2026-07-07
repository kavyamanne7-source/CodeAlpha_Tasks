from music21 import stream, note
import random

melody = stream.Stream()

notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]

for i in range(20):
    n = note.Note(random.choice(notes))
    n.quarterLength = random.choice([0.5, 1, 1.5])
    melody.append(n)

melody.write('midi', fp='generated_music.mid')

print("Music generated successfully!")
print("File saved as generated_music.mid")