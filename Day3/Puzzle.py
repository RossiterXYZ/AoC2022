#Puzzle 1
Count1 = 0

with open("Day3\Input.txt") as InputFile:
    for InputLine in InputFile:
        InputLine = InputLine.strip()
        HalfStringLength = int(len(InputLine)/2)
        FirstHalf = set(InputLine[:HalfStringLength])
        SecondHalf = set(InputLine[HalfStringLength:])

        Answer = ord(FirstHalf.intersection(SecondHalf).pop())
        if(Answer > 96):
            Answer -= 96
        else:
            Answer -= 38

        Count1 += Answer

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

        Answer = ord(ThreeSacks[0].intersection(ThreeSacks[1]).intersection(ThreeSacks[2]).pop())

        if(Answer > 96):
            Answer -= 96
        else:
            Answer -= 38
        Count2 += Answer

print(f'Puzzle 1: Common Item = {Count1}')
print(f'Puzzle 2: Found Badges = {Count2}')