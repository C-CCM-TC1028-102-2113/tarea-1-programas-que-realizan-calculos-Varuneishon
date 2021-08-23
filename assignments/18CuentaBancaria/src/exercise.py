def main():
    #escribe tu código abajo de esta línea
  
import math

x1 = float(input("Dame el saldo del mes anterior: "))
x2 = float(input("Dame los ingresos: "))
x3 = float(input("Dame los egresos: "))
x4 = int(input("Dame el numero de cheques: "))

s = x1+x2-x3-(x4*13)

sf=s*0.925
sf=round(sf,5)

print("El saldo final de la cuenta es", sf)
    pass

if __name__ == '__main__':
    main()
