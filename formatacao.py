# :s texto
# :d inteiro
# :f float
# :. numeros - ex {:.2}
# : -  caracteres > < ^ - ex {:0>10}

num = 10
nome = 'Rodrigo'


# utilizando format
print("{}".format(nome))
print("{n}".format(n=nome))
print("{:s}".format(nome))
print('{:.2f}'.format(num))
print('{:.2f}'.format(num))
print('{:0<10}'.format(num))
print('{:0>10}'.format(num))
print('{:0^10}'.format(num))

# utilizando f 
print(f'{num:.2f}')
print(f'{num:0<10}')
print(f'{num:0^10}')
