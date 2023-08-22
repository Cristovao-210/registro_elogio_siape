from views.janelas import tela_inicial
from models.funcoes import registrar_elogio, selecionar_servidores, gerar_log


dados_da_tela = tela_inicial()
sei = dados_da_tela['SEI']
lista_nome_servidores = dados_da_tela['SERVIDORES']
elogio = dados_da_tela['ELOGIO']

# print(f'\n\nNÚMERO DO SEI: {sei}\n\nLISTA DE SERVIDORES: {lista_nome_servidores}\n\nTEXTO DO ELOGIO: {elogio}')

servidores_selecionados = selecionar_servidores("listaServidores", lista_nome_servidores)
#gerar_log(servidores_selecionados[2], servidores_selecionados[1])

# print(f'''
# SERVIDORES SELECIONADOS:\n\n {servidores_selecionados[0]}\n\n
# SERVIDORES NÃO ENCONTRADOS:\n\n {servidores_selecionados[1]}\n\n
# SERVIDORES ENCONTRADOS:\n\n {servidores_selecionados[2]}''')

#registrar_elogio(sei, elogio, servidores_selecionados[0])