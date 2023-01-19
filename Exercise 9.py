'''
Enter the value
of a company's annual profit and calculate its withholding as it falls within the following parameters:
Revenue                      Retention
<= 10000                     Cero
>10000 y <= 15000            2% sobre (ganancia -10000) 
> 150000                     300+5% sobre (ganancia -15000)
'''
def ret1(n):
    print(f"Presenta cero retencion de {n}")
def ret2(n):
    r=n*0.02/(n-1000)
    print(f"La retencion2 sera de {r}")
def ret3(n):
    r=300+(n*0.05)/(n-15000)
    print(f"La retencion3 sera de {r}")

num=int(input("Ingrese valor de revenue:\n"))
if num <=10000:
    ret1(num)
elif num>10000 and num<=15000:
    ret2(num)
elif num>15000:
    ret3(num)