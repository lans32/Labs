def field(array, *arg):
    result = []
    for i in array:
        if len(arg) == 1:
            if i[arg[0]] != None:
                result.append(i[arg[0]])
        else:
            buf = dict()
            for j in arg:
                if i[j] != None:
                    buf[j] = i[j]
            result.append(buf)
    print(result)


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 ]
field(goods, 'title')
field(goods, 'title', 'price')

