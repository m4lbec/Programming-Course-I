'''
Enter the measures of two angles expressed in degrees minutes and seconds and find the sum. 
(remember that minutes and seconds must not exceed 60)
'''

grados_1 = int(input("Ingrese los grados del angulo: "))
minutos_1 = int(input("Ingrese los minutos del angulo: "))
segundos_1 = int(input("Ingrese los segundos del angulo: "))

grados_2 = int(input("Ingrese los grados del angulo: "))
minutos_2 = int(input("Ingrese los minutos del angulo: "))
segundos_2 = int(input("Ingrese los segundos del angulo: "))

suma_segundos = segundos_1 + segundos_2 
if suma_segundos >= 60:
    minutos_extra = suma_segundos // 60
    suma_segundos = suma_segundos % 60
else:
    minutos_extra = 0
suma_minutos = minutos_1 + minutos_2 + minutos_extra
if suma_minutos >= 60:
    grados_extra = suma_minutos // 60
    suma_minutos = suma_minutos % 60
else:
    grados_extra = 0
suma_grados = grados_1 + grados_2 + grados_extra

print(f"La suma de los angulos es de {suma_grados}º {suma_minutos}' {suma_segundos}''")
