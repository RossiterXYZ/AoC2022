TotalScore1 = 0
RulesTable1 = {
    'A X': 1 + 3,
    'B X': 1 + 0,
    'C X': 1 + 6,
    'A Y': 2 + 6,
    'B Y': 2 + 3,
    'C Y': 2 + 0,
    'A Z': 3 + 0,
    'B Z': 3 + 6,
    'C Z': 3 + 3,
}
TotalScore2 = 0
RulesTable2 = {
    'A X': 3 + 0, #S
    'B X': 1 + 0, #R
    'C X': 2 + 0, #P
    'A Y': 1 + 3, #R
    'B Y': 2 + 3, #P
    'C Y': 3 + 3, #S
    'A Z': 2 + 6, #P
    'B Z': 3 + 6, #S
    'C Z': 1 + 6, #R
}

with open("Day2\Input.txt") as InputFile: # Use file to refer to the file object
    for InputLine in InputFile:
        InputLine = InputLine.strip()
        #Must easier to just put into a table actually.
        #InputLine.split(' ')
        TotalScore1 += RulesTable1[InputLine]
        TotalScore2 += RulesTable2[InputLine]
print(f'Puzzle 1: Assumed Rules = {TotalScore1}')
print(f'Puzzle 2: Actual Rules = {TotalScore2}')