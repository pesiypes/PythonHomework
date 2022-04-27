per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
m = float(input("Type the ammount of money "))
per_list = list(per_cent.values())
deposit = []
for i in per_list:
    deposit.append(i * m)
print(max(deposit))