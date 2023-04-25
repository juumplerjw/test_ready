max_num = None

for i in range(5):
    num = int(input("숫자를 입력하세요: "))
    if max_num is None or num > max_num:
        max_num = num

print(max_num)