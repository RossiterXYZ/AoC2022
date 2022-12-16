def ParseFile(_File):
    ReturnValue = []
    FileTmp = ""
    with open(_File) as InputFile:
        return [[eval(y) for y in x.split('\n')] for x in InputFile.read().strip().split("\n\n")]


Lists = ParseFile("Day13\Input.txt")

Index = 3

print(Lists[Index][0])
print('')
print(Lists[Index][1])

Part1 = 1
Part2 = 1

print(f'Puzzle 1: {Part1}')
print(f'Puzzle 2: {Part2}')