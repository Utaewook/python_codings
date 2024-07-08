
def calculate(a, b, op):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    else:
        return abs(a)//b * (abs(a)//a)

def dfs(curr_val, i, rest_op):
    global nums, val_min, val_max

    if i == len(nums) - 1:
        curr_val = calculate(curr_val, nums[i], rest_op)
        val_max = max(val_max, curr_val)
        val_min = min(val_min, curr_val)

        return






if __name__ == "__main__":
    n = int(input())
    nums = list(map(int,input().split()))
    ops = list(map(int, input().split()))

    val_max, val_min = -1 * float('inf'), float('inf')