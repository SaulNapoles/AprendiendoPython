# Suma
print('1.- Suma\n')
sumando1 = int(input("Introduzca el primer sumando: "))
sumando2 = int(input("Introduzca el segundo sumando: "))
print("Resultado de la suma: ", sumando1 + sumando2)

print('\n')

# Resta Int(Enteros)
print('2.- Resta Int(Enteros)\n')
minuendo = int(input("Introduzca el minuendo: "))
sustraendo = int(input("Introduzca el sustraendo: "))
print("Resultado de la resta: ", minuendo - sustraendo)

print('\n')

# Resta Float(Decimales)
print('3.- Resta Float(Decimales)\n')
minuendo = float(input("Introduzca el minuendo: "))
sustraendo = float(input("Introduzca el sustraendo: "))
print("Resultado de la resta: ", minuendo - sustraendo)

print('\n')

# Multiplicacion Float(Decimales)
print('4.-Multiplicacion Float(Decimales)\n')
multiplicando = float(input("Introduzca el multiplicando: "))
multiplicador = float(input("Introduzca el multiplicador: "))
print("Resultado de la multiplicacion: ", multiplicando * multiplicador)

print('\n')

# Division Float(Decimales)
print('5.-Division Float(Decimales)\n')
dividendo = float(input("Introduzca el dividendo: "))
divisor = float(input("Introduzca el divisor: "))
print("Resultado de la division: ", dividendo / divisor)

print('\n')

#Redondeo
print('6.- Redondeo\n')
dividendo = float(input("Introduzca el dividendo: "))
divisor = float(input("Introduzca el divisor: "))
resultado = round(dividendo / divisor,1)
print("Resultado de la division: ", resultado)
