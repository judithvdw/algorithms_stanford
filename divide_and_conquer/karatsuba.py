def karatsuba(x, y):
    if x <= 9 or y <= 9:
        return x * y
    else:
        n = max(len(str(y)), len(str(x))) // 2
        a, b = x // (10 ** n), x % (10 ** n)
        c, d = y // (10 ** n), y % (10 ** n)
        step_1 = karatsuba(a, c)
        step_2 = karatsuba(b, d)
        step_3 = karatsuba(a + b, c + d)
        step_4 = step_3 - step_2 - step_1
        return (10 ** (2 * n) * step_1) + (10 ** n * step_4) + step_2


assert karatsuba(1234, 5678) == 1234 * 5678
