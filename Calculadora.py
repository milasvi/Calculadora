
import emoji



#cabecalho
print(emoji.emojize(':input_numbers::plus:CALCULADORA:plus::input_numbers:'))

#calculadora
n1 =int(input('\nEscreva o primeiro valor:'))
n2 = int(input('Escreva o segundo valor:'))
while True:   
    escolha = input("""\n**ESCOLHA:**
    [1]Somar
    [2]Multiplicar
    [3]Novos números
    [4]Sair
    """)
    print('=-'*15)
    while escolha != '1' and escolha != '2'and escolha != '3' and escolha != '4':
        escolha = input('\033[0;31m Opcão inválida!\033[m')
    if escolha == '4':
        print('Obrigade por usar a CALCULADORA.\nSaindo...')
        break
    elif escolha == '1':
        print(f'Soma : {n1} + {n2} = {n1+n2}')
    elif escolha == '2':
        print(f'Multiplicação: {n1} x {n2} = {n1*n2}')
    else:
        n1 =int(input('Escreva o primeiro valor:'))
        n2 = int(input('Escreva o segundo valor:'))
