# exemplos de laços for 

#1º laço while com a função (len) = built-in A função len () retorna o número de itens em um objeto.
nome = 'Rodrigo'
i = 0
while i < len(nome):
    print(nome[i])
    i += 1

#2º laço for com a função (enumarate)  = contador automatico
lista = [1,2,3,4,5,6,7,8]
for i, lt in enumerate(lista):
    print(i, lt)  

#3º laço for com a função (range) = A função range() permite-nos especificar o 
# início da sequência, o passo, e o valor final. O único parâmetro obrigatório é 
# o que define quem será o último elemento da sequência.
# range(start=1, stop, setp=1)
#exemplo 1
for i in range(1,10):
    print(i)

#exemplo 2
for i  in range(1,10,2):
    print(i)

#exemplo 2
for i in range(10, 1, -1):
    print(i)