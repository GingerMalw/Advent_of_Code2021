from pathlib import Path

p = Path('C:\\Users\\Malwina\\PycharmProjects\\ChristmasAdventure2021\\Day 1_sonar')
with p.open(mode='r') as f:
    l = f.readlines()

x = int(l[0].strip())
res = 0
for element in l:
    if int(element.strip()) > x:
        res += 1
    x = int(element.strip())
print(res)