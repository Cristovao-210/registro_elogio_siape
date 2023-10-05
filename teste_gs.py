from models.funcoes import carregar_dados_googlesheets

servidores = carregar_dados_googlesheets('sei_cadastrado')
lista = []

dicionario_mat_siape = {}
for registro in servidores:
    #print(f'{registro["NOME"]}: {registro["SIAPECAD"]}')
    dicionario_mat_siape[registro["SIAPECAD"]] = registro["NUMERO_SEI"]
    lista.append(registro["SIAPECAD"])


for chave in dicionario_mat_siape:
    print(chave,": ",dicionario_mat_siape[chave])

#print(len(set(servidores)))
# conjunto = set(lista)
# print(len(conjunto))
# print(len(lista))
# lista.sort()
# for i, item in enumerate(lista):
#     if item == 'ANDREA PEDROSA RIBEIRO ALVES OLIVEIRA':
#         print(item)