"""
Convert lengths from miles to km and from inches to cm, if: 1 mile = 1.60935 km.
1 inch = 2.534 cm
"""
"""
len=float(input("Inserte longitud en millas:\n"))
km=len*1.60935

len2=float(input("Inserte longitud en inch:\n"))
cm=len2*2.534

print(f"La medida en km es {km} y la medida en cm es {cm}")
"""

def millas(le):
    km=le*1.60935

    return km

def inches(le2):
    cm=le2*2.534

    return cm


len=float(input("Insert lenght to convert from miles to km:\n"))
len2=float(input("Insert lenght to convert from inches to cm:\n"))
cm=inches(len2)
km=millas(len)

print(f"{len} miles = {km} km")
print(f"{len2} inches = {cm} cm")
