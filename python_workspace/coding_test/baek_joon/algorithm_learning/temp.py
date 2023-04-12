test_cases = int(input())

for test_case in range(test_cases):
    days = int(input())
    cost = list(map(int, input().split()))
    cost.reverse()
    stock_stack = []
    profit = 0
    while cost:
        c = cost.pop()
        if (not stock_stack) or stock_stack[-1] <= c:
            stock_stack.append(c)
        elif stock_stack[-1] > c:
            profit += stock_stack[-1] * (len(stock_stack) - 1) - sum(stock_stack[:-1])
            stock_stack = [c]
    if stock_stack:
        profit += stock_stack[-1] * (len(stock_stack) - 1) - sum(stock_stack[:-1])


    print(f"#{test_case + 1} {profit}")