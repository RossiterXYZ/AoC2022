import math, copy

def ParseFile(_File):
    ReturnValue = []
    FileTmp = ""
    with open(_File) as InputFile:
        FileTmp = InputFile.read()
    return [ParseMonkeyData(Individual) for Individual in FileTmp.split("\n\n")]

def ParseMonkeyData(_Input):
    Monkey = {
        'Inventory': [],
        'Operation': [],
        'Test': 0,
        'Recipient': [False, True],
        'ThrowCount': 0,
    }
    RawLines = [x.strip() for x in _Input.strip().split("\n")]
    Monkey["Inventory"] = [int(x) for x in RawLines[1].split(": ")[1].split(", ")]
    Monkey["Operation"] = RawLines[2].split("old ")[1].split(" ")
    Monkey["Test"] = int(RawLines[3].split("by ")[1])
    Monkey["Recipient"][1] = int(RawLines[4].split("monkey ")[1])
    Monkey["Recipient"][0] = int(RawLines[5].split("monkey ")[1])
    return Monkey

def SimulateMonkeyingAround(_Count, _Stressed):
    for _ in range(_Count):
        for MonkeyIndex in range(len(Monkeys)):
            for InventoryIndex in range(len(Monkeys[MonkeyIndex]["Inventory"])):
                ThrowItem(MonkeyIndex, InventoryIndex, _Stressed)
            Monkeys[MonkeyIndex]["Inventory"] = []

def ThrowItem(_MonkeyIndex, _InventoryIndex, _Stressed = False):
    Item = Monkeys[_MonkeyIndex]["Inventory"][_InventoryIndex]

    if Monkeys[_MonkeyIndex]["Operation"][1] == "old":
        Change = Item
    else:
        Change = int(Monkeys[_MonkeyIndex]["Operation"][1])
    if Monkeys[_MonkeyIndex]["Operation"][0] == "*":
        Item *= Change
    else:
        Item += Change
    if not _Stressed:
        Item = math.floor(Item / 3)
    Item = Item % Modulo

    Truth = int(Item % Monkeys[_MonkeyIndex]["Test"] == 0) #Using the Truthy Value as an array index
    Monkeys[Monkeys[_MonkeyIndex]["Recipient"][Truth]]["Inventory"].append(Item)
    Monkeys[_MonkeyIndex]["ThrowCount"] += 1

def FancyPrint(_Attribute):
    for Index in range(len(Monkeys)):
        print(Index, Monkeys[Index][_Attribute])
    print("")

def MonkeyBusiness():
    Counts = []
    for Index in range(len(Monkeys)):
        Counts.append(Monkeys[Index]["ThrowCount"])
    Counts.sort(reverse=True)
    return Counts[0] * Counts[1]


Monkeys = ParseFile("Day11\Input.txt")

#I COULD rewrite the whole thing to be more generic but naw
Modulo = 1
for Monke in Monkeys:
    Modulo *= Monke["Test"]

TmpMonkeyCopy = copy.deepcopy(Monkeys)
SimulateMonkeyingAround(20, False)
Part1 = MonkeyBusiness()

Monkeys = copy.deepcopy(TmpMonkeyCopy)
FancyPrint("ThrowCount")
SimulateMonkeyingAround(10000, True)
FancyPrint("ThrowCount")
Part2 = MonkeyBusiness()

print(f'Puzzle 1: {Part1}')
print(f'Puzzle 2: {Part2}')