print("Mas sobre funciones")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s = a+b
    return s

# Lamada de funciones
print("CALCULANDO SUMA AB")
n1 = int(input("Ingrese el 1er numero "))
n2 = int(input("Ingrese el 2do numero "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es de: {suma}")

def res_cd(c,d):
    r = c-d
    return r
print("CALCULANDO RESTA")
n3 = int(input("Ingrese el 1er numero "))
n4 = int(input("Ingrese el 2do numero "))
resta=res_cd(n3,n4)
print(f"La resta de {n3} - {n4} es de: {resta}")

def mul_ef(e,f):
    mul = e*f
    return mul
print("CALCULANDO MULTIPLICACION")
n5 = int(input("Ingrese el 1er numero "))
n6 = int(input("Ingrese el 2do numero "))
mult=mul_ef(n5,n6)
print(f"La multiplicacion de {n5} * {n6} es de: {mult}")

def div_gh(g,h):
    div = g/h
    return div
print("CALCULANDO DIVISIONES")
n7 = float(input("Ingrese el 1er numero "))
n8 = float(input("Ingrese el 2do numero "))
div=div_gh(n7,n8)
print(f"La division de {n7}/{n8} es de: {div}")