amount = int(input("금액을 입력하세요: "))

coin500 = amount // 500
amount = amount % 500

coin100 = amount // 100
amount = amount % 100

coin50 = amount // 50
amount = amount % 50

coin10 = amount // 10
amount = amount % 10

coin1 = amount // 1

print("500:", coin500, "개")
print("100:", coin100, "개")
print("50:", coin50, "개")
print("10:", coin10, "개")
print("1:", coin1, "개")
