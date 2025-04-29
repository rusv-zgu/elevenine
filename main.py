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
    print("Доступные операции: +, -, *, /")
    
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ")
        
        if operation == '+':
            print(f"Результат: {addition(a, b)}")
        elif operation == '-':
            print(f"Результат: {subtraction(a, b)}")
        elif operation == '*':
            print(f"Результат: {multiplication(a, b)}")
        elif operation == '/':
            print(f"Результат: {division(a, b)}")
        else:
            print("Ошибка: неизвестная операция")

    except:
        print("Ошибка: введите целое положительное число")

if __name__ == "__main__":
    main()
