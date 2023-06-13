import json

# JSON 파일 읽기
with open('task10_file.json', 'r') as file:
    json_data = file.read()

# JSON 데이터를 dictionary로 변환
data = json.loads(json_data)

# 출력
print(data)
