def fibonacci_sequence(n):
    if not isinstance(n, int) or n <= 0 or n >= 20:
        print('error')
        return
    fib_seq = [0, 1]
    for i in range(2, n+1):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq