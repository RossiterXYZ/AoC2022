def ParseFile(_File):
    ReturnValue = []
    FileTmp = ""
    with open(_File) as InputFile:
        FileTmp = InputFile.read()
    return [list(Individual.strip()) for Individual in FileTmp.strip().split("\n")]

def FindLocation(_Field, _Target):
    for y in range(len(_Field)):
        for x in range(len(_Field[0])):
            if _Field[y][x] == _Target:
                return [x, y]

def CalculatePath(_Field, _Target, _Distance, _Direction):
    Stack = [[*_Target, 4], 0]
    CurrentDistance = 0
    DirectionMatrix = [{'x': 1, 'y': 0}, {'x': 0, 'y': 1}, {'x': -1, 'y': 0}, {'x': 0, 'y': -1}]
    CharMatrix = ['<', '^', '>', 'V', 'E']

    while len(Stack) > 0:
        Cell = Stack.pop(0)
        if len(Stack) <= 0:
            continue
        if type(Cell) is int:
            CurrentDistance += 1
            Stack.append(CurrentDistance)
            #FancyPath(DistanceField, DirectionField)
            continue
        if not _Direction[Cell[1]][Cell[0]] == " ":
            continue

        _Direction[Cell[1]][Cell[0]] = CharMatrix[Cell[2]]
        _Distance[Cell[1]][Cell[0]] = CurrentDistance
        for Index in range(4):
            if not Cell[1]+DirectionMatrix[Index]["y"] in range(len(_Field)) or not Cell[0]+DirectionMatrix[Index]["x"] in range(len(_Field[0])):
                continue
            Char1 = ord(_Field[Cell[1]][Cell[0]])
            Char2 = ord(_Field[Cell[1]+DirectionMatrix[Index]["y"]][Cell[0]+DirectionMatrix[Index]["x"]])
            if Char1 <= Char2+1:
                Stack.append([Cell[0]+DirectionMatrix[Index]["x"], Cell[1]+DirectionMatrix[Index]["y"], Index])

def ShortestPath(_Height, _Distance):
    Smallest = 999
    for y in range(len(_Height)):
        for x in range(len(_Height[0])):
            if _Height[y][x] == 'a' and _Distance[y][x] < Smallest:
                Smallest = _Distance[y][x]
    return Smallest

HeightField = ParseFile("Day12\Input.txt")
DistanceField = [[999_999 for _ in range(len(HeightField[0]))] for _ in range(len(HeightField))]
DirectionField = [[' ' for _ in range(len(HeightField[0]))] for _ in range(len(HeightField))] #It wasn't needed, Made a nice visual though

StartingSquare = FindLocation(HeightField, "S")
EndingSquare = FindLocation(HeightField, "E")
HeightField[EndingSquare[1]][EndingSquare[0]] = 'z'
HeightField[StartingSquare[1]][StartingSquare[0]] = 'a'

CalculatePath(HeightField, EndingSquare, DistanceField, DirectionField)

Part1 = DistanceField[StartingSquare[1]][StartingSquare[0]]
Part2 = ShortestPath(HeightField, DistanceField)

print(f'Puzzle 1: {Part1}')
print(f'Puzzle 2: {Part2}')