
def ParseFile(_File, _Function):
    ReturnValue = {}
    with open(_File) as InputFile:
        for InputLine in InputFile:
            ReturnValue = _Function(InputLine, ReturnValue)

def CreateDirectoryStructure(_Input, _Data):
    return True

DirectoryStructure = ParseFile("Day7\Input.txt", )

print(f'Puzzle 1: Find Sue =      {1}')
print(f'Puzzle 2: Find REAL Sue = {1}')