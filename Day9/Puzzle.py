def ParseFile(_File):
    ReturnValue = []
    with open(_File) as InputFile:
        for InputLine in InputFile:
            Tmp = InputLine.strip().split(' ')
            ReturnValue.append({'Direction': Tmp[0], 'Count': int(Tmp[1])})
    return ReturnValue

def FindStringPath(_Path, _Length):
    WholeString = [{'x': 0, 'y': 0} for _ in range(_Length)]
    TailLocations = set()
    Movement = {
        'R': {'x': 1 , 'y': 0 },
        'L': {'x': -1, 'y': 0 },
        'D': {'x': 0 , 'y': -1},
        'U': {'x': 0 , 'y': 1 },
    }

    for Step in _Path:
        Direction = Step["Direction"]
        for _ in range(Step["Count"]):
            WholeString[0]["x"] += Movement[Direction]["x"]
            WholeString[0]["y"] += Movement[Direction]["y"]
            for Index in range(1, _Length):
                TailStep = SimulateTail(WholeString[Index-1], WholeString[Index])
                WholeString[Index]["x"] += TailStep[0]
                WholeString[Index]["y"] += TailStep[1]
            TailLocations.add(str(WholeString[_Length-1]["x"])+"|"+str(WholeString[_Length-1]["y"]))

    return TailLocations

def SimulateTail(_Lead, _Follow):
    TailLagx = _Lead["x"] - _Follow["x"]
    TailLagy = _Lead["y"] - _Follow["y"]

    if TailLagx in range(-1,2) and TailLagy in range(-1,2):
        return [0, 0]

    TailLagx = max(-1, min(TailLagx, 1))
    TailLagy = max(-1, min(TailLagy, 1))
    return[TailLagx, TailLagy]

#Left in only for fun, doesn't really scale to the whole Input
def TestDraw(_Headx, _Heady, _Tailx, _Taily, _HashList = []):
    Grid = [['.' for _ in range(6)] for _ in range(5)]

    for _Pair in _HashList:
        _Pair = _Pair.split('|')
        Grid[int(_Pair[1])][int(_Pair[0])] = '#'
    Grid[_Taily][_Tailx] = "T"
    Grid[_Heady][_Headx] = "H"

    Grid = list(reversed(Grid))
    for Index in range(len(Grid)):
        Grid[Index] = "".join(Grid[Index])
    Grid = "\n".join(Grid)
    print(Grid, "\n")

Steps = ParseFile("Day9\Input.txt")
print(f'Puzzle 1: Short String = {len(FindStringPath(Steps, 2))}')
print(f'Puzzle 2: Long String = {len(FindStringPath(Steps, 10))}')