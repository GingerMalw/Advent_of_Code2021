from pathlib import Path

p = Path('C:\\Users\\Malwina\\PycharmProjects\\ChristmasAdventure2021\\Day 1_sonar')
with p.open(mode='r') as f:
    l = f.readlines()

l2 = list()
# poz = 1
# x = int(l[poz].strip()) + int(l[poz+1].strip()) + int(l[poz+2].strip())
for e in l:
    l2.append(int(e.strip()))

res = 0
times = len(l2) - 3
for t in range(times):
    x1 = sum(l2[t:(t+3)])
    x2 = sum(l2[(t+1):(t+4)])
    if  x2 > x1:
       res += 1
print(res)