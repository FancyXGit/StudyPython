import time


def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
print(fibonacci(35))
end = time.time()
print("运行时间:", end - start, "秒")
