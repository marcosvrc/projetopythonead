'''
Created on 22 de abr de 2019

@author: marcos.camara
'''
import os
import pickle
import random

base = {}

#Valida se o candidato foi cadastrado pelo numero e pela regiao.
def verificar_cand_informado(cod, regiao):
    cand_cadastrado = False
    try:
        arquivo = open(obter_nome_arquivo(), "rb")
        list_cand = pickle.load(arquivo)
        desc_regiao = obter_descricao_regiao(regiao)
        for key in sorted(list_cand.keys()):
            if(list_cand[key]["codigo"] == cod and list_cand[key]["regiao"] == desc_regiao):
                cand_cadastrado = True
                break
    except Exception as ex:
        print(ex)
    finally:
        arquivo.close()
            
    return cand_cadastrado             

def cadastrar_candidato():
    
    candidato = {}
    
    codigo = raw_input("Digite o codigo do candidato\n")
    
    candidato["codigo"] = codigo
    candidato["nome"] = raw_input("Digite o nome do candidato\n")
    candidato["cargo"] = raw_input("Digite o cargo do candidato\n")
    candidato["num_votos"] = raw_input("Digite o numero de votos\n")
    regiao = int(raw_input("Regiao:\n"
                           "[1] Norte\n"
                           "[2] Nordeste\n"
                           "[3] Centro-Oeste\n"
                           "[4] Sul\n"
                           "[5] Sudeste\n"
                           "Digite o codigo da regiao: "))
    
    candidato["regiao"] = regiao
    
    if (verificar_cand_informado(codigo, regiao)):
        print("Ja existe um candidato com este codigo e regiao. Favor informar outro!")
        cadastrar_candidato()

    try:
        arquivo = open(obter_nome_arquivo(), "wb")
        base[random.randrange(0,100001)] = candidato
        pickle.dump(base,arquivo)
    except Exception as ex:
        print("Erro ao cadastrar o candidato!")
        print(ex)
    finally:
        arquivo.close()

    
def listar_candidatos_cadastrados():
    try:
        arquivo = open(obter_nome_arquivo(), "rb")
        list_cand = pickle.load(arquivo)
        for key in sorted(list_cand.keys()):
            print('\n')
            print("Codigo.........: " + list_cand[key]["codigo"])
            print("Nome...........: " + list_cand[key]["nome"])
            print("Cargo..........: " + list_cand[key]["cargo"])
            print("Regiao.........: " + obter_descricao_regiao(list_cand[key]["regiao"]))
            print("Numero de Votos: " + list_cand[key]["num_votos"])
    except Exception as ex:
        print("Erro ao listar os candidatos cadastrados!")
        print(ex)
    finally:
        arquivo.close()
    
def listar_voto_por_candidato():
    
    codigo = raw_input("Digite o codigo do candidato\n")
    
    try:
        arquivo = open(obter_nome_arquivo(), "rb")
        list_cand = pickle.load(arquivo)
        soma_regiao_norte = 0
        soma_regiao_sul = 0
        soma_regiao_nordeste = 0
        soma_regiao_sudeste = 0
        soma_regiao_centro_oeste = 0
        achou_cand = False
        nome_cand = ""
        for key in sorted(list_cand.keys()):
            if(list_cand[key]["codigo"] == codigo):
                nome_cand = list_cand[key]["nome"]
                achou_cand = True
                if(list_cand[key]["regiao"] == 1):
                    soma_regiao_norte += int(list_cand[key]["num_votos"])
                elif(list_cand[key]["regiao"] == 2):
                    soma_regiao_nordeste += int(list_cand[key]["num_votos"])
                elif(list_cand[key]["regiao"] == 3):
                    soma_regiao_centro_oeste =+ int(list_cand[key]["num_votos"])
                elif(list_cand[key]["regiao"] == 4):
                    soma_regiao_sul += int(list_cand[key]["num_votos"])
                elif(list_cand[key]["regiao"] == 5):
                    soma_regiao_sudeste += int(list_cand[key]["num_votos"])
        
        if(achou_cand):
            print('\n')
            print("Codigo............................: " + codigo)
            print("Nome..............................: " + nome_cand)
            print("Total de Votos Regiao Norte.......: {:d}".format(soma_regiao_norte))
            print("Total de Votos Regiao Nordeste....: {:d}".format(soma_regiao_nordeste))
            print("Total de Votos Regiao Centro-Oeste: {:d}".format(soma_regiao_centro_oeste))
            print("Total de Votos Regiao Sudeste.....: {:d}".format(soma_regiao_sudeste))
            print("Total de Votos Regiao Sul.........: {:d}".format(soma_regiao_sul))
        else:
            print("Candidato nao encontrado")
       
    except Exception as ex:
        print("Erro ao lista os votos do candidato por regiao")
        print(ex)
    finally:
        arquivo.close()
   
def listar_total_votos_cand():

    codigo = raw_input("Digite o codigo do candidato\n")

    try:
        arquivo = open(obter_nome_arquivo(), "rb")
        list_cand = pickle.load(arquivo)
        total_votos = 0
        nome = None
        for key in sorted(list_cand.keys()):
            if(list_cand[key]["codigo"] == codigo):
                nome = list_cand[key]["nome"]
                total_votos += list_cand[key]["num_votos"]
        
        print("O total de votos para o candidato: {} - {} foi de: {}".format(codigo, nome, total_votos))
    except Exception as ex:
        print("Erro ao listar total de votos por candidato!")
        print(ex)
    finally:
        arquivo.close()

def listar_total_votos_por_regiao():
    regiao = int(raw_input("Regiao:\n"
                           "[1] Norte\n"
                           "[2] Nordeste\n"
                           "[3] Centro-Oeste\n"
                           "[4] Sul\n"
                           "[5] Sudeste\n"
                           "Digite o codigo da regiao: "))
    
    try:
        arquivo = open(obter_nome_arquivo(), "rb")
        list_cand = pickle.load(arquivo)
        soma_total_votos = 0
        achou_regiao = False
        for key in sorted(list_cand.keys()):
            if(list_cand[key]["regiao"] == regiao):
                achou_regiao = True
                soma_total_votos += int(list_cand[key]["num_votos"])
                
        if(achou_regiao):
            print('\n')
            print("Regiao...........: " + obter_descricao_regiao(regiao))
            print("Total de Voto....: {:d}".format(soma_total_votos))
            print("\n")
        else:
            print("Regiao Nao Encontrada")
       
    except Exception as ex:
        print("Erro ao listar total de votos por regiao!")
        print(ex)
    finally:
        arquivo.close()
        
def listar_total_geral_regiao():
    
    try:
        arquivo = open(obter_nome_arquivo(), "rb")
        list_cand = pickle.load(arquivo)
        soma_regiao_norte = 0
        soma_regiao_sul = 0
        soma_regiao_nordeste = 0
        soma_regiao_sudeste = 0
        soma_regiao_centro_oeste = 0
        soma_total = 0
       
        for key in sorted(list_cand.keys()):
        
            if(list_cand[key]["regiao"] == 1):
                soma_regiao_norte += int(list_cand[key]["num_votos"])
                soma_total += soma_regiao_norte
            elif(list_cand[key]["regiao"] == 2):
                soma_regiao_nordeste += int(list_cand[key]["num_votos"])
                soma_total += soma_regiao_nordeste
            elif(list_cand[key]["regiao"] == 3):
                soma_regiao_centro_oeste += int(list_cand[key]["num_votos"])
                soma_total += soma_regiao_centro_oeste
            elif(list_cand[key]["regiao"] == 4):
                soma_regiao_sul += int(list_cand[key]["num_votos"])
                soma_total += soma_regiao_sul
            elif(list_cand[key]["regiao"] == 5):
                soma_regiao_sudeste += int(list_cand[key]["num_votos"])
                soma_total += soma_regiao_sudeste
        
        if(soma_total > 0):
            print('\n')
            print("Total de Votos Regiao Norte.......: {:d}".format(soma_regiao_norte))
            print("Total de Votos Regiao Nordeste....: {:d}".format(soma_regiao_nordeste))
            print("Total de Votos Regiao Centro-Oeste: {:d}".format(soma_regiao_centro_oeste))
            print("Total de Votos Regiao Sudeste.....: {:d}".format(soma_regiao_sudeste))
            print("Total de Votos Regiao Sul.........: {:d}".format(soma_regiao_sul))
            print("Total Geral.......................: {:d}".format(soma_total))
        else:
            print("Nao ha dados para exibir!")
       
    except Exception as ex:
        print("Erro ao lista os votos do candidato por regiao")
        print(ex)
    finally:
        arquivo.close()

def obter_descricao_regiao(regiao):
    descricao = None
    if (regiao == 1):
        descricao = "Norte"
    elif (regiao == 2):
        descricao = "Nordeste"
    elif (regiao == 3):
        descricao = "Centro-Oeste"
    elif (regiao == 4):
        descricao = "Sul"
    elif (regiao == 5):
        descricao = "Sudeste"
    
    return descricao


def exibir_opcoes():
     
    os.system("cls") 
    print("\n")
    print("###### Controle de Votacao #######")
    print("\n")
    print("1. Cadastrar Candidato")
    print("2. Listar candidatos cadastrados")
    print("3. Listar votos por candidato")
    print("4. Listar total de votos por candidato")
    print("5. Listar total de votos por regiao")
    print("6. Listar total geral por regiao")
    print("7. Sair do programa")

def criar_arquivo():
    arquivo = open(obter_nome_arquivo(), "wb")
    arquivo.close()

def obter_nome_arquivo():
    return "controle_votacao.db"

if __name__ == '__main__':
    opcao = None
 
    exibir_opcoes()
    
    criar_arquivo()
    
    while opcao != 1:
        opcao = raw_input("\nOpcao: ")
        if opcao == "1":
            cadastrar_candidato()
            exibir_opcoes()
        elif opcao == "2":
            listar_candidatos_cadastrados()
            exibir_opcoes()
        elif opcao == "3":
            listar_voto_por_candidato()
            exibir_opcoes()
        elif opcao == "4":
            listar_total_votos_cand()
            exibir_opcoes()
        elif opcao == "5":
            listar_total_votos_por_regiao()
            exibir_opcoes()
        elif opcao == "6":
            listar_total_geral_regiao()
            exibir_opcoes()
        elif opcao == "7":
            print("Programado Finalizado!")
            exit()
            break
        else:
            print("\nOpcao Invalida")
 

