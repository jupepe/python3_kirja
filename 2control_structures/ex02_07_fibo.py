# Fibonaccin lukusarja

def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


result_list = fib(90)
print(result_list)
