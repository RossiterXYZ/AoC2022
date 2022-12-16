def ParseFile(_File):
    ReturnValue = []
    FileTmp = ""
    with open(_File) as InputFile:
        return [[eval(y) for y in x.split('\n')] for x in InputFile.read().strip().split("\n\n")]

def CompareValues(_a, _b):
    #If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
    #If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
    #If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].

    if _a == None and not _b == None:
        return -1
    if _b == None and not _a == None:
        return 1

    aType = type(_a) is int
    bType = type(_b) is int

    if aType and bType and not _a == _b:
        return max(-1, min(_b - _a, 1))

    return aType, bType

def ComparePackets(_Input):
    ValidPairs = 0
    Index = 0

    #ValidPairs = CompareValues(_Input[Index][0], _Input[Index][1])
    ValidPairs = CompareValues(1, 1)

    return ValidPairs

PacketList = ParseFile("Day13\Input.txt")

print(ComparePackets(PacketList))

Part1 = 1
Part2 = 1

print(f'Puzzle 1: {Part1}')
print(f'Puzzle 2: {Part2}')