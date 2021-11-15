def mayor(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
numero_mayor=mayor(10,20,50)
print(numero_mayor)