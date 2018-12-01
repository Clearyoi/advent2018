
result = 0
list_of_results = []
number_found = False
while not number_found:
    with open("input.txt") as f:
        for line in f:
            result += int(line)
            if result in list_of_results:
                print result
                number_found = True
                break
            else:
                list_of_results.append(result)
