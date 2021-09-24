from sys import stdin, stdout

nums = {str(i) for i in range(100)}
numDict = {'0':'zero',
           '1':'one',
           '2':'two',
           '3':'three',
           '4':'four',
           '5':'five',
           '6':'six',
           '7':'seven',
           '8':'eight',
           '9':'nine',
           '10':'ten',
           '11':'eleven',
           '12':'twelve',
           '13':'thirteen',
           '14':'fourteen',
           '15':'fifteen',
           '16':'sixteen',
           '17':'seventeen',
           '18':'eighteen',
           '19':'nineteen',
           '20':'twenty',
           '30':'thirty',
           '40':'forty',
           '50':'fifty',
           '60':'sixty',
           '70':'seventy',
           '80':'eighty',
           '90':'ninety'}

def convert(numStr):
    if numStr in numDict:
        return numDict[numStr]
    return numDict[numStr[0] + '0'] + '-' + numDict[numStr[1]]

for line in stdin.readlines():
    line = line.split()
    for i in range(len(line)):
        if line[i] in nums:
            line[i] = convert(line[i])
    line[0] = line[0][0].upper() + line[0][1:]
    print(' '.join(line))