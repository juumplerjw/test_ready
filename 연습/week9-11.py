import json
import csv

# JSON 파일 읽기
with open('task11_file.json', 'r') as json_file:
    json_data = json.load(json_file)

# CSV 파일 생성 및 데이터 저장
with open('task11_file.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    for key, value in json_data.items():
        writer.writerow([key + ', ' + value])
