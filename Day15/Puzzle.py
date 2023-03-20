import copy, math

def ParseLines(_String):
    _, _, x1, y1, _, _, _, _, x2, y2 = _String.split(' ')
    x1 = int(x1[2:-1])
    x2 = int(x2[2:-1])
    y1 = int(y1[2:-1])
    y2 = int(y2[2:])
    return {"Sensor": {'x': x1, 'y': y1}, "Beacon": {'x': x2, 'y': y2}}

def ParseFile(_File):
    with open(_File) as InputFile:
        return [ParseLines(Line) for Line in InputFile.read().strip().split("\n")]

def FindCoverageInY(_DataSet, _y = 2_000_000):
    ConvertDataSet = []
    for Record in _DataSet:
        Distance = abs(Record["Sensor"]["x"] - Record["Beacon"]["x"]) + abs(Record["Sensor"]["y"] - Record["Beacon"]["y"])
        Offset = abs(_y - Record["Sensor"]["y"])
        Width = Distance - Offset
        if Width >= 0:
            ConvertDataSet.append({'Start': Record["Sensor"]['x'] - Width, 'End': Record["Sensor"]['x'] + Width})
    ConvertDataSet = sorted(ConvertDataSet, key=lambda x: x['Start'])

    Count = 0
    Start = End = ConvertDataSet[0]["Start"]
    for Record in ConvertDataSet:
        if End < Record["Start"]:
            Count += End - Start
            Start = End = Record["Start"]
        End = max(Record["End"], End)
    Count += End - Start
    return Count

def To1D(_x, _y, _w = 4_000_000):
    return _x * _w + _y
def To2D(_index, _w = 4_000_000):
    return divmod(_index, _w)

def CheckBounds(_x, _y, _w = 4_000_000):
    if _x in range(_w+1) and _y in range(_w+1):
        return To1D(_x, _y, _w)
    return -1

def InRange(_Element, _Sensors, _w = 4_000_000):
    x, y = To2D(_Element, _w)
    Results = [True for Sensor in _Sensors if (abs(Sensor['x'] - x) + abs(Sensor['y'] - y)) <= (Sensor['Distance'])]
    return len(Results) > 0

def FindTuningFrequency(_DataSet, _w = 4_000_000):
    ConvertDataSet = {'Sensors': [], 'Possibilities': {}}
    Index = 1
    for Record in _DataSet:
        Distance = abs(Record["Sensor"]["x"] - Record["Beacon"]["x"]) + abs(Record["Sensor"]["y"] - Record["Beacon"]["y"]) + 1
        ConvertDataSet["Sensors"].append({'x': Record["Sensor"]["x"], 'y': Record["Sensor"]["y"], 'Distance': Distance - 1})
        for Iterator in range(Distance + 1):
            a = CheckBounds(Record["Sensor"]["x"] + Distance - Iterator, Record["Sensor"]["y"] + Iterator, _w)
            b = CheckBounds(Record["Sensor"]["x"] - Distance + Iterator, Record["Sensor"]["y"] - Iterator, _w)
            c = CheckBounds(Record["Sensor"]["x"] + Iterator, Record["Sensor"]["y"] - Distance + Iterator, _w)
            d = CheckBounds(Record["Sensor"]["x"] - Iterator, Record["Sensor"]["y"] + Distance - Iterator, _w)
            for Item in [a, b, c, d]:
                if ConvertDataSet["Possibilities"].get(Item, -1) == -1:
                    ConvertDataSet["Possibilities"].update({Item: 1})
                else:
                    ConvertDataSet["Possibilities"][Item] += 1
        print(f'Processed Sensor {Index}/{len(_DataSet)}')
        Index += 1
    print(f'Pre-Length: {len(ConvertDataSet["Possibilities"])}')
    ConvertDataSet["Possibilities"] = [Item[0] for Item in ConvertDataSet["Possibilities"].items() if Item[1] > 1]
    print(f'Post-Length: {len(ConvertDataSet["Possibilities"])}')

    Solution = [TestElement for TestElement in ConvertDataSet["Possibilities"] if not InRange(TestElement, ConvertDataSet["Sensors"], _w)]
    return Solution


SensorData = ParseFile("Day15\Input.txt")
Part1 = FindCoverageInY(SensorData)
print(f'Puzzle 1: {Part1}')

Part2 = FindTuningFrequency(SensorData)
print(f'Puzzle 2: {Part2}')