with open("fintest.txt", "r") as file:
    contents = file.read()
    user_input = input("문자를 입력하세요: ")

if user_input in contents:
    print(True) 
else:
    print(False)       