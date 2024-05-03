def total_salary(path):
    total = 0
    count = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                _, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total += salary
                count += 1
            except ValueError:
                print(f"Ошибка: неверный формат строки '{line.strip()}'")
    if count == 0:
        return 0, 0 
    average = total / count
    return total, average

data = [
    "Ivan Bocman,2500",
    "Liudmila Shmel',1900",
    "Mishel' Corp,1600"
]

with open("salary_file.txt", "w", encoding="utf-8") as file:
    for line in data:
        file.write(line + "\n")

total, average = total_salary("salary_file.txt")
print(f"Общая сумма заработной платы: {total}, Средняя заработная плата: {average}")
