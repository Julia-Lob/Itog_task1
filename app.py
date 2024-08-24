#task_1
import os    #работа с ОС
import sys   #работа с аргументами командной строки
from datetime import datetime

# 1. Получение пути
try:
   # path = r'/home/julia/PycharmProjects/Atteast_2'
    path = my_dir
except NameError:
    # Если переменная path не определена, используем корневую директорию
    path = "/"


# 2. Подсчёт количества файлов и нахождение топ-10 файлов по размеру
def get_files_info(path):
    files_info = []

    # Проходимся по всем файлам и папкам в заданном пути
    for root, dirs, files in os.walk(path):   #список директорий, список поддерикторий, файлы
        for file in files:
            full_path = os.path.join(root, file)   # полный путь к файлу
            try:
                size = os.path.getsize(full_path) / 1024  # размер в Кб (получает в байтах)
                files_info.append((file, size))
            except OSError:
                continue

    # Сортируем по размеру и выбираем топ-10
    top_10_files = sorted(files_info, key=lambda x: x[1], reverse=True)[:10]

    return len(files_info), top_10_files


# 3. Принимаем аргумент из командной строки для приветствия
def print_greeting():

    if len(sys.argv) > 1:
        name = sys.argv[1]
 #       name = echo $USER
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Привет, {name}! \nТекущая дата и время: {now}")
    else:
        print("Привет! Текущая дата и время не выведены, так как не было указано имя.")


if __name__ == "__main__":

    print_greeting()

    file_count, top_10_files = get_files_info(path)

    print(f"Количество файлов в директории '{path}': {file_count}")

    print("Топ-10 файлов по размеру (в Кб):")
    for i, (file, size) in enumerate(top_10_files, start=1):
        print(f"{i}. {file} - {size:.2f} Кб")