
# Cоздания двух исключений:
class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

# Функция, которая будет генерировать исключения:
def check_value(value):
    if value < 10:
        raise ValueTooSmallError("Значение слишком мало!")
    if value > 20:
        raise ValueTooLargeError("Значение слишком большое!")
    return value

# Добавим обработку исключений в функции, вызывающие check_value:
try:
    print(check_value(8))
except ValueTooSmallError as e:
    print(f"Ошибка: {e}-")
except ValueTooLargeError as e:
    print(f"Внимание: {e}-")
except Exception as e:
    print(f"Неожиданная ошибка: {e}-")

# Вызовем функцию check_value с разными значениями и обработаем исключения:
try:
    print(check_value(21))
except ValueTooSmallError as e:
    print(f"Ошибка: {e}-")
except ValueTooLargeError as e:
    print(f"Внимание: {e}-")
except Exception as e:
    print(f"Неожиданная ошибка: {e}-")

