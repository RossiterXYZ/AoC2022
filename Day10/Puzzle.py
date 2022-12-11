def ParseFile(_File):
    ReturnValue = []
    with open(_File) as InputFile:
        for InputLine in InputFile:
            ReturnValue.append(InputLine.strip())
    return ReturnValue

def ProcessInstructions(_Input):
    X = 1
    Output = [X]

    for Instruction in _Input:
        Output.append(X)
        if Instruction[:4] == "addx":
            Value = int(Instruction.split(" ")[1])
            Output.append(X + Value)
            X += Value
    return Output

def GetSignalStrengths(_CPUList, _Required):
    TotalSignal = 0
    for Value in _Required:
        TotalSignal += _CPUList[Value-1] * Value
    return TotalSignal

def GetPicture(_CPUList, _Fancy = True):
    OutputData = []
    Lit = "🟨"
    Dim = "⬛"
    if not _Fancy:
        Lit = "#"
        Dim = "."
    for Index in range(240):
        HorizontalPosition = Index % 40
        if HorizontalPosition == 0:
            OutputData.append("\n")

        if _CPUList[Index] in range(HorizontalPosition-1, HorizontalPosition+2):
            OutputData.append(Lit)
        else:
            OutputData.append(Dim)
    return "".join(OutputData)


Instructions = ParseFile("Day10\Input.txt")
CPUOutput = ProcessInstructions(Instructions)

print(f'Puzzle 1: {GetSignalStrengths(CPUOutput, [20, 60, 100, 140, 180, 220])}')
print(f'Puzzle 2: {GetPicture(CPUOutput)}')