import PySimpleGUI as sg
import pyautogui

def tela_inicial():
    layout = [
        [sg.Text("Informe o número do processo SEI")],
        [sg.InputText(key="num_sei", size=(80, 25))],
        [sg.Text("", key="texto_erro_SEI", text_color="red")],
        [sg.Text("Informe os nomes dos servidores (um nome por linha)"),sg.Text(" "*63), sg.Text("Informe o texto do elogio a ser registrado")],
        [sg.Multiline(key="servidores", size=(80, 25)), sg.Multiline(key="txt_elogio", size=(80, 25))],
        [sg.Text("", key="texto_erro_servidores", text_color="brown"),sg.Text(" "*140), sg.Text("", key="texto_erro_txt_elogio", text_color="brown")],
        [sg.Text("", key="texto_INFO_usuario", text_color="yellow")],
        [sg.Text(" "*120), sg.Button("INICIAR REGISTRO"), sg.Button("CANCELAR")]
        #[sg.Text(" "*63)]
    ]

    janela = sg.Window("REGISTRO DE ELOGIO NO SIAPE", layout)

    

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "CANCELAR":
            break
        if evento == "INICIAR REGISTRO":
            processo_sei = valores["num_sei"]
            if processo_sei == "":
                janela["texto_erro_SEI"].update(f"NECESSÁRIO INFORMAR O NÚMERO DO PROCESSO SEI")
                continue
            else:
                janela["texto_erro_SEI"].update("")

            servidores_elogio = valores["servidores"]
            if servidores_elogio == "":
                janela["texto_erro_servidores"].update(f"NECESSÁRIO INFORMAR O NOME DE PELO MENOS UM SERVIDOR")
                continue
            else:
                janela["texto_erro_servidores"].update("")    
            lista_de_servidores = str(servidores_elogio).split("\n")

            texto_elogio = valores["txt_elogio"]
            if texto_elogio == "":
                janela["texto_erro_txt_elogio"].update(f"NECESSÁRIO INFORMAR O TEXTO A SER REGISTRADO")
                continue
            else:
                janela["texto_erro_txt_elogio"].update("")
                janela["texto_INFO_usuario"].update("AGUARDE A MENSAGEM INFORMANDO O TÉRMINO DO REGISTRO")

                janela["num_sei"].update("")
                janela["servidores"].update("")
                janela["txt_elogio"].update("")
                break
        
            
    janela.close()
    
    return {"SEI": processo_sei, "SERVIDORES": lista_de_servidores, "ELOGIO": texto_elogio}


# mensagens a serem utilizadas no programa
def infos_programa(tema_info):
  '''
  1 - Informações sobre o programa
  2 - Nenhum servidor localizado na base de dados
  3 - Alguns servidores não localizados na base de dados
  4 - Base de dados não localizada
  5 - TODOS OS SERVIDORES CADASTRADOS COM SUCESSO!
  '''
  match tema_info:
    case 1:
      msg_info = '''                 ######   INFORMAÇÕES IMPORTANTES   ######

      1 - Antes de iniciar o programa é necessário que a tela do Hod (SIAPE TELA PRETA) esteja ATIVA, MAXIMIZADA e em PRIMEIRO PLANO em qualquer uma das telas do computador.

      2- Também é necessário que NÃO esteja mais na página de abertura. Para isso, após a abertura da TELA PRETA, tecle F12.

      3 - Durante a execução do programa não será possível usar o mouse e o teclado do computador.

      4 - Quando o registro terminar será informado se algum servidor não foi cadastrado.

      5 - Caso seja necessário interromper a execução do programa, posicione o cursor do mouse no canto superior esquerdo da sua tela principal.
      Costuma ser logo acima do ícone da lixeira na área de trabalho.
      
      ATENÇÃO!! Caso os itens 1 e 2 ainda não tenham sido executados, clique em CANCELAR, faça o solicitado e execute o programa novamente.
      '''
    case 2:
      msg_info = '''                 ######   ATENÇÃO   ######

      Nenhum dos servidores listados foi localizado na base de dados.
      Será gerado um relatório com o nome desses servidores na pasta onde se encontra o executável deste programa.

      '''
    case 3:
      msg_info = '''                 ######   ATENÇÃO   ######

      Alguns dos servidores listados não foram localizados na base de dados.
      Será gerado um relatório com o nome desses servidores na pasta onde se encontra o executável deste programa.
      '''
    case 4:
      msg_info = '''                 ######   ATENÇÃO   ######

      O arquivo listaServidores.csv não foi localizado.
      Este arquivo precisa estar na pasta onde se encontra o executável deste programa.

      '''
    case 5:
      msg_info = '''                 ######   ATENÇÃO   ######

      O ELOGIO FOI CADASTRADO PARA TODOS OS SERVIDORES!
      Será gerado um relatório com o nome desses servidores na pasta onde se encontra o executável deste programa.

      '''

  return pyautogui.confirm(msg_info)
