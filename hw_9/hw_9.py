import json
import csv

# Рівень Elementary
factory = {
    'It department': 50,
    'Sales dep': 30,
    'Production dep': 40,
    'Law dep': 20,
    'Construction dep': 25
}

factory['It department'] = 55
factory['Marketing dep'] = 15
del factory['Law dep']
total_employees = sum(factory.values())
print(f"Загальна кількість співробітників: {total_employees}")

# Рівень Intermediate

with open('factory_data.json', 'w') as json_file:
    json.dump(factory, json_file)

with open('factory_data.json', 'r') as json_file:
    factory = json.load(json_file)

total_employees = sum(factory.values())
print(f"Загальна кількість співробітників: {total_employees}")

# Рівень Advanced

with open('factory_data.json', 'w') as json_file:
    json.dump(factory, json_file)

with open('factory_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Department', 'Employees'])
    for department, employees in factory.items():
        writer.writerow([department, employees])

with open('factory_data.json', 'r') as json_file:
    factory = json.load(json_file)

with open('factory_data.csv', 'r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        department, employees = row
        factory[department] = int(employees)

total_employees = sum(factory.values())
print(f"Загальна кількість співробітників: {total_employees}")
