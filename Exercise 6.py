'''
Enter a number. If it is positive, calculate its square root,
if it is negative, show its square, and if it is zero, show “Error. You have entered a null value.”
'''
def raiz(n):
    m=n**(0.5)
    return m
def cuadrado(n):
    c=n*n
    return c




num=int(input("Ingrese numero:\n"))
if num > 0:
    r=raiz(num)
    print(f"La raiz cuadrada es {r}")
    
elif num < 0:
    cu=cuadrado(num)
    print(f"El cuadrado es {cu}")
else:
    print(f"Error. You have entered a null value!")
