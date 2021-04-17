# insira a hora é informa se é (Bom dia, Boa Tarde, Boa Noite)

hora = input('Digite a hora: ')

if hora[:2].isnumeric() == True:
    if int(hora[:2]) <= 11:
        print("Bom dia")
    elif int(hora[:2]) <= 18 :
        print("Boa tarde")
    else:
        print("Boa noite")
else:
    print('Não é um número')


