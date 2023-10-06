from views.janelas import tela_inicial
from models.funcoes import registrar_elogio, selecionar_servidores, gerar_log, infos_programa, carregar_dados_googlesheets, conectar_googlesheets


resposta = infos_programa(1)

if resposta == "OK":
    try:
        conectar_gs = conectar_googlesheets()
        dados_googlesheets_servidores = carregar_dados_googlesheets(conectar_gs,'servidores')
        dados_googlesheets_SEI = carregar_dados_googlesheets(conectar_gs, 'sei_cadastrado')
        dados_da_tela = tela_inicial()
        servidores_selecionados = selecionar_servidores(dados_googlesheets_servidores, dados_da_tela['SERVIDORES']) # "listaServidores", 
        if len(servidores_selecionados["SERV_LOCALIZADOS"]) == 0:
            gerar_log(servidores_selecionados["SERV_LOCALIZADOS"], servidores_selecionados["SERV_NAO_LOCALIZADOS"], dados_da_tela['SEI'])
        else:
            registrar_elogio(conectar_gs, dados_googlesheets_SEI, dados_da_tela['SEI'], dados_da_tela['ELOGIO'], servidores_selecionados["MATRICULAS"])
            gerar_log(servidores_selecionados["SERV_LOCALIZADOS"], servidores_selecionados["SERV_NAO_LOCALIZADOS"], dados_da_tela['SEI'])
    except:
        # gravar servidores que não estão na lista

        # gravar servidores registrados até o momento OU os não lançados

        # criar um BD com duas tabelas: uma com nome e matricula do servidor e outra com os números do SEI que ele já tem registrado
        # Caso já tenha sido registrado aquele SEI, retirar o nome dele da lista
         
        # Cancelado pelo usuário
        infos_programa(6) 
