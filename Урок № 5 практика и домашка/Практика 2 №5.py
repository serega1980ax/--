def num(n):
    d = 2
    while d *d <= n and n % d != 0:
        d += 1
    return d * d > n
d = [1, 2, 3, 4, 6, 8, 10]
n = int(input())
b = list(map(num, d))
print(b)