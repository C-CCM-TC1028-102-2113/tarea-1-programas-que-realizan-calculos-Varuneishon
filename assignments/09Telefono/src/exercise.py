def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
print("Este programa calcula el costo total de un plan mensual" )

t1 = int(input("Dame número de mensajes : "))
t2 = float(input("Dame número de megas : " ))
t3 = int(input("Dame número de minutos : " ))

tf = (t1+t2+t3)*0.8
tf = round(tf,2)

print("El costo mensual es:" ,tf)
    pass


if __name__ == '__main__':
    main()
