from sys import stdout
from os import path

stdout.write(path.dirname(__file__))
adr = path.dirname(__file__)

file_haldler = open(adr + "/myfile.txt", "w")

file_haldler.write("Halo Word!\n")
file_haldler.write("Ahoj miláčku!\n")

file_haldler.flush()
file_haldler.close()

with open(adr + "/yourfile.txt", "a") as file_haldler:
    c = ord("a")
    while chr(c) != "z":
        file_haldler.write(chr(c))
        c += 1

stdout.write("Konec\n")