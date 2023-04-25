from random import randint

A = tuple(randint(1, 10) for _ in range(10))
result = A[0] >= A[1]
print(result)