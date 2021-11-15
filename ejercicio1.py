#1.	Elabore una función que 
# tome como argumento dos números enteros 
# y devuelva el mayor.
def mayor(a, b):
    if a>b:
        return a
    else:
        return b

numero_mayor=mayor(10,20)
print(numero_mayor)