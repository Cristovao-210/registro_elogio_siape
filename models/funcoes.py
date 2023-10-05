import pandas as pd
import pyautogui, pygetwindow
import time
from views.janelas import infos_programa
import gspread
import tomllib # para acessar o arquivo de configuraação

# carregar dados dos servidores da base de dados do google docs
def carregar_dados_googlesheets(pagina):
    # acessando o arquivo de configuração
    with open("models\conecta_gs\pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    # CÓDIGO DA PLANILHA
    CODE = data['CODE']['ID'] 

    # ACESSO A PLANILHA
    gc = gspread.service_account(filename='models/conecta_gs/listaservidores.json')

    # ABRIR A PLANILHA
    sh = gc.open_by_key(CODE)

    # ACESSANDO A 'ABA' DESEJADA POR TÍTULO
    ws_dados = sh.worksheet(pagina)
    return ws_dados.get_all_records()

# tratando preposições e conectivos em geral que aparecem o a inicial maiúscula
def tratar_elementos_ligacao_txt(txt):

    for ch in txt:
      match ch:
        case 'à':
          txt = txt.replace(ch, 'a')
        case 'á':
          txt = txt.replace(ch, 'a')
        case 'ã':
          txt = txt.replace(ch, 'a')
        case 'â':
          txt = txt.replace(ch, 'a')
        case 'é':
          txt = txt.replace(ch, 'e')
        case 'ê':
          txt = txt.replace(ch, 'e')
        case 'í':
          txt = txt.replace(ch, 'i')
        case 'ó':
          txt = txt.replace(ch, 'o')
        case 'ô':
          txt = txt.replace(ch, 'o')
        case 'õ':
          txt = txt.replace(ch, 'o')
        case 'ú':
          txt = txt.replace(ch, 'u')
        case 'ü':
          txt = txt.replace(ch, 'u')
        case 'ç':
          txt = txt.replace(ch, 'c')

        # no caso das letras serem maiúsculas
        case 'À':
          txt = txt.replace(ch, 'A')
        case 'Á':
          txt = txt.replace(ch, 'A')
        case 'Ã':
          txt = txt.replace(ch, 'A')
        case 'Â':
          txt = txt.replace(ch, 'A')
        case 'É':
          txt = txt.replace(ch, 'E')
        case 'Ê':
          txt = txt.replace(ch, 'E')
        case 'Í':
          txt = txt.replace(ch, 'I')
        case 'Ó':
          txt = txt.replace(ch, 'O')
        case 'Ô':
          txt = txt.replace(ch, 'O')
        case 'Õ':
          txt = txt.replace(ch, 'O')
        case 'Ú':
          txt = txt.replace(ch, 'U')
        case 'Ü':
          txt = txt.replace(ch, 'U')
        case 'Ç':
          txt = txt.replace(ch, 'C')

    return txt


# pegando a matrícula dos servidores para registrar o elogio
def selecionar_servidores(servidores_elogio): # dados_servidores, 

  try:
    # carregando dados
    servidores = carregar_dados_googlesheets('servidores') #pd.read_csv(f'{dados_servidores}.csv', sep=",", encoding='latin-1')
  except:
    # base de dados não encontrada (listaServidores.csv)
    infos_programa(4)

  dicionario_mat_siape = {}
  lista_mat_siape = []
  log_servidores_nao_cadastrados = []
  log_servidores_cadastrados = []
  lista_gspread = []

  for registro in servidores: #zip(list(servidores['NOME']), list(servidores['SIAPECAD'])):
      dicionario_mat_siape[registro["NOME"]] = registro["SIAPECAD"]
      lista_gspread.append(registro['NOME'])
      # É preciso pensar em um jeito de separar por cargo.
      # Alguns servidores tem mais de uma matrícula, tem mais de um vínculo  

  for nome in servidores_elogio:
    nome_servidor = str(tratar_elementos_ligacao_txt(str(nome).strip())).upper()
    if nome_servidor in lista_gspread: #list(servidores['NOME']):
        lista_mat_siape.append(dicionario_mat_siape.get(nome_servidor))
        log_servidores_cadastrados.append(f'{nome_servidor} - {dicionario_mat_siape.get(nome_servidor)}')
    else:
        log_servidores_nao_cadastrados.append(f'{nome_servidor}')

  return {"MATRICULAS": lista_mat_siape,
          "SERV_NAO_LOCALIZADOS": log_servidores_nao_cadastrados,
          "SERV_LOCALIZADOS": log_servidores_cadastrados} # retorna um dicionário com 3 listas dentro



def gerar_log(serv_cadastrados, serv_nao_cadastrados, processo_sei):
  # log dos nomes que foram localizados na base de dados
  processo_sei = str(processo_sei).replace("/","").replace("-","").replace(".","")
  if len(serv_cadastrados) > 0:
    with open(f'servidores_cadastrados_{processo_sei}.txt', 'a', encoding='utf-8') as na_lista:
      na_lista.write(f'NOME DOS SERVIDORES QUE TIVERAM O ELOGIO REGISTRADO: \n\n')
      for serv_cad in serv_cadastrados:
        na_lista.write(f'{serv_cad}\n')
  # log dos nomes que NÃO foram localizados na base de dados
  if len(serv_nao_cadastrados) > 0:
    with open(f'servidores_nao_cadastrados_{processo_sei}.txt', 'a', encoding='utf-8') as nao_lista:
      nao_lista.write(f'O ELOGIO NAO FOI REGISTRADO PARA: \n\n')
      for serv_nao_cad in serv_nao_cadastrados:
        nao_lista.write(f'{serv_nao_cad}\n')
  # Avisando sobre o relatório com o nome dos servidores NÃO CADASTRADOS
  if len(serv_cadastrados) > 0 and len(serv_nao_cadastrados) > 0:
    infos_programa(3)
  elif len(serv_cadastrados) > 0 and len(serv_nao_cadastrados) == 0:
    infos_programa(5)
  elif len(serv_cadastrados) == 0 and len(serv_nao_cadastrados) > 0:
    infos_programa(2)


def registrar_elogio(num_sei, texto_elogio, matriculas_servidores):

  processo_sei = f"PROCESSO SEI Nº {num_sei}"
  sleep = 1
  elogio = texto_elogio
  # descobrindo a quantidade de linhas para saber quantas vezes repetir
  iteracoes = int(len(elogio) / 60)
  # cada linha tem 60 caracteres
  tam_linha = 60
  # preenchendo o primeiro elemento com o ínicio do texto
  lista_texto = [str(elogio[0:60]).upper()]
  # preenchendo a lista com as linhas do texto
  for i in range(iteracoes):
    # removendo as partes do texto que já estão na lista
    texto = str(elogio.replace(elogio[0:tam_linha], "")).upper()
    tam_linha += 60
    lista_texto.append(texto[0:60])
  # intervalo entre os comandos
  pyautogui.PAUSE = 3
  # posicionando o mouse dentro do hod
  janela = pygetwindow.getWindowsWithTitle(title='Terminal 3270 - A - AWVADS8R')[0]
  janela.activate()
  # Diminuindo o intervalo entre os comandos
  pyautogui.PAUSE = 0.3
  # posicionando o cursor na barra de comandos
  pyautogui.press("F2")
  time.sleep(sleep)
  # digitando o comando para acessar a função desejada
  pyautogui.write(">CAINELOGIO")
  time.sleep(sleep)
  pyautogui.press("enter")
  time.sleep(sleep)
  # inserindo a matricula do servidor
  for matricula in matriculas_servidores:
    time.sleep(sleep)
    pyautogui.write(str(matricula))
    time.sleep(sleep)
    pyautogui.press("enter")
    time.sleep(sleep)
    # dando tab até chegar na posição de digitar o número do SEI
    for repete in range(8):
        pyautogui.press("tab")
    # inserindo o número do SEI para chegar a descrição
    pyautogui.write(processo_sei)
    pyautogui.press("enter")
    time.sleep(sleep)
    # inserindo a descrição 
    pyautogui.press("enter")
    time.sleep(sleep)
    count_rows = 0
    for lt in lista_texto:
      pyautogui.write(tratar_elementos_ligacao_txt(lt.replace("\n", "")))
      count_rows += 1
      time.sleep(0.5)
      if (count_rows % 10 == 0):
        time.sleep(sleep)
        pyautogui.press("F8")
        time.sleep(sleep)
    # salvando
    pyautogui.press("F3")
    time.sleep(sleep)
    pyautogui.write("S")
    time.sleep(sleep)
    pyautogui.press("enter")
  pyautogui.press('F3')

