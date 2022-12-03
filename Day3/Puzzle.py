#Puzzle 1
Count1 = 0

def ElvesValue(_Value):
    Value = ord(_Value)
    if(Value > 96):
        Value -= 96
    else:
        Value -= 38
    return Value

with open("Day3\Input.txt") as InputFile:
    for InputLine in InputFile:
        InputLine = InputLine.strip()
        HalfStringLength = int(len(InputLine)/2)
        FirstHalf = set(InputLine[:HalfStringLength])
        SecondHalf = set(InputLine[HalfStringLength:])

        Answer = FirstHalf.intersection(SecondHalf).pop()
        Count1 += ElvesValue(Answer)

Iterator = 0
Count2 = 0
ThreeSacks = [{},{},{}]
with open("Day3\Input.txt") as InputFile:
    for InputLine in InputFile:
        InputLine = InputLine.strip()
        ThreeSacks[Iterator] = set(InputLine)
        if Iterator < 2:
            Iterator += 1
            continue
        else:
            Iterator = 0

        Answer = ThreeSacks[0].intersection(ThreeSacks[1]).intersection(ThreeSacks[2]).pop()
        Count2 += ElvesValue(Answer)

print(f'Puzzle 1: Common Item = {Count1}')
print(f'Puzzle 2: Found Badges = {Count2}')