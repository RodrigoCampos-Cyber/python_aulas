# identificar se o numero é par ou impar

def verifica_numero(numero):
    return numero.isnumeric()


numero = input('Digite um número: ')


if verifica_numero(numero) == True:
    if (int(numero)%2) >= 1:
        print("ímpar")
    else:  
        print("par")
else:
    print("Não é numero")


