from itertools import combinations

T = int(input())

def swapped_values(value):
    values = set()
    for idx1,idx2 in index_combinations:
        new_value = list(value)
        new_value[idx1],new_value[idx2] = new_value[idx2],new_value[idx1]
        values.add(''.join(c for c in new_value))

    return values


for test_case in range(1, T + 1):
    result = 0
    val, swap_count = input().split()
    val, swap_count = str(val), int(swap_count)
    dict = {0: {val}}
    index_combinations = list(combinations(range(len(val)), 2))

    for i in range(1, swap_count+1):
        next_values = set()
        for v in dict[i-1]:
            next_values.update(swapped_values(v))
        dict[i] = next_values

    result = int(max(dict[swap_count]))
    print("#%d %d" % (test_case, result))

