nome_produto = 'Camiseta'
preco_original = 50.00
porcentagem_desconto = 20

#valor do desconto
valor_desconto = preco_original * (20/100)

#valor final com desconto
valor_final = preco_original - valor_desconto

print(f'Produto: {nome_produto}')
print(f'Preço Original: R${preco_original:.2f}')
print(f'Desconto de: {porcentagem_desconto}%')
print(f'Valor do desconto: R${valor_desconto:.2f}')
print(f'Valor final: R${valor_final:.2f}')
