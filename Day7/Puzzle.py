def ParseFile(_File, _Function, _PassedValue):
    ReturnValue = {'CurrentDirectory': []}
    with open(_File) as InputFile:
        for InputLine in InputFile:
            ReturnValue = _Function(InputLine, ReturnValue, _PassedValue)
    return ReturnValue

def CreateDirectoryStructure(_Line, _Data, _AdditiveStructure):
    if _Line[:4] == "$ ls":
        return _Data
    
    if _Line[:4] == "$ cd":
        Dir = _Line[5:-1]
        if  Dir == '..':
            _Data["CurrentDirectory"].pop()
        else:
            _Data["CurrentDirectory"].append(Dir)
        return _Data

    _Line = _Line.strip().split(' ')
    if _AdditiveStructure:
        for Depth in range(len(_Data["CurrentDirectory"])):
            Dir = "/".join(_Data["CurrentDirectory"][:Depth+1])
            if _Data.get(Dir) is None:
                _Data[Dir] = 0
            if _Line[0] != "dir":
                _Data[Dir] += int(_Line[0])
    else:
        Dir = "/".join(_Data["CurrentDirectory"])
        if _Data.get(Dir) is None:
            _Data[Dir] = 0
        if _Line[0] != "dir":
            _Data[Dir] += int(_Line[0])

    return _Data

def FindAppropriateDirectories(_Directories):
    _Directories.pop('CurrentDirectory')
    Sum = 0
    for Value in _Directories.values():
        if Value <= 100_000:
            Sum += Value
    return Sum

def FindLargeDirectory(_Directories, _Distinct):
    _Directories.pop('CurrentDirectory')
    _Distinct.pop('CurrentDirectory')
    RemainingSpace = 0

    for Value in _Distinct.values():
        RemainingSpace += Value
    RemainingSpace = 70_000_000 - RemainingSpace
    Requirement = 30_000_000 - RemainingSpace

    BestFit = 30_000_000
    for Value in _Directories.values():
        if Value >= Requirement and Value < BestFit:
            BestFit = Value
    return BestFit

DirectoryStructure = ParseFile("Day7\Input.txt", CreateDirectoryStructure, True)
DistinctDirectories = ParseFile("Day7\Input.txt", CreateDirectoryStructure, False)
print(f'Puzzle 1: Find Suitable Directories = {FindAppropriateDirectories(DirectoryStructure.copy())}')
print(f'Puzzle 2: Find Large Enough Directory = {FindLargeDirectory(DirectoryStructure.copy(), DistinctDirectories.copy())}')