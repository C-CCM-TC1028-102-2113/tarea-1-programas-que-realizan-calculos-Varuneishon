def main():
    #escribe tu código abajo de esta línea
n = float (input ("Dame el numero de paginas: " ))

p = float((n//475)*60)
p1 = float(n%475)

if p>=1:
    c1 = float(p)+60
    c2 = float(c1)*0.9
    print("El costo de la publicación es: ", c2)

else:
    e = float(p)*0.9
    print("El costo de la publicación es: ", p)
    pass


if __name__ == '__main__':
    main()
