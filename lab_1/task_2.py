from_mb_to_b = 1024 * 1024
capacity_disk_in_mb = 1.44
page = 100
row = 50
symbol = 25
cost_symbol = 4

count_book = int(capacity_disk_in_mb*from_mb_to_b/(page*row*symbol*cost_symbol))

print("Количество книг, помещающихся на дискету:", count_book)
