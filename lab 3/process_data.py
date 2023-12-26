import json
import sys


def field(items, *args):

    assert len(args) > 0
    if len(args) == 1:
        return [i[args[0]] for i in items if args[0] in i.keys() and i[args[0]] != None]
    return [{j: i[j] for j in args if j in i.keys() and i[j] != None} for i in items]


import random


def gen_random(num_count, begin, end):
    result = [random.randint(begin, end) for i in range(num_count)]
    return result

class Unique(object):
    def __init__(self, items, ignore_case=False):
        self.index = -1  # Текущий индекс
        current = items[0]  # Последний уникальный элемент
        self.items = [current]  # Набор уникальных элементов

        for i in range(1, len(items)):
            if ((ignore_case == True or type(items[i]) != str) and items[i] not in self.items):
                self.items.append(items[i])
            if (ignore_case == False and type(items[i]) == str):
                add_flag = True
                for j in self.items:
                    if (type(j) == str and j.upper() == items[i].upper()):
                        add_flag = False
                        break
                if (add_flag):
                    self.items.append(items[i])
        self.len = len(self.items)  # Длина набора уникальных элементов

    def __next__(self):
        if self.index == self.len - 1:
            raise StopIteration
        self.index += 1
        return self.items[self.index]

    def __iter__(self):
        return self


def print_result(func):
    def wrapper(arg):
        print(func.__name__)
        print(func(arg))

    return wrapper


import time
class cm_timer():
    def __init__(self):
        self.start = 0.0
        self.end = 0.0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time.time()
        print('Время выполнения: {} секунд.'.format(self.end - self.start))


path = 'data_light.json'  # Путь к файлу для чтения

with open(path, encoding="utf-8") as f:
    data = json.load(f)


def f1(arg):
    return sorted([i for i in Unique(field(data, 'job-name'), True)])


def f2(arg):
    return list(filter(lambda x: "программист" in x, arg))


def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return tuple(zip(arg, gen_random(len(arg), 100_000, 200_000)))


if __name__ == '__main__':
    with cm_timer():
        f4(f3(f2(f1(data))))