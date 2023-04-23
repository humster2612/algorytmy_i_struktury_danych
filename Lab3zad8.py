def f(n):
    if n == 1:
        return 4
    else:
        return 1 / (1 - f(n-1))
for n in range(1, 101):
    print(f"f({n}) = {f(n)}")
