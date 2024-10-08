def fibonacci(num, first=0, second=1):
    if num > 1:
        return fibonacci(num-2, first+second, second+first+second)
    elif num == 1:
        return second
    elif num < 1:
        return first


print(fibonacci(1000))
