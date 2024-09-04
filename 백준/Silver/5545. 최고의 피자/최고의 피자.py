import sys

input = sys.stdin.readline
n = int(input())
price_d, price_t = map(int, input().split())
cal_d = int(input())
cal_t = [int(input()) for _ in range(n)]
cal_t.sort(reverse=True)
topping = []
for i in range(n):
    cal = cal_d + sum(topping)
    price = price_d + len(topping) * price_t
    if (cal / price) < (cal + cal_t[i]) / (price + price_t):
        topping.append(cal_t[i])
print((cal_d + sum(topping)) // (price_d + len(topping) * price_t))
