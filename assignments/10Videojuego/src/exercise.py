def main():
    #escribe tu código abajo de esta línea
    import math
print("Este programa calcula el costo total de una compra" )

v1 = int(input("Dame la cantidad de juegos nuevos : "))
v2 = int(input("Dame la cantidad de juegos usados : " ))

p1 = v1*1000
p2 = v2*350
pt = p1+p2

print("El total de la compra es:" ,pt)
   pass



if __name__ == '__main__':
    main()
