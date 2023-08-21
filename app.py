from views.janelas import tela_inicial
from models.funcoes import registrar_elogio


dados_da_tela = tela_inicial()
sei = dados_da_tela['SEI']
lista_nome_servidores = dados_da_tela['SERVIDORES']
elogio = dados_da_tela['ELOGIO']

print(f'\n\nNÚMERO DO SEI: {sei}\n\nLISTA DE SERVIDORES: {lista_nome_servidores}\n\nTEXTO DO ELOGIO: {elogio}')