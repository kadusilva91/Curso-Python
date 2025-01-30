# Elabora um program que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:

print(10*"=",'LOJAS GUANABARA',10*"=")
valor = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))
if opcao == 1:
    precofinal = valor * 0.9
elif opcao == 2:
    precofinal = valor * 0.95
elif opcao == 3:
    precofinal = valor
    print(f'Sua compra será parcelada em 2x de R${valor/2:.2f}')
elif opcao == 4:
    precofinal = valor * 1.2
    parcela = int(input('Quantas parcelas? '))
    valor_parcela = precofinal / parcela
    print(f'Sua compra será parcelada em {parcela}x de R${valor_parcela:.2f} com juros de 20% ')
else:
    precofinal = 0
    print('OPÇÃO INVÁLIDA, tente novamente')
print(f'Sua compra de R${valor:.2f} vai custar R${precofinal:.2f} no final.')
