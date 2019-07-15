# map

def adder(x):
    return x + 5

mapping = map(adder, [1,2,3,4,5])
print(mapping)
print(list(mapping))

print([adder(x) for x in [1,2,3,4,5]])

# filter

def iseven(x):
    if x % 2 == 0:
        return True
    return False

filtered = filter(iseven, range(20))

otherway = [i for i in range(20) if i % 2 == 0]

print(filtered)
print(list(filtered))

