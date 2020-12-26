# -*- coding: utf-8 -*-
meu_dicionario={"A":"ameixa","B":"bola", "C": "carro"}

for i in meu_dicionario:
    print(meu_dicionario[i])

arquivo = open("arquivo.txt")
print(arquivo)
linhas = arquivo.read()
print(linhas)
arquivo2 = open("arquivo2.txt","w")
arquivo2.write("Esse é o meu arquivo")
arquivo2.close