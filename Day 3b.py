from pathlib import Path

p = Path('C:\\Users\\Malwina\\PycharmProjects\\ChristmasAdventure2021\\Day 3 binary code')


def load_input():
    p = Path(__file__).parent / "Day 3 binary code"
    with p.open(mode='r') as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
    return lines


def common_bit_on_position(lines, pos, mode):
    ones = 0
    zeros = 0
    c_lines = len(lines)
    counter = 0
    for line in lines:
        if line[pos] == '1':
            ones += 1
        else:
            zeros += 1
        counter += 1
        if zeros > c_lines / 2 or ones > c_lines / 2:
            if mode == 'm':
                res = 1 if ones > zeros else 0
            elif mode == 'l':
                res = 1 if ones < zeros else 0
            return res


def common_bit_on_position2(lines, pos, mode):
    ones = 0
    zeros = 0
    c_lines = len(lines)
    counter = 0
    for line in lines:
        if line[pos] == '1':
            ones += 1
        else:
            zeros += 1
        counter += 1
        # if zeros >= c_lines / 2  or ones >= c_lines / 2 : #Conside 0 0 1 1
    if mode == 'o':
        res = 1 if ones >= zeros else 0
    elif mode == 'co2':
        res = 0 if ones >= zeros else 1
    return res


def task2():
    m_lines = load_input()
    l_lines = load_input()
    c_bits = len(m_lines[0])
    o2 = ''
    co2 = ''
    for pos in range(0, c_bits):

        # print(F"POS: {pos}")

        if len(m_lines) > 1:
            # print(F"m_lines length: {len(m_lines)}")
            m_bit = common_bit_on_position2(lines=m_lines, pos=pos, mode='o')
            # print(F"m_bit: {m_bit}")
            m_lines = [x for x in m_lines if x[pos] == str(m_bit)]
            # print(F"m_lines length after reduction: {len(m_lines)}")
            # print(m_lines)

        if len(l_lines) > 1:
            # print(F"l_lines length: {len(l_lines)}")
            l_bit = common_bit_on_position2(lines=l_lines, pos=pos, mode='co2')
            # print(F"l_bit: {l_bit}")
            l_lines = [x for x in l_lines if x[pos] == str(l_bit)]
            # print(F"l_lines length after reduction: {len(l_lines)}")
            # print(l_lines)

    if len(m_lines) == 1:
        o2 = m_lines[0]
        print(F"O2: {o2}")
    if len(l_lines) == 1:
        co2 = l_lines[0]
        print(F"CO2: {co2}")

    o2_dec = int(o2, 2)
    co2_dec = int(co2, 2)

    # return F"Result: {int(o2, 2) * int(co2, 2)}"
    print(o2_dec * co2_dec)


task2()