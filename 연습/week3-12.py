tree = ''
for i in range(1, 10, 2):
    line = '*' * i
    tree += "{:^9}\n".format(line)

print(tree)