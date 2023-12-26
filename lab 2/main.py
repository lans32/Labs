from rectangle import Rectangle
from circle import Circle
from square import Square


def main():
    r = Rectangle("red", 2, 2)
    c = Circle("cyan", 2)
    s = Square("green", 2)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
