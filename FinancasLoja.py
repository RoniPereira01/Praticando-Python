#input
email= input("Escreva seu email:")
nome = input("Escreva seu nome")

print(email, nome)

#listas

vendas = [10, 20, 30, 155, 14564, 5640]

quantidade_vendas = sum(vendas)
print(quantidade_vendas)

print(max(vendas))
print(min(vendas))

listaProduto = ["iphone" , "airpod", "ipad", "macbook"]
produtoProcurado = input("Pesquise pelo nome do produto:")
produtoProcurado =produtoProcurado.lower()

print(produtoProcurado in listaProduto)

#adicionar um item
listaProduto.append("apple wath")
print(listaProduto)

#remover um item
listaProduto.remove("apple wath")
print(listaProduto)

listaProduto.pop(0)
print(listaProduto)
#editar um item
preco = [6000, 1500, 3500]
preco[0]= preco[0] * 1.5
print(preco)

#contar quantas vezes um item
listaProduto = ["iphone" , "airpod", "ipad", "macbook"]
print(listaProduto.count("apple watch"))

#ordenar uma lista
listaProduto.sort(reverse= True)
print(listaProduto)