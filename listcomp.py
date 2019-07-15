
result = []
for i in range(1,100,3):
    result.append("The number {}".format(i))

# the same as:

result = ["The number {}".format(i) for i in range(1,100,3)]

# expression for variable in sequence

result = []
for i in range(1,100,3):
    if i % 2 == 0:
        result.append("The number {}".format(i))

# is the same as:

result = ["The number {}".format(i) for i in range(1,100,3) if i % 2 == 0]

# expression for variable in sequence if condition

print(result)