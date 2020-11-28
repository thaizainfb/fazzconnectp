# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:50:48 2020

@author: walla
"""

import csv
import sys
from pathlib import Path


def buscaSkuOrdem():
    listaskus = []

    # Faz a leitura dos arquivos da amazon e preenche lista 
    fileName = argList[2] + '.txt' 
    path = Path("c:/FazzConnect") / argList[1] / "amazon" / fileName
    
    with open(path, newline='') as csvfile:        
        reader = csv.DictReader(csvfile, delimiter = '\t')          
        for row in reader:
            tupla = (row['sku'] , row['product-name'])
            listaskus.append(tupla)
    
    return listaskus


def buscakuCadastrados():
    skucadastrado = []
    
    with open("c:/FazzConnect/sku-shortname.properties", 'r') as sku_file:
        sku_file.__next__()
        
        for row in sku_file:
            chave,valor = row.split('=')
            skucadastrado.append(chave.strip())   
            
    return skucadastrado
    

# Verifica se o sku ja existe e adiciona em uma lista os novos
def verificasku(skuCadastrados, skuOrdens):
    
    newSku = []             
    for tupla in skuOrdens:
        sku = tupla[0]
        if sku not in skuCadastrados:
            newSku.append(tupla)
        
    return(newSku)

# Adiciona um novo sku no aquivo de propriedades    
def addsku(newSku):       
    
    with open("c:/FazzConnect/sku-shortname.properties", 'a', newline='') as file:   
        
        newName = ""       
        for sku in newSku:     
            newName = input(sku[1] + ": ")                                 
            file.write("\n" + sku[0] + "\t = \t" + newName)
        
        file.close()
     
        
argList = sys.argv  
#argList = ["0","20201124","CA"] 


#Buscar sku das novas ordens
skuOrdens = buscaSkuOrdem()


#buscar sku ja cadastrados
skucadastrados = buscakuCadastrados()


#verificar se sku novos ja estao cadastrados
novosSku = verificasku(skucadastrados, skuOrdens)

# Cadastra sku e Adiciona o nome curto para o produto atraves do sku
addsku(sorted(set(novosSku)))





