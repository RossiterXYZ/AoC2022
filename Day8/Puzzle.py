def ParseFile(_File):
    ReturnValue = []
    with open(_File) as InputFile:
        for InputLine in InputFile:
            ReturnValue.append([int(x) for x in InputLine.strip()])
    return ReturnValue

def SplitValues(_Line):
    return _Line.strip().split('')

def CountVisibleTrees(_TreeArray):
    SeenList = [[0 for _ in range(len(_TreeArray[0]))] for _ in range(len(_TreeArray))]
    for yIndex in range(len(_TreeArray)):
        xFound = -1
        yFound = -1
        x_Found = -1
        y_Found = -1
        for xIndex in range(len(_TreeArray)):
            TreeIndex = len(_TreeArray) - 1
            if _TreeArray[xIndex][yIndex] > xFound: #Right
                SeenList[xIndex][yIndex] = SeenList[xIndex][yIndex] | 1
                xFound = _TreeArray[xIndex][yIndex]
            if _TreeArray[yIndex][xIndex] > yFound: #Down
                SeenList[yIndex][xIndex] = SeenList[yIndex][xIndex] | 1
                yFound = _TreeArray[yIndex][xIndex]
            if _TreeArray[TreeIndex - xIndex][TreeIndex - yIndex] > x_Found: #Left
                SeenList[TreeIndex - xIndex][TreeIndex - yIndex] = SeenList[TreeIndex - xIndex][TreeIndex - yIndex] | 1
                x_Found = _TreeArray[TreeIndex - xIndex][TreeIndex - yIndex]
            if _TreeArray[TreeIndex - yIndex][TreeIndex - xIndex] > y_Found: #Up
                SeenList[TreeIndex - yIndex][TreeIndex - xIndex] = SeenList[TreeIndex - yIndex][TreeIndex - xIndex] | 1
                y_Found = _TreeArray[TreeIndex - yIndex][TreeIndex - xIndex]

    SeenCount = 0
    for x in range(len(_TreeArray)):
        for y in range(len(_TreeArray)):
            SeenCount += SeenList[x][y]
    return SeenCount

def FindBestTreeScore(_TreeArray):
    BestScore = 0
    for x in range(len(_TreeArray)):
        for y in range(len(_TreeArray)):
            Score = TreeScore(_TreeArray, x, y)
            if Score > BestScore:
                BestScore = Score
    return BestScore

def TreeScore(_TreeArray, _x, _y):
    TreeHeight = _TreeArray[_x][_y]
    Distance = [0, 0, 0, 0]
    Offsets = [{'x': -1, 'y': 0}, {'x': 0, 'y': -1}, {'x': 1, 'y': 0}, {'x': 0, 'y': 1}]
    Exit = [False, False, False, False]
    for CheckDistance in range(1, len(_TreeArray)):
        for Index in range(4):
            if Exit[Index]:
                continue
            X = _x + Offsets[Index]['x'] * CheckDistance
            Y = _y + Offsets[Index]['y'] * CheckDistance
            if X not in range(len(_TreeArray)) or Y not in range(len(_TreeArray)):
                Exit[Index] = True
                continue
            Distance[Index] = CheckDistance
            if _TreeArray[X][Y] >= TreeHeight:
                Exit[Index] = True
        if Exit == [True, True, True, True]:
            break

    return Distance[0] * Distance[1] * Distance[2] * Distance[3]

TreeValues = ParseFile("Day8\Input.txt")
print(f'Puzzle 1: Visible Trees = {CountVisibleTrees(TreeValues)}')
print(f'Puzzle 2: Best Visibility = {FindBestTreeScore(TreeValues)}')