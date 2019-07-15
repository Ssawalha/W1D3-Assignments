from functools import reduce

values = [1,2,3,4,5, 6, 2, 3,6,7]

def addthem(currentsum, nextelement):
    return currentsum + nextelement

complicatedsum = reduce(addthem, values, 0)

def buildset(currentset, nextelement):
    currentset.add(nextelement)
    return currentset

setfromlist = reduce(buildset, values, set())

print(complicatedsum)
print(setfromlist)