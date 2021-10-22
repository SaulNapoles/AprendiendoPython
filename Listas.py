# Lista en una variable y en mostrarla por pantalla.
print('1.- Lista en una variable y en mostrarla por pantalla.\n')
lista = ["ordenador","teclado","raton"]
print(lista)

print('\n')

# Lista en una variable, mostrar longitud de la lista.
# y cada elemento de la lista por separado
print('2.- Lista en una variable, mostrar longitud de la lista y cada elemento de la lista por separado\n')
lista = ["ordenador","teclado","raton"]
print(len(lista))
print(lista[0])
print(lista[1])
print(lista[2])

print('\n')

# Suma de 2 listas en una variable mostrada en pantalla.
print('3.- Suma de 2 listas en una variable mostrada en pantalla.\n')
listaoriginal = ["ordenador","teclado","raton"]
listanueva = ["monitor","impresora","altavoces"]
listafinal = listaoriginal + listanueva
print(listafinal)

print('\n')

# Impresión de lista e impresión de la misma lista sumandole un nuevo elemento.
print('4.- Impresión de lista e impresión de la misma lista sumandole un nuevo elemento.\n')
lista = ["ordenador","teclado","raton"]
print(lista)
lista = lista + ["mesa"]
print(lista)

print('\n')

# Modificacion por elemento de la lista.
print('5.- Modificacion por elemento de la lista.\n')
lista = ["ordenador","teclado","raton"]
print(lista)
lista[0] = "monitor"
lista[1] = "impresora"
lista[2] = "altavoces"
print(lista)

print('\n')

# Eliminar segundo elemento de la lista
print('6.- Eliminar segundo elemento de la lista.\n')
lista = ["ordenador","teclado","raton"]
print(lista)
del lista[1]
print(lista)

print('\n')

# Lista compuesta por cadenas de texto y una lista de elementos de tipo de dato lista
print('7.- Lista compuesta por cadenas de texto y una lista de elementos de tipo de dato lista.\n')
lista = ["ordenador","teclado","raton", ["tarjeta de sonido","microfono","altavoces"]]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[3][0])
print(lista[3][1])
print(lista[3][2])
