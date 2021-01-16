# Программа по расчету компании
revenue = int(input("Введите выручку компании: ")) # Запрос выручки
costs = int(input("Введите издержки компании: ")) # Запрос издержок
staff = int(input("Введите количество сотрудников: ")) # Запрос сотрудников

profit = revenue - costs # прибыль
profitability = profit / revenue * 100 # рентабельность
staff = revenue / staff # прибыль на 1 сотрудника

if revenue > costs:
    print(f"Компания работает в прибыль, она составляет = {profit} \nПрибыль фирмы в расчете на 1 сотрудника = {round(staff, 2)}")
else:
    print(f"Компания работает в убыток, он составляет = {profit}")

if profit > 0:
    print(f"Рентабельность выручки составляет = {round(profitability, 2)} %")
