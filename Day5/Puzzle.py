CrateString = ''
ParseSteps = False
StepData = []
with open("Day5\Input.txt") as InputFile:
    for InputLine in InputFile:
        if not ParseSteps:
            if InputLine == "\n":
                ParseSteps = True
                Tmp = list(reversed(CrateString.strip().split('\n')))
                ParseTmp = [Tmp[0][i] for i in range(1, len(Tmp[0]), 4)]
                print(ParseTmp)
            else:
                CrateString += InputLine
        else:
            _, Count, _, From, _, To = InputLine.split(' ')
            StepData.append([int(Value) for Value in [Count, From, To]])



#print(f'Puzzle 1: Subset = {1}')
#print(f'Puzzle 2: Overlap = {1}')