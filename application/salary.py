def calculate_salary(casing, work_days, actually_worked_out):
    result = casing / work_days * actually_worked_out
    print(f'Сотрудник получит {round(result)} рублей')