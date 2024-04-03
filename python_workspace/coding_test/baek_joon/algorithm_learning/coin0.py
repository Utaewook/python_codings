n, k = map(int,input().split())
coins = list()

for _ in range(n):
    coin = int(input())
    if coin > k:
        break
    coins.append(coin)

count = k
while coins:
    biggest_coin = coins.pop()

    rest_coins = coins[:]
    temp_count, temp_k = k // biggest_coin, k % biggest_coin

    while temp_k > 0:
        coin = rest_coins.pop()
        coin_count, temp_k = temp_k // coin, temp_k % coin

        temp_count += coin_count

    count = min(count, temp_count)

print(count)