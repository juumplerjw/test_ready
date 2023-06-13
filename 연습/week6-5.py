import math

x = 45

if x == 0:
    print("error")
else:
    radian = math.radians(x)
    sin_value = round(math.sin(radian), 3)
    cos_value = round(math.cos(radian), 3)
    tan_value = round(math.tan(radian), 3)

    print(sin_value, cos_value, tan_value)
