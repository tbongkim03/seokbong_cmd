from seokbong_add.add import add
from seokbong_division.divide import seokbong_division

def call():
    choose = int(input("덧셈(1), 곱셈(2), 나눗셈(3) 입력 : "))
    if choose == 1:
        add()
    else if choose == 2:
        mul()
    else if choose == 3:
        divide()
    else:
        print("num err")
        break
