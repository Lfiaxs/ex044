produto = float(input('Qual o valor do produto? R$'))
print('O valor do produto é {}.'.format(produto))
print('Vamos verificar a condição do pagamento!')
print ('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = produto - (produto * 10 / 100)
elif opção == 2:
    total = produto - (produto*5/100)
elif opção == 3:
   total = produto
   parcela = total / 2
   print ('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif opção == 4:
    total = produto + (produto * 20 / 100 )
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totparc,parcela))
else:
    total = produto
    print('Opção inválida de pagamento. Tente Novamente.')
print('Sua compra de R${:.2f} vai custar no final R${}.'.format(produto, total))
print('Tenha um bom dia!')



