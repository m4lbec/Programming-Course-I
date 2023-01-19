'''
Enter the code for the type of call: 1. Local 2. Interurban 3. 
International and the duration in minutes of the call. If the minute costs $0.25 for the local call, 
$0.40 for the long-distance call, and $1.05 for 
the international call, design an algorithm that allows calculating the amount to be paid for said call.
'''
def localcall(cod,m):
    lc=m*0.25

    return lc

def interurbancall(cod,m):
    ic=m*0.40

    return ic
    
def internationalcall(cod,m):
    iic=m*1.05

    return iic





code=int(input("Ingrese opcion:\n1-Local\n2-Interurban\n3-International"))
min=int(input("Ingrese minutos de llamada:\n"))
if code == 1:
    lc=localcall(code,min)
    print(f"El costo de llamada es: {lc}")
elif code == 2:
    ic=interurbancall(code,min)
    print(f"El costo de llamada es: {ic}")
elif code ==3:
    iic=internationalcall(code,min)
    print(f"El costo de llamada es: {iic}")