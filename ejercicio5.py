#5.	Elabore una funcion1() 
# y una función2() que sumen y multipliquen 
# respectivamente todos los números de una lista.
# Por ejemplo: funcion1([1,2,3,4]) debería imprimir 10 
# y funcion2([1,2,3,4]) debería devolver 24. 
def suma(a):
    total=0
    for i in range(len(a)):
        total +=a[i]
    return total
def producto(a):
    total=1
    for i in range(len(a)):
        total*=a[i]
    return total
print(suma([1,2,3,4]))
print(producto([1,2,3,4]))