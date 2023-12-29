from views.janelas import tela_inicial
from models.funcoes import registrar_elogio, selecionar_servidores, gerar_log, infos_programa, carregar_dados_googlesheets, conectar_googlesheets, configura_sigla_terminal_siape


resposta = infos_programa(1)

if resposta == "OK":
    try:
        conectar_gs = conectar_googlesheets()
        dados_googlesheets_servidores = carregar_dados_googlesheets(conectar_gs,'servidores')
        dados_googlesheets_SEI = carregar_dados_googlesheets(conectar_gs, 'sei_cadastrado')
        sigla_tela_preta = configura_sigla_terminal_siape()
        dados_da_tela = tela_inicial()
        servidores_selecionados = selecionar_servidores(dados_googlesheets_servidores, dados_da_tela['SERVIDORES']) # "listaServidores", 
        if len(servidores_selecionados["SERV_LOCALIZADOS"]) == 0:
            gerar_log(servidores_selecionados["SERV_LOCALIZADOS"], servidores_selecionados["SERV_NAO_LOCALIZADOS"], dados_da_tela['SEI'])
        else:
            registrar_elogio(conectar_gs, sigla_tela_preta, dados_googlesheets_SEI, 
                             dados_da_tela['SEI'],
                             dados_da_tela['ELOGIO'], 
                             servidores_selecionados["MATRICULAS"],
                             servidores_selecionados['LOG_SERV_CADASTRADO'])
            gerar_log(servidores_selecionados["SERV_LOCALIZADOS"], servidores_selecionados["SERV_NAO_LOCALIZADOS"], dados_da_tela['SEI'])
    except:      
        # Cancelado pelo usuário
        infos_programa(6) 
