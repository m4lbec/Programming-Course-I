'''
Enter the ages of two people. If one of them is
of legal age and the other is a minor, calculate and display their average. Otherwise show the two ages
'''


def average(ed1,ed2):
    if (ed1 > 18 and ed2<18) or (ed1<18 and ed2>18):
        prom=(ed1+ed2)/2
        print(f"El promedio es {prom}")
    else:
        print(f"Las edades son {ed1} y {ed2}")


edad1=int(input("Ingrese primera edad:\n"))
edad2=int(input("Ingrese segunda edad:\n"))
average(edad1,edad2)
