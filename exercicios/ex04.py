# digite o seu nome se ele tiver 4 letras ou menor "Seu nome é muito curto" se tiver 5 ou 6 "Seu nome é normal" se for maior que 6 "Seu nome é muito grande"

nome = input('Digite o seu nome:').title()

if nome.istitle() == True:
    if len(nome) > 6:
        print('Seu nome é muito grande')
    elif len(nome) >= 5:
        print('Seu nome é normal')
    else: 
        print('Seu nome é muito curto')   
else:
    print('Não é um nome')