import csv

def read_csv(file_path):
    data_list = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            data_list.append(row)
    return data_list

file_path = 'task9_file.csv'
data_list = read_csv(file_path)
print(data_list)
