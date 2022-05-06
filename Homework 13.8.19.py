quant = int(input('Enter the required quantity of tickets '))
summ = 0
age = []
for i in range(0, quant):
    age.append(int(input(f"Enter the age of visitor number {i+1} ")))
    if age[i] >= 25:
        summ += 1390
        print('Charge is 1390 rubles')
    elif 18 <= age[i] < 25:
        summ += 990
        print('Charge is 990 rubles')
    elif 0 < age[i] <= 18:
        print("No charge")
    else:
        print('Incorrect age. Try once over.')
        age[i] = False
        break

if quant > 3 and not age.count(False):
    print(f"Total charge with 10% discount is {summ * 0.9}")
elif quant <= 3 and not age.count(False):
    print(f"Total charge is {summ}")
