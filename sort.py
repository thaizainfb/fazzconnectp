# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:11:33 2020

@author: walla
"""


import csv
import sys
from pathlib import Path

# Faz a leitura dos arquivos da amazon
def sortfile(argList):

    fileName = argList[2] + '.txt' 
    path = Path("c:/FazzConnect") / argList[1] / "amazon" / fileName
	
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = '\t')          
        reader_sorted = sorted(reader, key=lambda i: (i['product-name'],i['quantity-purchased']))    
            
    return reader_sorted


def writefile(dic, argList):

    newFileName = argList[2] + '.txt' 
    path = Path("c:/FazzConnect") / argList[1] / "amazon" / newFileName
    
    with open(path, "w") as csvfile:
        
        titulo = dic[0]
        chave = ""
        for key, valor in titulo.items():
            chave += (key + "\t")
        csvfile.writelines(chave + "\n")
        
        for row in dic:
            linha = ""
            for key, valor in row.items():
                linha += (str(valor) + "\t")       
            
            csvfile.writelines(linha + "\n")
            
    csvfile.close()


argList = sys.argv
#argList = ["0","20201124","CA"]

# Ordena arquivo da Amazon
arquivoOrdenado = sortfile(argList)

# Cria uma copia do arquivo da amazon ordenado
writefile(arquivoOrdenado, argList)


print("Sorted File!")