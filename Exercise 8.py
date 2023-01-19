'''
Enter two numbers, calculate and display the quotient of the first by the second, as 
long as the divisor is not zero. In the latter case, display the legend “the quotient cannot be done”.
'''

def cociente(n1,n2):
    if n2 != 0:
        c=n1/n2
        print(f'El cociente de los numeros es: {c}')
    else:
        print(f"El cociente no se puede realizar")


num1=int(input("Ingrese numero que quiere dividir:\n"))
num2=int(input("Ingrese numero que va a dividir al primero:\n"))
cociente(num1,num2)