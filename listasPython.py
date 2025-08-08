#Exemplo 1
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, 2, 'Esther', 'Hadassa', 4, 4.5]

print(lista1)
print(30* '*')
print(lista2)


#Exemplo 2 Adiciona um dado na última posição - lista.append('dado') (INSERT)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, 2, 'Esther', 'Hadassa', 4, 4.5]

print(lista1)
print(30* '*')
print(lista2)

lista2.append('Valeria')
print(lista2)

print(30* '*')


#Exemplo 3 lista.insert()
nomes = ['Evani', 'Romeu', 'Nilton', 'Júnior']
print(nomes)

nomes.insert(2, 'Liah')
print(nomes)

print(30* '*')


#Exemplo 4 Alterando um dado existente - (UPDATE)
linguagens = ['Python', 'Java', 'JavaScript', 'Php']
print(linguagens)

linguagens[3] = ['C++']
print(linguagens)

print(30* '*')


#Exemplo 5 Removendo um dado da lista - lista.remove() (DELETE)
lista2.remove('Valeria')
print(lista2)

print(30* '*')


#Exemplo 6 Deletando dado via indice - (DELETE)
lista3 = ['Carlos', 'Mauricio', 'Allan', 'Clodoaldo']
del lista3[1]

print(lista3)

print(30* '*')


#Exemplo 7 Remove dados - (DELETE)
listaNumeros = [100, 200, 300, 459, 400, 500]
print(listaNumeros)

listaNumeros.pop() #Remove o último dado registrado
print(listaNumeros)

listaNumeros.pop(-4) #Remove o registro indicado no índice
print(listaNumeros)

print(30* '*')


#Exemplo 8 Posição do elemento lista.index('nome do elemento')
lista4 = ['Maçã', 'Morango', 'Mixirica', 'Laranja']
print(lista4)

print(lista4.index('Maçã'))

print(30* '*')


#Exemplo 9 Verificação com operadores - Operador 'in'
lista4 = ['Maçã', 'Morango', 'Mixirica', 'Laranja']
print(lista4)

print(lista4.index('Maçã'))

print('Uva' in lista4)
print('Morango' in lista4)

print(30* '*')


#Exemplo 10 Contatenar listas
umaLista = [1, 2, 3]
outraLista = [10, 20, 30]
novaLista = umaLista + outraLista

print(novaLista)

print(30* '*')


#Exemplo 11 Repetição de listas
lista = [1, 2, 3, 4, 5]
listaRepeticao = lista * 3
print(listaRepeticao)

print(30* '*')


#Exemplo 12 Somando os valores de uma lista - SUM
lista5 = [2, 4, 5, 6]
print(sum(lista5))


#Exemplo 12 Menor(min) e maior(max) valor
list01 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(min(list01))
print(max(list01))

print(30* '*')


#Exemplo 13 len(lista)
lista6 = [10, 20, 30, 50, 70]
print(len(lista6))

print(30* '*')


#Exemplo 13 Primeiro e últimos intens da lista
list01 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print('Primeiro item da lista', list01[0])
print('Último item da lista', list01[-1])

print(30* '*')


#Exemplo 14 Lista ordenadas
desordem =  [320, 530, 1220, 12, 743, 839, 75, 100, 29, 18, 761, 900, 275, 600, 1, 99]
desordem.sort(reverse=False)
print(desordem)

print(40* '#')

nomes = ['Camila', 'Thais', 'Diva', 'Francisco']
nomes.sort(reverse=False)
print(nomes)

print(30* '#')


#Exemplo 15 Entrada de dados via input
minhaLista = []
minhaLista.append(input('Digite um valor para inserir à lista: '))

print(minhaLista)

print(30* '#')


#Exemplo 16 Entrada de dados via input - Laço FOR
minhaLista = []
for i in range (1 ,5):
    minhaLista.append(input('Digite um valor para inserir à lista: '))

print(minhaLista)

print(30* '#')


#Exemplo 17 Imprimindo uma lista
desordem = [320, 530, 1220, 12, 743, 839, 75, 100, 29, 18, 761, 900, 275, 600, 1, 99]

for i in desordem:
    print(i)

print('Fim da Lista!!!')

print(30* '#')


#Exemplo 18 Imprimindo uma lista usando operador range
desordem = [320, 530, 1220, 12, 743, 839, 75, 100, 29, 18, 761, 900, 275, 600, 1, 99]

for i in range(1, 6):
    print(desordem[i])

print('Fim da Lista!!!')

print(30* '#')


#Exemplo 19 List.clear - ultilizado para limpar (apagar) todos os itens da lista
listAnimais = ['Cabrito', 'Cavalo', 'Abelha', 'Jumento']
print(listAnimais)

listAnimais.clear()
print(listAnimais)
#EOF