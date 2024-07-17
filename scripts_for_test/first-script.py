print('Hello World!')

x = "глобальная"

def func():
    y = "локальная"  # Локальная переменная
    print(y)
    print(x)

func()  # Не забудьте вызвать эту функцию, чтобы увидеть результат

def outer_func(length, width):
    message = "Hi, вычисляем площадь и периметр"  # Локальная переменная внешней функции

    def calculate_area_and_perimeter(length, width):
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter

    print(message)  # Выведем сообщение внутри outer_func
    return calculate_area_and_perimeter(length, width)  # Вызываем внутреннюю функцию и возвращаем ее результат

area, perimeter = outer_func(10, 5)  # Теперь здесь будет корректно возвращен результат функции calculate_area_and_perimeter
print(f"Площадь: {area}, Периметр: {perimeter}")
