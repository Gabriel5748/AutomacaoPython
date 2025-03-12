import os
import pandas as pd
import functions as func


def inserirArquivo():
    file_path = input("Informe o caminho do arquivo excel: ")
    print("Caminho informado = {} ".format(file_path))
    return file_path

def tratarArquivo(arquivo):
    arquivo = arquivo.replace('"','')
    return arquivo

def verificarArquivo(arquivo):
    while not os.path.isfile(arquivo):
        print("Arquivo não existe")
        arquivo = input("Informe o caminho do arquivo excel: ")

    try:
        lista = pd.read_excel(arquivo, names=['Livros'])
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        exit()

    return lista


# file_path = input("Informe o caminho do arquivo excel: ")
# print("Caminho informado = {} ".format(file_path))

# file_path = file_path.replace('"','')

# while not os.path.isfile(file_path):
#     print("Arquivo não existe")
#     file_path = input("Informe o caminho do arquivo excel: ")

# try:
#     lista = pd.read_excel(file_path, names=['Livros'])
# except Exception as e:
#     print(f"Erro ao ler o arquivo: {e}")
#     exit()


# for index, row in lista.iterrows():
#     print(row["Livros"])
    



