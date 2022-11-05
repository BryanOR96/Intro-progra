

print("vamos a calcular el precio del lote con forma triangular ")
base= int(input("Digite la base del lote "))
altura=int(input("Digite la altura del lote "))        
PxM = int(input("Digite el precio por metro cuadrado "))
Area= base*altura
total=PxM*Area
print("El precio total a pagar por un lote de un area total de :",Area, "mts cuadrados es de ",total,)
print()
print()

print("vamos a calcular el precio del lote con forma pentagonal ")
lado= int((input("Digite la medida del lado del lote ")))
apotema=int((input("Digite la medida de la apotema del lote ")))        
PxM = int(input("Digite el precio por metro cuadrado "))
perimetro = lado*5
Area1= perimetro*apotema/2
total1=PxM*Area
print("El precio total a pagar por un lote de un area total de :",Area1, "mts cuadrados es de ",total1,)