#YOHEL PEREZ 98100658321

L = input('ingrese una lista de numeros')
L = tuple(item for item in L.split(',') if item.strip())
iteraciones = 0 # Contador de iteraciones
ban = False
bajo = 0
alto = len(L) - 1
clave =int(input('que numero quiere buscar?'))
print('clave: ', str(clave))

while bajo <= alto: # Recorrido de la lista ** Inicio del ciclo **
    central = bajo + alto
    central = central // 2
    if int(L[central]) ==clave:
        iteraciones = iteraciones + 1
        intervalo = L[bajo:alto+1]
        print('iteracion:' + str(iteraciones) + ', central:' + str(central) + ', L[' + str(central) + ']:' + str(L[central]) + ', intervalo:' + str(intervalo))

        print('numero encontrado en la posicion ' + str(central))

        print('cantidad de iteraciones ' + str(iteraciones))
        ban = True
        break
    else:
        if int(L[central]) < clave:
            intervalo = L[bajo:alto+1]
            bajo = central +1
            iteraciones = iteraciones + 1
            print('iteracion:' + str(iteraciones) + ', central:' + str(central) + ', L[' + str(central) + ']:' + str(L[central]) + ', intervalo:' + str(intervalo))
        else:
            intervalo = L[bajo:alto+1]
            alto = central +1
            iteraciones = iteraciones +1
            print('iteracion:' + str(iteraciones) + ', central:' + str(central) + ', L[' + str(central) + ']:' + str(L[central]) + ', intervalo:' + str(intervalo))

if ban == False:
    print('la clave no esta en la lista')
    print('cantidad de iteraciones ' + str(iteraciones))