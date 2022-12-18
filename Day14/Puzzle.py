import copy

def ParseFile(_File):
    with open(_File) as InputFile:
        return [[[int(Value) for Value in Pair.split(',')] for Pair in Line.split(' -> ')] for Line in InputFile.read().strip().split("\n")]

def BuildWall(_Pair1, _Pair2):
    ReturnList = []
    if _Pair1[0] + _Pair1[1] > _Pair2[0] + _Pair2[1]:
        _Pair1, _Pair2 = _Pair2, _Pair1

    for y in range(_Pair1[1], _Pair2[1] + 1):
        for x in range(_Pair1[0], _Pair2[0] + 1):
            ReturnList.append([x, y])
    return ReturnList

def GenerateCave(_Data):
    NewList = [[' ' for x in range(1000)] for y in range(200)]
    for Pairs in _Data:
        for Index in range(len(Pairs) - 1):
            for x, y in BuildWall(Pairs[Index], Pairs[Index + 1]):
                NewList[y][x] = '#'
    return NewList

def CheckPath(_x, _y, _Data):
    if _Data[_y + 1][_x] == " ":
        return [0, 1]
    if _Data[_y + 1][_x - 1] == " ":
        return [-1, 1]
    if _Data[_y + 1][_x + 1] == " ":
        return [1, 1]
    return [0, 0]

def SimulateCaveIn(_Data):
    NewSand = [500, 0]
    SandCount = 0
    while True:
        if NewSand[1] == 199:
            break
        Path = CheckPath(NewSand[0], NewSand[1], _Data)
        NewSand[0] += Path[0]
        NewSand[1] += Path[1]
        if Path == [0,0]:
            _Data[NewSand[1]][NewSand[0]] = '0'
            SandCount += 1
            if _Data[0][500] == '0':
                break
            NewSand = [500, 0]

    #DebugCave(_Data, [0, 0, 1000, 200])
    return SandCount

def DebugCave(_Input, _Bounds):
    String = ''
    for y in range(_Bounds[1], _Bounds[3]):
        for x in range(_Bounds[0], _Bounds[2]):
            if [x, y] == [500, 0]:
                String += "*"
            else:
                String += _Input[y][x]
        String += '\n'
    print(String)

def AddFloor(_Input):
    for Index in range(len(_Input) - 1, -1, -1):
        if '#' in _Input[Index]:
            _Input[Index + 2] = ['#' for _ in _Input[Index]]
            return _Input

WallData = ParseFile("Day14\Input.txt")
WallList = GenerateCave(WallData)

Part1 = SimulateCaveIn(copy.deepcopy(WallList))

WallList = AddFloor(WallList)
Part2 = SimulateCaveIn(copy.deepcopy(WallList))

print(f'Puzzle 1: {Part1}')
print(f'Puzzle 2: {Part2}') #Too Low = 27624