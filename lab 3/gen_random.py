import random
def gen_random(num_count, begin, end):
    return [random.randint(begin, end) for i in range(0, num_count)]

print(gen_random(5, 1, 3))
