def main(input_str: str) -> str:
    try:

        parts = input_str.split()


        if len(parts) != 3:
            raise ValueError("Неверный формат строки")



        a = int(parts[0])
        b = int(parts[2])
        if not (1 <= a <= 10) or not (1 <= b <= 10):
            raise ValueError("Числа должны быть от 1 до 10")

        c = parts[1]


        if c == '+':
            result = a + b
        elif c == '-':
            result = a - b
        elif c == '*':
            result = a * b
        elif c == '/':

            if b == 0:
                raise ValueError("Деление на ноль")
            result = a // b
        else:
            raise ValueError("Неподдерживаемая операция")


        return str(result)
    except Exception as e:
        return "Ошибка: " + str(e)



if __name__ == "__main__":
    while True:
        input_str = input("Hello calculyator Введите выражение +,-,*,/ (для выхода введите 'exit'): ")
        if input_str.lower() == "exit":
            print("Good bye my friend!")
            break
        print(main(input_str))






