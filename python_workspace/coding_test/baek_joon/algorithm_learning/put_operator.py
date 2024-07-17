
def calculate(a, b, op):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    else:
        return abs(a)//b * (abs(a)//a) if a and b else 0

def dfs(curr_val, i, rest_op):
    global nums, val_min, val_max

    if i == len(nums) - 1:
        curr_op = None
        for op, count in enumerate(rest_op):
            if count:
                curr_op = op
                break
        curr_val = calculate(curr_val, nums[i], curr_op)
        val_max = max(val_max, curr_val)
        val_min = min(val_min, curr_val)

        return

    for op, count in enumerate(rest_op):
        if count:
            temp_val = calculate(curr_val, nums[i], op)
            rest_op[op] -= 1
            dfs(temp_val, i+1, rest_op)
            rest_op[op] += 1


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int,input().split()))
    ops = list(map(int, input().split()))
    first_val, nums = nums[0], nums[1:]

    val_max, val_min = float('-inf'), float('inf')
    dfs(first_val,0, ops)
    print(val_max)
    print(val_min)