numeros = [1, 2, 3,]

numeros.append(4)
# .append() -> Adiciona o valor 4 ao FINAL da lista

numeros2 = [5, 6, 7]

numeros.extend(numeros2)
# .extend() -> "Fundir": Adiciona todos os itens de numeros2 ao final de numeros

numeros.insert(4,10)
# .insert() -> Adiciona o valor 10 na posição 4 da lista

numeros.insert(6,10)
# .insert(índice, valor) -> Coloca outro 10 na posição 6

numeros.remove(10)
# .remove() -> Remove APENAS a primeira ocorrência do valor 10 encontrado

print(numeros.pop(2))
# .pop(índice) -> Remove o item pelo ÍNDICE e o "retorna" (mostra qual foi removido)

numeros2.clear()
# .clear() -> Esvazia a lista totalmente, deixando-a como []



numeros2 = [7, 9, 10, 11]

index = numeros2.index(10)



numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

numeros3 = numeros.copy()
print(numeros3)

