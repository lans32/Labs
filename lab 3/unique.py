class unique(object):
    def __init__(self, items, **kwargs):
        if "ignore_case" not in kwargs.keys():
            self._ignore_case = False
        else:
            self._ignore_case = kwargs["ignore_case"]
        self.uniq_items = []
        for i in items:
            if self._ignore_case:
                temp = i.lower()
            else:
                temp = i
            if temp not in self.uniq_items:
                self.uniq_items.append(temp)
        self.index = 0

    def __next__(self):
        if self.index != len(self.uniq_items):
            print(self.uniq_items[self.index])
            self.index+= 1

    def __iter__(self):
        return self

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
result = iter(unique(data))
next(result)
next(result)
next(result)
next(result)

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
result = iter(unique(data, ignore_case = True))
next(result)
next(result)
next(result)
next(result)
