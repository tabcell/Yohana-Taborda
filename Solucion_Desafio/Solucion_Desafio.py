print('Ingrese sus 5 calificaciones, una por una:')
cal1 = float(input("Ingrese su primera calificación:"))
cal2 = float(input("Ingrese su segunda calificación:"))
cal3 = float(input("Ingrese su tercera calificación:"))
cal4 = float(input("Ingrese su cuarta calificación:"))
cal5 = float(input("Ingrese su quinta calificación:"))
suma = cal1 + cal2 + cal3 + cal4 + cal5
promedio = suma / 5
print("Su promedio es:", promedio)
if promedio>=60:
    print('Aprobado')
elif promedio>=40 and promedio <=59:
    print('En recuperación')
else:
    print('Reprobado')