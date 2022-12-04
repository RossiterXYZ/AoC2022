def SplitValues(_Input):
    #Split by ',' then by '-' and parse into an int
    return [[int(i) for i in x.split('-')] for x in _Input.split(',')]

SubsetCount = 0
OverlapCount = 0
with open("Day4\Input.txt") as InputFile:
    for InputLine in InputFile:
        Elf1, Elf2 = [set(range(Elf[0], Elf[1] + 1)) for Elf in SplitValues(InputLine)]
        if Elf1.issubset(Elf2) or Elf2.issubset(Elf1):
            SubsetCount += 1
        if len(Elf1.intersection(Elf2)) > 0:
            OverlapCount += 1
print(SubsetCount)


print(f'Puzzle 1: Subset = {SubsetCount}')
print(f'Puzzle 2: Overlap = {OverlapCount}')