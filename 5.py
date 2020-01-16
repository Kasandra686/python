revenues = int(input("Введите сумму выручки фирмы: "))
expenses = int(input("Введите сумму затрат: "))
if revenues > expenses:
    profit = revenues - expenses
    print(f"Фирма принесла прибыль в сумме:{profit}")
    staff = int(input("Введите количество сотрудников для расчета прибыли на каждого: "))
    profit_st = profit / staff
    print(f" Прибыль на каждого сотрудника составляет : {profit_st:.2f}")
else:
    lesion = expenses - revenues
    print(f"Фирма понесла убыток в сумме:{lesion}")
