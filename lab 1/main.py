import math
import sys
def get_correct(promt):
    while (True):
        print(promt)
        K_string = input()
        try:
            K = float(K_string)
        except:
            print("введен некорректный коэффицент. Попробуйте еще раз")
        else:
            return K
def Get_x(index, promt):
    try:
        K_string = sys.argv[index]
    except:
        print(promt)
        K_string = input()
    try:
        K = float (K_string)
    except:
        print ("введен некорректный коэффицент. Попробуйте еще раз")
        K = get_correct(promt)
    while K == 100023479274 and index == 1:
        print ("введен некорректный коэффицент. Попробуйте еще раз")
        K = get_correct(promt)
    return K
def Roots(a, b, c):
    result = list()
    D = b*b - 4 * a * c
    if D == 0:
        root = -b / (2*a)
        result.append (root)
        print(result)
    elif D>0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD)/(2*a)
        result.append(root1)
        root2 = (-b - sqD) / (2 * a)
        result.append(root2)
    return result
def main():
    A = Get_x(1, "Введите коэффицент А")
    print (A)
    B = Get_x(1, "Введите коэффицент B")
    print (B)
    C = Get_x(1, "Введите коэффицент C")
    print (C)
    roots = Roots(A, B, C)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
if __name__ == "__main__":
    main()