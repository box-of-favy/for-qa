import time

def timer_with_control(print_time=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if print_time:
                print(f"Функция {func.__name__} выполнялась {end_time - start_time} секунд.")
            return result
        return wrapper
    return decorator

@timer_with_control()  # Управляем печатью времени выполнения
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 10  # Вы можете изменить это значение для тестирования с разными числами
result = factorial(n)
print(f"Факториал числа {n} равен {result}")