from copy import deepcopy
CrateString = ''
CrateData = {}
Crate9001 = {}
ParseSteps = False
with open("Day5\Input.txt") as InputFile:
    for InputLine in InputFile:
        if not ParseSteps:
            if InputLine == "\n":
                ParseSteps = True
                RawCrateData = list(reversed(CrateString.rstrip().split('\n')))
                RawCrateData = [[RawCrateData[x][i] for i in range(1, len(RawCrateData[0]), 4)] for x in range(len(RawCrateData))]
                CrateData = {Pile: [] for Pile in RawCrateData.pop(0)}
                for Row in RawCrateData:
                    for Stack in range(len(CrateData)):
                        if Row[Stack] != ' ':
                            CrateData[str(Stack+1)].append(Row[Stack])
                Crate9001 = deepcopy(CrateData)
            else:
                CrateString += InputLine
        else:
            _, Count, _, From, _, To = InputLine.strip().split(' ')
            Index = len(Crate9001[From]) - int(Count)
            for _ in range(int(Count)):
                CrateData[To].append(CrateData[From].pop(len(CrateData[From])-1))
                Crate9001[To].append(Crate9001[From].pop(Index))

print(f'Puzzle 1: CrateMover9000 = {"".join([x.pop() for x in CrateData.values()])}')
print(f'Puzzle 2: CrateMover9001 = {"".join([x.pop() for x in Crate9001.values()])}')