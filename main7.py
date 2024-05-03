
print("Calculyator")
while True:

    try:
        print()
        select_operation = input("Введите операцию:( +,-,/ *):")



        a = int(input("Введите первое число"))
        b = int(input("Введите второе число"))

        if select_operation =="/" and b == 0:
            print("Второе число не может быть равно нулю (деление на ноль)")
            continue


    except:
        print("ошибка введите число")
        print("ощибка введите операцию")
    else:
        if select_operation == "+":
            print(a + b)
        elif select_operation == "-":
            print(a - b)
        elif select_operation == "*":
            print(a * b)
        elif select_operation == "/":
            print(a / b)


