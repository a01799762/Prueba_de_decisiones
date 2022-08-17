moneda_1 = int(input("Dame una moneda: "))
moneda_2 = int(input("Dame otra moneda: "))

if moneda_1 > moneda_2:
    moneda_mayor1 = moneda_1
    print(f' La moneda uno es mayor')
else:
    moneda_mayor1 = moneda_2
    print(f' La moneda dos es mayor')

moneda_3 = int(input("Dame una ultima moneda: "))
if moneda_mayor1 > moneda_3:
    print(f'La moneda {moneda_mayor1} es mayor')
else:
    print(f'La moneda tres es mayor')