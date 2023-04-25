num = int(input("정수를 입력하세요: "))

if num < 15:
    print("error")
else:
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)