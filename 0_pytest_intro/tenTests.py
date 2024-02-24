import subprocess

l = []
print("Type: ", type(l))
l.append(1)
l.append('1 ')
l.extend([2,3,4])
print("l -> ", l)


# Создание тестовых файлов
def test_one():
    print(" >>>I'm test one!")


# так можно, но не нужно, и с модулем не заработает
def testtwo():
    pass
# Создание тестовых классов
class TestClass:

    def test_one(self):
        pass

    def testtwo(self):
        pass
# запуск отдельных файлов, функций, классов
# Запустить pytest для всего каталога
subprocess.run(["pytest", "scripts_for_test/"])

# Запустить pytest для конкретного файла
subprocess.run(["pytest", "scripts_for_test/tenTests.py"])

# 1) Создаем файлы и функции с префиксом test
# 2) Создаем классы с префиксом Test
# 3) Флаг -v / -q управления подробностью вывода
# 4) Флаг -s позволяет отображать print’ы
# 5) Отдельный файл, метод, класс передаем его команде pytest
# 6) -x / --maxfail=n Остановить тесты после 1-го или n-го падения
# 7) --collect-only Собрать информацию о тестах
# 8) --lf запустить только последние упавшие
# 9) Посмотреть все другие параметры -h

# pytest .\0_pytest_intro\ -v
