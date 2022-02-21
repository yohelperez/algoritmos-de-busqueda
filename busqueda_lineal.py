#YOHEL PEREZ 9810065321

L = input('ingrese una lista de numeros ' )
ban = False # Bandera que indica si se encontro
            # la clave en la lista tal que:
            # -> Ban = False, la clave no esta en la lista
            # -> Ban = True, la clave esta en la lista
L = tuple(item for item in L.split(',') if item.strip())
clave = int(input('que numero quiere buscar?')) # Valor de prueba para buscar en la lista
n =int(len(L))
i=0
iteraciones =0
print('clave:' + str(clave) + '\n') # Imprima el mensaje donde se muestre la clave

while i <= n-1:
    p = L[i]
    if int(p) == clave:
        ban = True
        iteraciones = iteraciones +1
        print('iteracion:' + str(i) + ', L['+ str(i)+ ']='+ str(p) + '\n')
        print('la clave está en la posicion:',i) # Imprima el mensaje en el cual se informe la posición
        break
    else:
        iteraciones = iteraciones + 1
        print('iteracion:' + str(i) + ', L['+ str(i)+ ']='+ str(p))# Imprima el mensaje en el cual se muestre cada elemendo de la iteración
        i = i +1
if ban == True:
    print('cantidad de iteraciones:' + str(iteraciones))
else: # Verifique si la clave se encontró
    print('la clave no está en la lista') # Recorrido de la lista ** Fin del ciclo **
    print('cantidad de iteraciones ' + str(iteraciones))