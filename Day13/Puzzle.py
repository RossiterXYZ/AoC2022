def ParseFile(_File):
    with open(_File) as InputFile:
        return [[eval(y) for y in x.split('\n')] for x in InputFile.read().strip().split("\n\n")]

def CompareValues(_a, _b, _ColdStart = True):
    if not _ColdStart:
        aType = type(_a) is int
        bType = type(_b) is int

        if aType and bType:
            return max(-1, min(_b - _a, 1))

        if aType:
            _a = [_a]
        if bType:
            _b = [_b]

    ListLength = max(len(_a), len(_b))
    for Index in range(ListLength):

        if Index >= len(_a) and Index < len(_b):
            return 1
        if Index < len(_a) and Index >= len(_b):
            return -1

        Value = CompareValues(_a[Index], _b[Index], False)
        if Value in [-1, 1]:
            return Value

def ComparePackets(_Input):
    ValidPairs = 0

    for Index in range(len(_Input)):
        Value = CompareValues(_Input[Index][0], _Input[Index][1])
        if Value > 0:
            ValidPairs += Index + 1

    return ValidPairs

def PreparePart2(_Input):
    NewList = [[[2]], [[6]]]
    for Index in range(len(_Input)):
        NewList.append(_Input[Index][0])
        NewList.append(_Input[Index][1])
    return NewList

#Seems Python sort doesn't work the way I expected. It's BubbleSort time.
def SortPackets(_Input):
    for OuterLoop in range(len(_Input)):
        for Index in range(len(_Input) -1):
            if CompareValues(_Input[Index], _Input[Index+1]) > 0:
                _Input[Index], _Input[Index+1] = _Input[Index+1], _Input[Index]
    return _Input

PacketList = ParseFile("Day13\Input.txt")

Part1 = ComparePackets(PacketList)

PacketList = PreparePart2(PacketList)
TmpSorted = list(reversed(SortPackets(PacketList)))
CodeIndicies = 1
for Index in range(len(TmpSorted)):
    if TmpSorted[Index] in [[[2]], [[6]]]:
        CodeIndicies *= (1 + Index)
Part2 = CodeIndicies

print(f'Puzzle 1: {Part1}')
print(f'Puzzle 2: {Part2}')