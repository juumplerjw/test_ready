def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "잘못된 연산자입니다."

input_str = input("숫자와 연산자를 입력하세요: ")
num1, operator, num2 = input_str.split()
result = calculate(float(num1), operator, float(num2))
print(result)