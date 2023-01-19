'''
Enter the measure of an angle and determine if it is acute, obtuse, right, zero, or straight. 
If the value entered is greater than 180o, display the legend "invalid angle" and enter a new value.
'''
def agudo(a):
    print(f"Angulo agudo")

def obtuso(a):
    print(f"Angulo obtuso")

def recto(a):
    print(f"Angulo recto")


ang=int(input("Ingrese medida de angulo:\n"))
if ang < 90:
    agudo(ang)
elif ang == 90:
    recto(ang)
elif ang > 90 and ang <=180:
    obtuso(ang)
elif ang > 180:
    print(f"Angulo invalido")

