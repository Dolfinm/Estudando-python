#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular
listagem = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}') #centraliza a partir de tal numero de caracteres
print('-' * 40)
for c in range (0, len(listagem), 2): #len() vai classificar o numero dos itens da tupla
    print(f'{listagem[c]:.<30} R${listagem[c+1]:>7.2f}')  # :.40 aninha até ter 40 caracteres adicionando-os e :>7 os direciona com distancia de 7 caracteres para a direita 
print('-' * 40)