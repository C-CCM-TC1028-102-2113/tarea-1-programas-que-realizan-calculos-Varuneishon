def main():
    #escribe tu código abajo de esta línea

n = (input('Dame un número: '))

l = int (len(n))

try :
    
    if (l == 4) :
        
        n = int (n)
        
        i = 1
        even_count = 0
        odd_count = 0
        zero_count = 0
        
        while (i <= l) :
           
            digit = int (n % 10)
            if (digit == 0) :
                zero_count +=1
            elif (digit %2 == 0) :
                even_count +=1
            else :
                odd_count +=1
            i += 1
            n /= 10
            
        print (f"El número de dígitos pares es:  {even_count}\n")
    

    else :
        print ("Solo numeros de 4 digitos")

except ValueError:
    print("por favor inserta un numero valido")
    pass


if __name__ == '__main__':
    main()
