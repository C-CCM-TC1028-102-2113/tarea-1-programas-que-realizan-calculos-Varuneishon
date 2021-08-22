def main():
    #escribe tu código abajo de esta línea

n = (input('Dame un número: '))

l = int (len(n))

try :
    
    if (l == 4) :
        
        n = int (n)
        
        i = 1
        e = 0
        o = 0
        z = 0
        
        while (i <= l) :
           
            d = int (n % 10)
            if (d == 0) :
                z +=1
            elif (d %2 == 0) :
                e +=1
            else :
                o +=1
            i += 1
            n /= 10
            
        print (f"El número de dígitos pares es:  {e}\n")
    

    else :
        print ("Solo numeros de 4 digitos")

except ValueError:
    print("por favor inserta un numero valido")
    pass


if __name__ == '__main__':
    main()
