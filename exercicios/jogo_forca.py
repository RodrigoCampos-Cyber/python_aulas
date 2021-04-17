# verificar letra digitada pelo usuario
def letra(letra, palavra):
    if letra.isnumeric():
        print(f'Ah.., o número {letra } é não é aceito, digite novamente')   
        return False
    elif len(letra) > 1:
        print(f'Ah.. {letra} tem {len(letra)} letras, digite novamente')
        return False
    else:       
        if letra in palavra:             
            return True
        else:
            print(f'Infelizmente essa letra não tem') 
            return False

       


# codigo principal
palavra_secreta = 'RODRIGO'
digitada = []
i = 0
while True:
    digitar_letra = str(input('Digite uma letra: ')).upper()     
    if letra(digitar_letra, palavra_secreta )  is False:
        digitada.pop()      
        continue 
    digitada.append(digitar_letra)
    letra_temp = ''
    for lentra_sec in palavra_secreta:
        if lentra_sec in digitada:
            letra_temp += lentra_sec     
        else:
            letra_temp += '*'         
    if letra_temp == palavra_secreta:
        print("Parabéns você ganhou o jogo")
        break
    else:
        print(f' A palavra está assim {letra_temp}')  

