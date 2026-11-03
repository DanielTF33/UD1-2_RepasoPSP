def fibonacci(numero):
    a = 0
    b = 1

    for _ in range(numero):
        yield a
        c = a + b
        a = b
        b = c


for num in fibonacci(10):
    print(num, end=" ")