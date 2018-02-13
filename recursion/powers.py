def power(x, n):
    def is_even(n):
        return n % 2 == 0

    if n == 0:
        return 1

    elif n < 0:
        return 1 / power(x, -n)

    elif is_even(n):
        even_power = power(x, n/2)
        return even_power * even_power

    else:
        return power(x, n-1) * x

print(power(4, 2))
print(power(5, -2))
print(power(2, 10))