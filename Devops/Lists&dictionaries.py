pnList = [1,3,5,7,11,13,17,19]
'''pnList is a list which contains values (of any datatype) which can be accessed by index'''
print(pnList)
print(1 in pnList)
'''"in" tells us if the value exists in the list'''
pnList.append(23)
'''append will add a value to list'''
print(pnList)
pnList.pop()
'''pop will remove the last value from the list'''
print(pnList)
pnList.pop(7)
'''removing the value with index 7 from list'''
print(pnList)
pnList.reverse()
'''reverses the order of list'''
print(pnList)
print(len(pnList))
'''Prints length/size of "pnList" list'''

pnDic = {"One": "Cricket", "Two": "Chess", "Three": "Badminton"}
'''dictionaries will have key value pairs. The values can be accessed using the keys'''
print(pnDic)
print(pnDic["Two"])
'''prints the value of key "Two" '''
pnDic["Two"] = "Swimming"
'''Updates the value of key "Two" to "Swimming" '''
print(pnDic)
pnDic.update({"Four": "Chess"})
'''Adds a new key value to pnDic dictionary'''
print(pnDic)
pnDic.pop("Three")
'''Deletes key "Three" and it's value '''
print(pnDic)
print(pnDic.keys())
'''Prints all the keys of pnDic dictionary'''
print(len(pnDic))
'''Prints length/size of pnDic dictionary'''
