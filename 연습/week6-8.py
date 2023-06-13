import task8_module

total_price = 0

while True:
    fruit = input("과일명을 입력하세요 (0 입력 시 종료): ")
    if fruit == "0":
        break
    price = task8_module.fruiterie(fruit)
    if price == "없는 메뉴입니다.":
        print(price)
    else:
        total_price += price

print(total_price)
