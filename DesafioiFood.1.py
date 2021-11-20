def organizarLista(lista):
    for x in range(len(lista)):
        for y in range(x + 1, len(lista)):
            if lista[x] > lista[y]:
                auxiliar = lista[x]
                lista[x] = lista[y]
                lista[y] = auxiliar


def reverterLista(lista):
    for x in range(1, len(lista)):
        auxiliar = lista[x]
        y = x
        while y > 0 and lista[y - 1] < auxiliar:
            lista[y] = lista[y - 1]
            y -= 1
            lista[y] = auxiliar


agrupadoPorNotas = [[]]

listaRestaurantes = [
    [4.9, 6.99, 'Kibon Sorveteria - Saúde'],
    [4.6, 7.99, 'Sukiya - Saúde'],
    [4.4, 9.90, 'A Feijoada'],
    [4.7, 7.99, 'Makis Place - Saúde'],
    [4.4, 5.99, 'Giraffas Carrefour Metrocar'],
    [4.4, 12.49, 'Viena - Shopping Santa Cruz']
]

organizarLista(listaRestaurantes)
reverterLista(listaRestaurantes)

notaAtual = listaRestaurantes[0][0]

cont = 0
for listaOrdenada in listaRestaurantes:
    if listaOrdenada[0] != notaAtual:
        agrupadoPorNotas.append([])
        cont += 1
    notaAtual = listaOrdenada[0]
    agrupadoPorNotas[cont].append(listaOrdenada)

cont = 1
for subLista in agrupadoPorNotas:
    organizarLista(subLista)
    for listaOrdenada in subLista:
        print("\n{}º) {}\n    Nota: {}\n    Frete: R${:.2f}".format(cont, listaOrdenada[2], listaOrdenada[0], listaOrdenada[1]))
        cont += 1
