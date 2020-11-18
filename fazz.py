# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:50:48 2020

@author: walla
"""

import csv


# Faz a leitura dos arquivos da amazon
def sortfile():
    
    listaskus = []
    listaprodutos = []
    
    with open("ca_orders.txt", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = '\t')          
        reader_sorted = sorted(reader, key=lambda i: (i['product-name'],i['quantity-purchased']))    
        for row in reader_sorted:
            #print(row['sku'] )
            listaskus.append(row['sku'])
            listaprodutos.append(row['product-name'])
             
    return reader_sorted , listaskus



# Verifica se o sku ja existe e adiciona em uma lista os novos
def verificasku(listasku):
    skucadastrado = []
    newsku = []
    
    with open('sku-names.txt', 'r') as sku_file:
        sku_file.__next__()
        
        for row in sku_file:
            chave,valor = row.split('=')
            skucadastrado.append(chave.strip())
                  
    for sku in listasku:
        if sku not in skucadastrado:
            newsku.append(sku)
        
    return(newsku)

# Adiciona um novo sku no aquivo de propriedades    
def addsku(newsku, dic):       
    with open('sku-names.txt', 'a', newline='') as file:
        
        newname = ""       
        for sku in newsku:  
            productname = searchNameProduct(dic,sku)
            newname = input(productname + ": ")                                 
            file.write("\n" + sku + "\t = \t" + newname)
        
        file.close()


def searchNameProduct(dic,sku):
    for row in dic:
        if row["sku"] == sku :
            return row["product-name"]
    

def changename(sku, productname):   
    with open('sku-names.txt', newline='') as skufile:
    #dicionario[chave] = novo valor        
        skufile.close()
        
        
        
# Ordena arquivo da Amazon
arquivoOrdenado, listasku = sortfile()
# Cria uma copia do arquivo da amazon ordenado

# Verifica se existem novos sku
novossku = verificasku(listasku)
# Adiciona o nome curto para o produto atraves do sku
addsku(sorted(set(novossku)), arquivoOrdenado)



print("well done!")




