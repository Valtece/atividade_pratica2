valor_real = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

#Conversão Real para DOLAR
convertido_dolar = valor_real / taxa_dolar

#Conversão Real para EURO
convertido_euro = valor_real / taxa_euro

print(f'Sabendo que a taxa do DOLAR é ${taxa_dolar:.2f} e do EURO é €{taxa_euro:.2f}, o valor de R${valor_real:.2f} convertido para DOLAR equivale a ${convertido_dolar:.2f} e convertido para EURO €{convertido_euro:.2f}.')