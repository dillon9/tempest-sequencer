
from random import randint
import sys

def makeSong():
    c = 0
    song = ""
    a = "ABCDEFG"
    b = "12345678"
    d = "#b"

    while c < randint(int(sys.argv[1]), int(sys.argv[2])):
        song += a[randint(0, len(a)-1)]
        if randint(0, 1):
            song += d[randint(0, 1)]
        song += b[randint(0, len(b)-1)]
        if randint(0, 10) >= 7:
            song += " - " if randint(0, 1) else " . "
        else:
            song += " "
        c += 1

    return song.strip().replace("E#", "Eb").replace("Fb","F#").replace("B#", "Bb").replace("Cb", "C#")


c = 0
while c < int(sys.argv[3]):
    fob = open(str(c) + ".txt", "w")
    fob.write(makeSong())
    fob.close()
    c += 1
