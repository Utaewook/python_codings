n, k = map(int,input().split())
coins = list()

for _ in range(n):
    coin = int(input())
    if coin > k:
        break
    coins.append(coin)

while coins:
    biggest_coin = coins.pop()

    temp_k = k
    while temp_k>0:
        pass