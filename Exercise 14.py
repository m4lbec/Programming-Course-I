'''
Enter a two-digit number, 
if it is greater than 50, show it inverted. Otherwise show the figure that corresponds to the units.
'''
def inverso(n):
    inv=str(n)
    inver=inv[::-1]

    return inver

def unidades(n):
    unid=str(n)
    uni=unid[-1]

    return uni
num=int(input("Insert number of two digits:\n"))
if num > 50:
    inver=inverso(num)
    print(f"El numero inverso es:{inver}")
else:
    uni=unidades(num)
    print(f"La unidad es {uni}")