import copy, math

def ParseLines(_String):
    StartString, EndString = _String.split(' to ')

    _, Name, _, _, Rate, _, _ = StartString.split(' ')
    Rate = int(Rate[5:7]) if len(Rate) == 8 else int(Rate[5:6])

    EndString = EndString.split(' ')
    EndString.pop(0)
    EndString = [Element[:2] for Element in EndString]

    return {Name: {"Rate": Rate, "Tunnels": EndString}}

def ParseFile(_File):
    with open(_File) as InputFile:
        return [ParseLines(Line) for Line in InputFile.read().strip().split("\n")]

def BestPath(_Graph):
    Path = ['AA']
    CurrentTunnel = 'AA'


ValveData = ParseFile("Day16\InputTest.txt")
[i for i in ValveData if print(i) or True]

#print(f'Puzzle 1: {Part1}')
#print(f'Puzzle 2: {Part2}')