
def correlation(lista1, lista2):
    x = sum(lista1)/len(lista1)
    y = sum(lista2)/len(lista2)
    
    suma1 = 0
    suma2 = 0
    suma3 = 0
    
    for i in range(0, len(lista1)):
        suma1 += (lista1[i]-x)*(lista2[i]-y)
        suma2 += (lista1[i]-x)**2
        suma3 += (lista2[i]-y)**2
        
    raiz = (suma2*suma3)**(1/2)
    # suma2 = math.sqrt(suma2)
    # suma3 = math.sqrt(suma3)
    # raiz = suma2 * suma3
    correlacion = suma1/raiz
    
    return correlacion


""" 
Atajo:
    ⌘ Z
    ⌘ ⇧ Z
    Ctrl +Z
    Ctrl + Shift + Z
 """