#3.	Elabore una función que calcule la longitud de
# una lista o una expresión de texto ingresada por teclado. 
def longitud(a):
    return len(a)
x=input("ingrese un texto: ")
print("la longitud del texto es: ",longitud(x))