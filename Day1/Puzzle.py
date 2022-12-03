CurrentElfCalories = 0
ElfData = []

with open("Day1\Input.txt") as InputFile:
    for InputLine in InputFile:
        if InputLine == "\n":
            ElfData.append(CurrentElfCalories)
            CurrentElfCalories = 0
        else:
            CurrentElfCalories += int(InputLine)
ElfData.sort(reverse=True)

print(f'Puzzle 1: Highest Elf = {ElfData[0]}')
print(f'Puzzle 2: Highest 3 Elves = {ElfData[0] + ElfData[1] + ElfData[2]}')