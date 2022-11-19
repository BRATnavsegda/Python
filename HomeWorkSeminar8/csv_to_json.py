import csv
import json


# Функция для конвертирования csv в json

def make_json(csv_file='numbers.csv', json_file='numbers.json'):

    data = {}

    with open(csv_file, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        for rows in csv_reader:

            key = rows['0']
            data[key] = rows

    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))




