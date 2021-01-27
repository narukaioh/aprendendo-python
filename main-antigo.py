'''
1- Método de etrada de dados
2 - Método de saída de dados
3 - If e else - While
4 - Operadores matemáticos


idade = input('Digite sua idade: ')
print('Você tem ' +idade+ ' anos')

if int(idade) > 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')

cont = 0    
while cont < 10:
    print(cont)
    cont+=1
'''

cadastro = '1'
clientes = []
produtos = []
preco_pedido = []
cont = 0
condicao = 0

while cadastro == '1':
    cliente = input('Nome do cliente: ')
    numero_produto = input('Quantidade do pedido: ')
    clientes.append(cliente)
    produtos.append(numero_produto)
    
    if int(numero_produto) > 999:
        preco_pedido.append(int(numero_produto) * 4.05)
    else:
        preco_pedido.append(int(numero_produto) * 4.50)
    
    cont += 1    
    cadastro = input('Cadastrar novo pedido:\n1 - SIM \n2 - NAO\n')

while condicao < cont:
    icms = preco_pedido[condicao] * 0.18
    ipi = preco_pedido[condicao] * 0.04
    pis = preco_pedido[condicao] * 0.0186
    cofins = preco_pedido[condicao] * 0.0854
    
    print('Cliente: ', clientes[condicao])
    print('Quantidade pedido: ', produtos[condicao])
    print('Valor Pedido: ', preco_pedido[condicao])
    print('--- Tributacao --- \nICMS: '+ str(icms) + '\nIPI: ' + str(ipi) + '\nPIS: ' + str(pis) + '\nCOFINS: ' + str(cofins))
    print('Total Impostos: ', preco_pedido[condicao] * 0.324)
    print('Total Mercadoria: ', preco_pedido[condicao])
    print('Total Geral: ', preco_pedido[condicao] * 1.324)
    condicao += 1

    
