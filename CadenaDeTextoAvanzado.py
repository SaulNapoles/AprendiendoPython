# Agregar letra Capital a texto.
cadenaejemplo = "ejemplo agregar capital a cadena de texto"
print('1.-',cadenaejemplo.capitalize())
print('\n')

# Convertir texto a MAYUSCULAS.
cadenaejemplo = "ejemplo convertir a mayusculas una cadena de texto"
print('2.-',cadenaejemplo.upper())
print('\n')

# Método islower(), comprueba si todos los caracteres que componen la cadena están en minúscula.
print('Método islower(), comprueba si todos los caracteres que componen la cadena están en minúscula.')
print('\n')

cadenaejemplo = "Ejemplo con mayuscula"
print('3.-"'+ cadenaejemplo + '" =', cadenaejemplo.islower())
print('\n')

cadenaejemplo = "ejemplo en minusculas"
print('4.-"'+ cadenaejemplo + '" =', cadenaejemplo.islower())
print('\n')

# Método isupper(), comprueba si todos los caracteres que componen la cadena de texto están en mayúscula.
print('Método isupper(), comprueba si todos los caracteres que componen la cadena de texto están en mayúscula.')
print('\n')

cadenaejemplo = "Ejemplo con minusculas"
print('5.- "'+ cadenaejemplo + '" =',cadenaejemplo.isupper())

cadenaejemplo = "EJEMPLO EN MAYÚSCULAS"
print('6.- "'+ cadenaejemplo + '" =',cadenaejemplo.isupper())


# Convertir texto a minusculas.
cadenaejemplo = "EJEMPLO CONVERTIR A MINUSCULAS UNA CADENA DE TEXTO"
print('7.-',cadenaejemplo.lower())
print('\n')

# Longitud de cadena.
cadenaejemplo = "Ejemplo longitud de cadena"
#El + Concatena los valores y el str(TipoDeDato) recibe un tipo de dato y lo convierte a string
print('8.-',cadenaejemplo + ' = ' + str(len(cadenaejemplo)))
print('\n')

# Método isalnum() para saber si una cadena solo tiene caracteres
# alfanumericos (retorna un boleano)
print('Método isalnum() para saber si una cadena solo tiene caracteres alfanumericos (retorna un boleano)')
print('\n')

cadenaejemplo = "Ejemplo de cadena..."
print('9.- Cadena de texto "'+ "Ejemplo de cadena..." '" =',cadenaejemplo.isalnum())
print('\n')

cadenaejemplo = "1234567890"
print('10.- Cadena de texto "'+ '1234567890"' + '" =',cadenaejemplo.isalnum())
print('\n')

cadenaejemplo = "abcdefg1234567890"
print('11.- Cadena de texto "'+ 'abcdefg1234567890"' + ' =' ,cadenaejemplo.isalnum())
print('\n')

cadenaejemplo = "abcdefg 1234567890"
print('12.- Cadena de texto "' + 'abcdefg 1234567890"' + ' =',cadenaejemplo.isalnum())
print('\n')



# Método isalpha() comprueba si todos los caracteres de la cadena de texto son caracteres alfabéticos.

print('Método isalpha() comprueba si todos los caracteres de la cadena de texto son caracteres alfabéticos.')
print('\n')

cadenaejemplo = "EjemploDeCadena"
print('13.- Cadena de texto "'+ 'EjemploDeCadena' + '" =',cadenaejemplo.isalpha())
print('\n')

cadenaejemplo = "Ejemplo De Cadena"
print('14.- Cadena de texto "'+ 'Ejemplo De Cadena' + '" =',cadenaejemplo.isalpha())
print('\n')

cadenaejemplo = "45764632"
print('15.- Cadena de texto "'+ '45764632' + '" =',cadenaejemplo.isalpha())
print('\n')

cadenaejemplo = "hsryjrjw 038096743"
print('16.- Cadena de texto "'+ 'hsryjrjw 038096743' + '" =',cadenaejemplo.isalpha())
print('\n')


# Método isdigit(), que comprueba si todos los caracteres de la cadena de texto son caracteresnuméricos.

print('Método isalpha() comprueba si todos los caracteres de la cadena de texto son caracteres alfabéticos.')
print('\n')

cadenaejemplo = "EjemploDeCadena"
print('17.- Cadena de texto "'+ 'EjemploDeCadena' + '" =',cadenaejemplo.isdigit())
print('\n')

cadenaejemplo = "Ejemplo De Cadena"
print('18.- Cadena de texto "'+ 'Ejemplo De Cadena' + '" =',cadenaejemplo.isdigit())
print('\n')

cadenaejemplo = "45764632"
print('19.- Cadena de texto "'+ '45764632' + '" =',cadenaejemplo.isdigit())
print('\n')

cadenaejemplo = "hsryjrjw 038096743"
print('20.- Cadena de texto "'+ 'hsryjrjw 038096743' + '" =',cadenaejemplo.isdigit())
print('\n')

# Métodos lstrip(), rstrip() y strip() permitirte eliminar espacios en blanco al principioy al final de la cadena de texto.
print('Métodos lstrip(), rstrip() y strip() permitirte eliminar espacios en blanco al principioy al final de la cadena de texto.')
print('\n')

cadenaejemplo = " Ejemplo borrar espacio al principio"
print('21.-'+cadenaejemplo.lstrip())

cadenaejemplo = "Ejemplo borrar espacio al final "
print('22.-'+cadenaejemplo.rstrip())

cadenaejemplo = " Ejemplo borrar espacios al principio y final "
print('23.-'+cadenaejemplo.strip())
print('\n')

# Método max() y min(), permiten conocer el carácter alfabético mayor y menor de la cadena de texto.
print('Método max() y min(), permiten conocer el carácter alfabético mayor y menor de la cadena de texto.')
print('\n')

cadenaejemplo = "abcdefghijklmnopqrstuvwxyz"
print('24.- Caracter Mayor =',max(cadenaejemplo))
print('25.- Caracter Menor =',min(cadenaejemplo))
print('\n')

# Método replace(), permite reemplazar caracteres de la cadena de texto por otros caracteres.
print('Método replace(), permite reemplazar caracteres de la cadena de texto por otros caracteres.')
print('\n')

cadenaejemplo = "AAEIOU"
print('26.- Cadena original "AAEIOU" reemplazar E por las A de la cadena, resultado =',cadenaejemplo.replace('A','E'))
print('\n')

# Método swapcase(), permite invertir las mayúsculas y minúsculas de la cadena de texto
print('Método swapcase(), que te va a permitir invertir las mayúsculas y minúsculas de la cadena de texto')
print('\n')

cadenaejemplo = "Ejemplo"
print('27.-',cadenaejemplo.swapcase())
print('\n')

# Método split, permite convertir una cadena de texto en una lista de elementos que se encuentran separados por espacios en la cadena de texto original.
print('Método split, permite convertir una cadena de texto en una lista de elementos que se encuentran separados por espacios en la cadena de texto original.')
print('\n')

cadenaejemplo = "Ejemplo cadena de texto"
print('28.-"' + 'Ejemplo cadena de texto" =' ,cadenaejemplo.split())
print('\n')

# Método split(), pero, esta vez, indicándole el carácter que tiene que utilizar para separar los elementos de la lista.
print('Método split(), pero, esta vez, indicándole el carácter que tiene que utilizar para separar los elementos de la lista.')
print('\n')

cadenaejemplo = "22/10/2021"
print('29.- Cadena de texto "' + '22/10/2021" =',cadenaejemplo.split("/"))
