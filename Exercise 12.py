'''
Calculate the kilometers traveled
by a car knowing the initial and current mileage. Show a legend according to the distance traveled:
For 100 km or less: “Patience, there is a long way to go”
More than 100 km and less than 200: “Stop for breakfast”
More than 200 km: “It is recommended to load fuel”
'''
def dif(initial,kilom):
    r=kilom-initial

    return r



ini=int(input("Ingrese km inicial:\n"))
km=int(input("Ingrese cantidad recorrida:\n"))
re=dif(ini,km)
if re <= 100:
    print("Patience, there is a long way to go ")
elif re > 100 and re < 200:
    print("Stop for breakfast")
elif re > 200:
    print("It is recommend to load fuel")