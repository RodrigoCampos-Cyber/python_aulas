s1 = {1,2,3,5,5,5,5,5,}
s2 = {9,6,7,5}

s3 = s1 | s2 # union retorno todos itens sem repetição
s4 = s1 - s2 # diference retorna somente itens da esquerda
s5 = s1 & s2 # intersection retorno somente os itens iguais de uma lista
s6 = s1 ^ s2 # symetric_diference retorno somentos os itens diferente entre lista

print(s3)
print(s4)
print(s5)
print(s6)


t = 'Rodrigo'

s = len(t)

print(s)