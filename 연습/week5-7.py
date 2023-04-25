sum = 0
while True:
    num = input()
    if num == "stop":
        break
    if num.isdigit():
        sum += int(num)
print(sum)