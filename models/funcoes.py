import pandas as pd
import pyautogui
import time

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



def selecionar_servidores(dados_servidores, servidores_elogio): # arquivo listaServidores

  servidores = pd.read_csv(f'{dados_servidores}.csv', sep=",", encoding='latin-1')

  dicionario_mat_siape = {}
  lista_mat_siape = []
  log_servidores_nao_cadastrados = []
  log_servidores_cadastrados = []

  for nome_serv, mat_siape in zip(list(servidores['NOME']), list(servidores['SIAPE'])):
      dicionario_mat_siape[nome_serv] = mat_siape

  for nome in servidores_elogio:
    nome_servidor = str(tratar_elementos_ligacao_txt(str(nome).strip())).upper()
    if nome_servidor in list(servidores['NOME']):
        lista_mat_siape.append(dicionario_mat_siape.get(nome_servidor))
        log_servidores_cadastrados.append(f'{nome_servidor} - {dicionario_mat_siape.get(nome_servidor)}')
    else:
        log_servidores_nao_cadastrados.append(f'{nome_servidor}')
  
  return [lista_mat_siape, log_servidores_nao_cadastrados, log_servidores_cadastrados] # retorna uma lista com 3 listas dentro



def gerar_log(serv_cadastrados, serv_nao_cadastrados):
  # log dos nomes que foram localizados na base de dados
  with open('servidores_cadastrados.txt', 'a', encoding='utf-8') as na_lista:
    na_lista.write(f'NOME DOS SERVIDORES QUE TIVERAM O ELOGIO REGISTRADO: \n\n')
    for serv_cad in serv_cadastrados:
      na_lista.write(f'{serv_cad}')

  # log dos nomes que NÃO foram localizados na base de dados
  with open('servidores_nao_cadastrados.txt', 'a', encoding='utf-8') as nao_lista:
     nao_lista.write(f'O ELOGIO NAO FOI REGISTRADO PARA: \n\n')
     for serv_nao_cad in serv_nao_cadastrados:
      nao_lista.write(f'{serv_nao_cad}\n')




def registrar_elogio(num_sei, texto_elogio, matriculas_servidores):
  # ENTRADA DE DADOS PARA:
    # MATRÍCULA
    # NÚMERO DO SEI
    # TEXTO DO ELEOGIO

  #matricula = "01932081" 
  processo_sei = f"PROCESSO SEI Nº {num_sei}"
  sleep = 1

  elogio = texto_elogio

  # descobrindo a quantidade de linhas para saber quantas vezes repetir
  iteracoes = int(len(elogio) / 60)
  # cada linha tem 60 caracteres
  tam_linha = 60
  # preenchendo o primeiro elemento com o ínicio do texto
  lista_texto = [elogio[0:60].lower()]

  # preenchendo a lista com as linhas do texto
  for i in range(iteracoes):
    # removendo as partes do texto que já estão na lista
    texto = str(elogio.replace(elogio[0:tam_linha], "")).lower()
    tam_linha += 60
    lista_texto.append(texto[0:60])

  pyautogui.PAUSE = 0.3

  # posicionando o mouse dentro do hod
  pyautogui.click(x=445, y=351)

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
    pyautogui.write(matricula)
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
    #pyautogui.click(x=384, y=381)
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
    # pyautogui.press("F3")
    # time.sleep(sleep)
    # pyautogui.write("S")
    # time.sleep(sleep)
    # pyautogui.press("enter")


