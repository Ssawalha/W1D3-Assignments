
# use a generator expression where you would use a list comprehension but
# do not need to store the list beyond its immediate usage

max([2*i for i in range(100)])

# this uses extra memory to create the list object

max(2*i for i in range(100))

# transforms the values in range one by one to create a sequence for max

# if you aren't saving your list comprehension in a variable, there's a good chance
# it could be a generator expression instead