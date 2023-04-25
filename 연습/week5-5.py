user_input = input("문자열을 입력하세요: ")

if user_input.isalpha():
    print(len(user_input))
else:
    print("error")