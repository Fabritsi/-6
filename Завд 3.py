import math
def znach(x,y):
    return (math.pow(x,2)+math.pow(y,2))
a = float(input("a= (Для першого і другого векторів)"))
b = float(input("b= (Для першого вектора)"))
c = float(input("c= (Для другого вектора)"))

S=2*znach(a,b) - 3*znach(a,c)
print("Відповідь:{}".format(S))
