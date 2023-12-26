def print_result(func):
    def wrapper():
        print(func.__name__)
        i = func()
        if type(i) == type(dict()):
            for key, value in i.items():
                print(key, '=', value)
        elif type(i) == type(list()):
            for value in i:
                print(value)
        else:
            print(i)
    return wrapper

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
        
