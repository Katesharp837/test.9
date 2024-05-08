
def main(input_str: str) -> str:
    result = str
    try:
        # Разбиваем входную строку на числа и оператор
        parts = input_str.split()
        a = int(parts[0])
        op = parts[1]
        b = int(parts[2])

        # Выполняем операцию в зависимости от оператора
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            # Проверка деления на ноль
            if b == 0:
                return "Ошибка: деление на ноль"
            result = a / b
        else:
            return "Ошибка: неподдерживаемая операция"

        # Возвращаем результат в виде строки
        return str(result)
    except Exception as e:
        return "Ошибка: " + str(e)

# Пример использования
if __name__ == "__main__":
    input_str = input("Введите выражение (например, '2 + 3'): ")
    print(main(input_str))








