pi = 3.141592

def carea(radius):
    # 원의 넓이 계산
    area = pi * radius * radius
    return area

def circum(radius):
    # 원의 둘레 계산
    circumference = 2 * pi * radius
    return circumference

radius = float(input("원의 반지름을 입력하세요: "))

area = carea(radius)
circumference = circum(radius)

print("Area:", format(area, ".3f"))
print("Circumference:", format(circumference, ".3f"))
