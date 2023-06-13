def calculate(num1, num2, cal):
    if cal == "plus":
        return num1 + num2
    elif cal == "minus":
        return num1 - num2
    elif cal == "multi":
        return num1 * num2
    elif cal == "divi":
        if num2 != 0:
            return num1 / num2
        else:
            return 0
    else:
        return 0

num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))
cal = input("사칙연산을 입력하세요 (plus, minus, multi, divi): ")

result = calculate(num1, num2, cal)
print("결과:", result)
