# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    """remover los elementos que esten en la posición 1,5 y 6 de una lista que no sabemos el largo"""
   # me fijo si la lista tiene al menos 7 elementos
    if len(list_to_remove_elements)==6:
        del list_to_remove_elements[5]
        del list_to_remove_elements [4]
        del list_to_remove_elements[0]
    
    if len(list_to_remove_elements) == 4:
        del list_to_remove_elements [0]

    return list_to_remove_elements


def add_elements(list_to_add_elements):
    """agrego pink al principio de la lista y yellow al final de la lista"""
    #primero agrego pink al principio de la lista
    list_to_add_elements.insert(0,"Pink")
    #ahora agrego yellow al final de la lista
    list_to_add_elements.append("Yellow")

    return list_to_add_elements


def is_empty(list_to_check):
    """que diga si la lista esta vacia o no"""
    if len(list_to_check)==0:
        return True
    else:
        return False
    


def check_lists(list_to_compare1, list_to_compare2):
    """compara si el 3er elemento de las dos listas son iguales, pero no se el largo de la lista"""
    #me fijo si la lista tiene al menos 3 elementos
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False


def list_of_lists(lista1 ,lista2, lista3):
    """de la primera lista solo se queda con los primeros dos elementos. de la segunda lista solo se quede con los elementos entre el segundo y cuarto elemento.De la tercera lista solo se quede con los ultimos 2 elementos(no se sabe el largo de las listas internas)"""
    #me fijo si la lista1 tiene al menos dos elementos
    if len(lista1) >= 2:
        lista1 = lista1[0:2]
    elif len(lista1) < 2:
        lista1 = lista1[0:1]
        return lista1

    #me fijo si la lista2 tiene al menos 4 elementos
    if len(lista2) >= 4:
        lista2 = lista2[1:4]
    elif len(lista2) < 4:
        lista2 = lista2[1:]
        return lista2
    #quiero los ultimos dos elementos de la lista3
    lista3==lista3[-2:]
    return lista3
  
