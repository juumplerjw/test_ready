def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("자연수 n을 입력하세요: "))

fibonacci_sequence = [str(fibonacci(i)) for i in range(n)]
factorial_value = factorial(n)

print("fibonacci", n, ":", ", ".join(fibonacci_sequence))
print("factorial", n, ":", factorial_value)
