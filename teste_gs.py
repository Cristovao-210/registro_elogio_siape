from models.funcoes import carregar_dados_googlesheets

processos_registrados = carregar_dados_googlesheets('sei_cadastrado')

dicionario_processos_sei = {}
num_sei = '23106.25262728/2023-40'
mat = "2430927"
for registro in processos_registrados:
    #print(f'{registro["NOME"]}: {registro["SIAPECAD"]}')
    dicionario_processos_sei[registro["NUMERO_SEI"]] = registro["SIAPECAD"]
if str(dicionario_processos_sei.get(num_sei)) == str(mat):
    print('Já está na lista')
else:
    print('Não está na lista')


# for chave in dicionario_mat_siape:
#     print(chave,": ",dicionario_mat_siape[chave])

