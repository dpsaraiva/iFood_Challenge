agrupadoPorNotas = [[]]

listaRestaurantes = [
    [4.9, 6.99, 'Kibon Sorveteria - Saúde'],
    [4.6, 7.99, 'Sukiya - Saúde'],
    [4.4, 9.90, 'A Feijoada'],
    [4.7, 7.99, 'Makis Place - Saúde'],
    [4.4, 5.99, 'Giraffas Carrefour Metrocar'],
    [4.4, 12.49, 'Viena - Shopping Santa Cruz']
]

listaRestaurantes.sort()
listaRestaurantes.reverse()

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
    subLista.reverse()
    for listaOrdenada in subLista:
        print("\n{}º) {}\n    Nota: {}\n    Frete: R${:.2f}".format(cont, listaOrdenada[2], listaOrdenada[0], listaOrdenada[1]))
        cont += 1