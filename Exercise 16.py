'''
Enter two numbers and without solving
the multiplication display a legend depending on whether the product is negative, positive or zero.
'''
def multiplicacion(n1,n2):
    mul=n1*n2
    if mul > 0:
        print(f"El resultado es positivo")
    elif mul < 0:
        print(f"El resultado es negativo")
    else:
        print(f"El resultado es nulo")


num1=int(input("Ingrese numero:\n"))
num2=int(input("Ingredse numero:\n"))
multiplicacion(num1,num2)