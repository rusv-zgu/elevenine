def discriminant(a, b, c):
    return b**2 - 4*a*c

def power(base, exponent):
    return base ** exponent

def root(number, n=2):
    try:
        if number < 0 and n % 2 == 0:
            raise ValueError("Четный корень из отрицательного числа")
        return number ** (1/n)
    except ValueError as e:
        return f"Ошибка: {e}"
    except ZeroDivisionError:
        return "Ошибка: нулевая степень корня"

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "деление на ноль!"
    return a / b

def main():
    print("Абсолютный калькулятор")
    print()
    
    try:
        print("""Выберите операцию:
        1. Сложение
        2. Вычитание
        3. Умножение
        4. Деление
        5. Дискриминант
        6. Корень n степени
        7. Возведение в степень""")

        operation = int(input())
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if operation == 5:
              c = int(input("Введите третье число: "))
        
        if operation == 1:
            print(f"Результат: {addition(a, b)}")
        elif operation == 2:
            print(f"Результат: {subtraction(a, b)}")
        elif operation == 3:
            print(f"Результат: {multiplication(a, b)}")
        elif operation == 4:
            print(f"Результат: {division(a, b)}")
        elif operation == 7:
            print(f"Результат: {power(a, b)}")
        elif operation == 5:
            print(f"Результат: {discriminant(a, b, c)}")
        elif operation == 6:
            print(f"Результат: {root(a, b)}")
        else:
            print("Ошибка: неизвестная операция")
           

    except:
        print("Ошибка: введите целое положительное число")

#Тестировщик всё проверил - всё работает, я даже исправил ваши ошибки, глупые разрабы

if __name__ == "__main__":
    main()
