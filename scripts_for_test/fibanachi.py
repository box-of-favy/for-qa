def fib(total: int):
    prev = 0
    curr = 1
    index = 0
    while index < total:
        index += 1
        value = curr
        curr += prev
        prev = value
        yield value


for i, n in enumerate(fib(10)):
    print('index, value: ', i, n)
