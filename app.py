from views.janelas import tela_inicial
from models.funcoes import registrar_elogio, selecionar_servidores, gerar_log, info_sobre_programa



resposta = info_sobre_programa()
if resposta == "OK":
    dados_da_tela = tela_inicial()
    sei = dados_da_tela['SEI']
    lista_nome_servidores = dados_da_tela['SERVIDORES']
    elogio = dados_da_tela['ELOGIO']

### ***** SE NENHUM SERVIDOR FOR ENCONTRADO AVISAR E FINALIZAR O PROGRAMA

### ***** SE NÃO LOCALIZAR A LISTA DE SERVIDORES INFORMAR QUE ELA DEVE ESTAR NA MESMA PASTA DO .EXE DO PROGRAMA

### ***** MOSTRAR NO TÉRMINO DA EXECUÇÃO OS SERVIDORES QUE NÃO FORAM ENCONTRADOS - USAR MSG DO PYAUTOGUI
# E INFORMAR QUE O ARQUIVO DE LOG ESTARÁ NA MESMA PASTA ONDE SE ENCONTRA O PROGRAMA COM O NOME XXXX

    servidores_selecionados = selecionar_servidores("listaServidores", lista_nome_servidores)
    #gerar_log(servidores_selecionados[2], servidores_selecionados[1])
    registrar_elogio(sei, elogio, servidores_selecionados[0])
else:
    pass