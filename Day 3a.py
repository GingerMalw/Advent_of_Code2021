from pathlib import Path

p = Path('C:\\Users\\Malwina\\PycharmProjects\\ChristmasAdventure2021\\Day 3 binary code')
with p.open(mode='r') as f:
    code = f.readlines()

code = [line.strip() for line in code]

gamma_rate = 0
epsilon_rate = 0
# power_cons = int(gamma_rate) * int(epsilon_rate)

# poz = len(code)
# list = len(code[0])
# print(together)


def checking(binary_list, x):
    zero = 0
    one = 0
    for l in binary_list:
        if l[x] == "0":
            zero += 1
        elif l[x] == "1":
            one += 1
    if zero <= one:
        return '1'
    else:
        return '0'


def unchecking(binary_list, x):
    zero = 0
    one = 0
    for l in binary_list:
        if l[x] == "0":
            zero += 1
        elif l[x] == "1":
            one += 1
    if zero < one:
        return '0'
    else:
        return '1'


lista_pozycji = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# for poz in range(0, len(code[0])):
for poz in lista_pozycji:
    # print(F"poz: {poz}")
    # gamma_rate = F"{gamma_rate}{checking(binary_list=code, x=poz)}" - hmmm
    gamma_rate = F"{gamma_rate}{checking(binary_list=code, x=poz)}"
    gamma_rate2 = int(gamma_rate, 2)
    epsilon_rate = F"{epsilon_rate}{unchecking(binary_list=code, x=poz)}"
    epsilon_rate2 = int(epsilon_rate, 2)

power_cons = int(gamma_rate2) * int(epsilon_rate2)

print(f"gamma rate  = {gamma_rate}")
print(f"epsilon rate  = {epsilon_rate}")

print(f"gamma rate (2) = {gamma_rate2}")
print(f"epsilon rate (2) = {epsilon_rate2}")
print(f"power = {power_cons}")

# print(F"Rezultat binarnie: {result}\nRezultat dziesietnie {int(result, 2)}")


