TotalScore1 = 0
RulesTable1 = {
    'A X': 1 + 3, #D
    'B X': 1 + 0, #L
    'C X': 1 + 6, #W
    'A Y': 2 + 6, #W
    'B Y': 2 + 3, #D
    'C Y': 2 + 0, #L
    'A Z': 3 + 0, #L
    'B Z': 3 + 6, #W
    'C Z': 3 + 3, #D
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

with open("Day2\Input.txt") as InputFile:
    for InputLine in InputFile:
        InputLine = InputLine.strip()

        TotalScore1 += RulesTable1[InputLine]
        TotalScore2 += RulesTable2[InputLine]

print(f'Puzzle 1: Assumed Rules = {TotalScore1}')
print(f'Puzzle 2: Actual Rules = {TotalScore2}')