#!/usr/bin/python3
""" 1-main """
from models.rectangle import Square

if __name__ == "__main__":

    Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 =Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
