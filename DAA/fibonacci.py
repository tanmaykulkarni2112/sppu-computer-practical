def fibonacci(n):
    if n == 1 or n == 0:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(1))
print(fibonacci(3))
print(fibonacci(5))
