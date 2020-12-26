#first exercise
a = input("Insira Nome: ")
b = input("Insira Nome: ")
if a == b:
    print("Sequências Iguais")
else:
    print("Sequências Diferentes")

#second exercise
nome = input("Insira o nome do Arquivo: ")
a = open(nome)
linhas = a.readlines()
for i in linhas:
    print(i)

#third exercise
menu = 0
def abrirArquivo():
    c = input("Insira o arquivo que desejar ")
    d = open(c)
    return d

def lerArquivo():
    linhas =  d.readlines()
    for linha in linhas:
        print(linha.strip) #if the article has one special character


while menu !=3:
    print("Digite 1 para ler o arquivo")
    print("Digite 2 para ler arquivo aberto")
    print("Digite 3 para sair")
    menu = input("Digite a opção desejada ")
    if menu == 1:
        d = abrirArquivo()
    elif menu == 2:
        d = lerArquivo()