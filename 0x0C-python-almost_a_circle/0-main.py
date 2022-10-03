#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = base()
    print(b3.id)

    b4 = base(12)
    print(b4.id)

    b5 = base()
    print(b5.id)
