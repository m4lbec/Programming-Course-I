'''
Calculate the amount that a car must pay in a parking lot taking into account the hours and minutes 
of use as data. The value of the hour 
is $45 and if the minutes exceed 15, the amount is increased by one hour. The minimum charge is one hour.
'''

def park(minutos):

    hours=minutos/60
    h=hours*45

    return h
    



min=int(input("Ingrese cantidad de minutos:\n"))
if min > 15:
    h=park(min)
    print(f"Debera pagar: {h}")
else:
    print("Despues de los 15 min se cobra la hora")
