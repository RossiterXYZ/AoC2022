# Second Solution as I accidentally typoed when entering the solution so thought I was wrong the whole time.
# But in fact, it was always right so when my second solution had the same answers I just tried to submit again.

def SplitValues(_Input):
    #Split by ',' then by '-' and parse into an int
    return [[int(i) for i in x.split('-')] for x in _Input.strip().split(',')]

SubsetCount = 0
with open("Day4\Input.txt") as InputFile:
    for InputLine in InputFile:
        Elf1, Elf2 = SplitValues(InputLine)
        if (Elf1[0] <= Elf2[0] and Elf1[1] >= Elf2[1]) or (Elf1[0] >= Elf2[0] and Elf1[1] <= Elf2[1]):
            SubsetCount += 1
        print(f'Input: {InputLine.strip()}\n{Elf1}\n{Elf2}\n')
print(SubsetCount)
