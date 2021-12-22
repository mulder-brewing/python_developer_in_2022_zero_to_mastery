# Rule: don't use sets, this would be easier with sets
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dupes = []
length = len(some_list)
for i in range(0, length - 1):
    for j in range(i + 1, length):
        evaluating = some_list[i]
        if evaluating == some_list[j]:
            if evaluating not in dupes:
                dupes.append(evaluating)

print(dupes)
