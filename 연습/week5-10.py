def multipl(num):
    with open('multiplication_table.txt', 'w') as f:
        for i in range(1, 10):
            result = num * i
            f.write(f"{num} x {i} = {result}\n")
    return None