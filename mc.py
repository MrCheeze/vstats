import os
import amulet
from amulet.api.block import Block
import glob

SCALE = 6820/12288

print("Deleting existing chunks to prevent lighting issues...")
for f in os.listdir("C:\\Users\\Matthew\\AppData\\Roaming\\.minecraft\\saves\\New World\\region"):
    print("Deleting " + f)
    os.remove("C:\\Users\\Matthew\\AppData\\Roaming\\.minecraft\\saves\\New World\\region\\"+f)

print("Loading level...")
level = amulet.load_level("C:\\Users\\Matthew\\AppData\\Roaming\\.minecraft\\saves\\New World")

dimension = "minecraft:overworld"
game_version = ("java", (1, 21, 6))
stone = Block("minecraft", "stone")

for fname in glob.glob('MainFieldOut/*.obj'):
    print("Reading", fname)
    f = open(fname)
    for line in f:
        if line != '\n':
            _, x, y, z = line.split()
            x = round(int(x) * SCALE)
            y = round(int(y) * SCALE)
            z = round(int(z) * SCALE)
            level.set_version_block(
                x,
                y,
                z,
                dimension,
                game_version,
                stone,
            )
    print(x, y, z)
    print("Saving world...")
    f.close()
    level.save()
level.close()
print("Done.")
