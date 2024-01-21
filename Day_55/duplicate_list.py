lis = [5,6,7,5,7,0,7,5,]
uniqueList = []
duplicatelist = []
 
for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(duplicateList)
