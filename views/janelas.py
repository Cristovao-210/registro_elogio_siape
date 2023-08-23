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