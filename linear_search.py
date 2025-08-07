def linearSearch(myList,val):
    for i in range(len(myList)):
        if myList[i] == val:
            return f"Index no : {i}"
    return -1
myList=[2,3,5,7,1,8]
val=1
print(linearSearch(myList,val))