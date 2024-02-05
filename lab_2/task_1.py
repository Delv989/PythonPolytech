money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count_month = 0
delta = spend-salary

while money_capital >= delta:
    money_capital -= delta
    spend += increase*spend
    count_month += 1
    delta = spend-salary
print("Количество месяцев, которое можно протянуть без долгов:", count_month)
