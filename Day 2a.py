from pathlib import Path

p = Path('C:\\Users\\Malwina\\PycharmProjects\\ChristmasAdventure2021\\Day 2_diving')
with p.open(mode='r') as f:
    all_list = f.readlines()

h = 0
d = 0
for el in all_list:
    el_split = el.split()
    if el_split[0] == 'forward':
        h += int(el_split[1])
    elif el_split[0] == 'down':
        d += int(el_split[1])
    elif el_split[0] == "up":
        d -= int(el_split[1])
print(h)
print(d)
depth = d*h
print(depth)
