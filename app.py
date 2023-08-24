from views.janelas import tela_inicial
from models.funcoes import registrar_elogio, selecionar_servidores, gerar_log, infos_programa


resposta = infos_programa(1)
if resposta == "OK":
    dados_da_tela = tela_inicial()
    servidores_selecionados = selecionar_servidores("listaServidores", dados_da_tela['SERVIDORES'])
    if len(servidores_selecionados["SERV_LOCALIZADOS"]) == 0:
        gerar_log(servidores_selecionados["SERV_LOCALIZADOS"], servidores_selecionados["SERV_NAO_LOCALIZADOS"], dados_da_tela['SEI'])
    else:
        registrar_elogio(dados_da_tela['SEI'], dados_da_tela['ELOGIO'], servidores_selecionados["MATRICULAS"])
        gerar_log(servidores_selecionados["SERV_LOCALIZADOS"], servidores_selecionados["SERV_NAO_LOCALIZADOS"], dados_da_tela['SEI'])
else:
    pass