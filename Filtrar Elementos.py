numeros = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
pares = [num for num in numeros if num % 2 == 0] 
cadenas = ['Salud', 'Cadena', 'Paises', 'Programacion']
filtradas = [cadena for cadena in cadenas if 'e' in cadena] 
print(pares, filtradas) 