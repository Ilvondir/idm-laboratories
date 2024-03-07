rawData = open("SMSSpamCollection.csv", encoding="utf-8").read()

parsedData = rawData.replace('\t', '\n').split('\n')
labelList = parsedData[0::2]
textList = parsedData[1::2]

print(len(labelList))
print(len(textList))

print(labelList)

labelList = labelList[:-1]

print(len(labelList))
print(len(textList))

