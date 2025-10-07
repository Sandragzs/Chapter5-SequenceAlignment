#37
from math import gcd, inf
from functools import reduce

def min_coins_change(money, coins):
    # Filtrar monedas válidas
    coins = sorted(set(c for c in coins if 0 < c <= money))
    if not coins:
        return -1

    # Reducir por MCD
    g = reduce(gcd, coins)
    if money % g != 0:
        return -1
    if g > 1:
        money //= g
        coins = [c // g for c in coins]

    # Inicialización DP
    dp = [0] + [inf] * money

    # DP unbounded knap
    for c in coins:
        for x in range(c, money + 1):
            dp[x] = min(dp[x], dp[x - c] + 1)

    return dp[money] if dp[money] != inf else -1

money = 40
coins = [1, 5, 10, 20, 25, 50]

print(min_coins_change(money, coins))