from models.funcoes import carregar_dados_googlesheets, inserir_dados_googlesheets, conectar_googlesheets


conectar = conectar_googlesheets()


processos_registrados = carregar_dados_googlesheets(conectar, 'sei_cadastrado')
num_sei = '23106.028752/2023-57'
mat = "1538765"

def verificar_sei_cadastrado(num_sei, mat, dados_planilha):
    lista_processos_sei = []
    for registro in dados_planilha:
        if str(registro["SIAPECAD"]) == str(mat):
            lista_processos_sei.append(str(registro["NUMERO_SEI"]))
    if str(num_sei) in lista_processos_sei:
        return True
    else:
        return False

#ws_dados.values_append(intervalo, params, body)

#dados = ['2256322','23106.116233/2023-45']
#inserir_dados_googlesheets('sei_cadastrado!A2',conectar, ['2256322','23106.116233/2023-45'])
# for chave in dicionario_mat_siape:
#     print(chave,": ",dicionario_mat_siape[chave])

if verificar_sei_cadastrado(num_sei, mat, processos_registrados):
    print('Já está na lista')
else:
    print('Não está na lista')
