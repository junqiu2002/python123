from pathlib import Path

for f in Path('/usr/bin').iterdir():
    print(f)
