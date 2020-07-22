from pathlib import Path

p=Path('/storage/emulated/0/termux/downloads/a.txt').read_text().splitlines()
c=[i.upper() for i in p]
print(c,sep='\n')
print(*c,sep='\n')