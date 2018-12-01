
result = 0
with open("input.txt") as f:
    for line in f:
        result += int(line)

print result
