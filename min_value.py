myList = [5,6,8,1,2,9]

minVal=myList[0]

for i in myList:
    if i < minVal:
        minVal = i

print("Lowest Value ",minVal)