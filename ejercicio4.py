#4.	Elabore una función que lea un carácter y devuelva 
# rue si es una vocal, de lo contrario que devuelva False
def vocal(x):
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
      return True
    return False 
letra=(input("ingrese una letra: "))
print(vocal(letra))
