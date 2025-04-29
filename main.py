def discriminant(a, b, c):
    """
    Вычисляет дискриминант квадратного уравнения ax² + bx + c = 0
    Возвращает: float
    """
    return b**2 - 4*a*c

def power(base, exponent):
    """
    Возведение числа в произвольную степень
    Возвращает: float
    """
    return base ** exponent

def root(number, n=2):
    """
    Вычисление корня n-ной степени (по умолчанию квадратный)
    Возвращает: float или строку с ошибкой
    """
    try:
        if number < 0 and n % 2 == 0:
            raise ValueError("Четный корень из отрицательного числа")
        return number ** (1/n)
    except ValueError as e:
        return f"Ошибка: {e}"
    except ZeroDivisionError:
        return "Ошибка: нулевая степень корня"
