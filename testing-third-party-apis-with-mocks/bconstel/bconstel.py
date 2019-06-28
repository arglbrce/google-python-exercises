# coding: utf-8

import csv
import json

import requests

CABECALHO = ('#', 'REGIONAL', 'ÁREA', 'NOME', 'EMAIL', 'MATRICULA',
             'RAMAL', 'CHEFIA', 'EMAIL-CHEFIA', 'RAMAL-CHEFIA')
CONSTEL_URL = 'https://constel.serpro.gov.br/s.php'


def obter_empregado(termo="DAAT3"):
    parametros = {'term': termo}
    response = requests.get(CONSTEL_URL, params=parametros)
    return json.loads(response.content)


def obter_chefia(empregado):
    return obter_empregado(empregado['manager'])


def sucesso_obter_empregado(empregado):
    try:
        if empregado[0]['error']:
            return False
    except KeyError:
        return True


def exibir_empregado(empregado):
    if sucesso_obter_empregado(empregado):
        for k, v in empregado[0].items():
            print("{}: {}".format(k, v))
    else:
        print('Não validado')


def ler_arquivo_empregados(arquivo='dados.txt'):
    empregados = []
    with open(arquivo, 'r') as f:
        for empregado in f:
            empregados.append(obter_empregado(empregado))
    return empregados


def chaves_empregado():
    return ('usrlocal', 'ou', 'cn', 'mail', 'employeenumber', 'telephonenumber')


def chaves_chefia():
    return ('cn', 'mail', 'telephonenumber')


def merge_empregado_chefia(empregado, chefia):
    # print('Empregago: {} Chefia: {}'.format(type(empregado), type(chefia)))
    merge = list(empregado.values()) + chefia
    return merge


def empregado_ordenado_chaves(empregado, chaves):
    _empregado = []
    for c in chaves:
        _empregado.append(empregado[c])
    # print(_empregado)
    return _empregado


def chefia_ordenado_chaves(chefia, chaves):
    _chefia = []
    for c in chaves:
        _chefia.append(chefia[0][c])
    # print(_chefia)
    return _chefia


def gerar_csv(empregados=[], arquivo='empregados.csv'):
    with open(arquivo, 'w', newline='') as csvfile:
        # fieldnames = ['usrlocal', 'ou', 'cn', 'mail', 'employeenumber', 'telephonenumber']
        # fieldnames = empregados[0][0].keys()
        fieldnames = list(chaves_empregado()) + list(chaves_chefia())
        print(fieldnames)
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for empregado in empregados:
            # print(obter_chefia(empregado[0]))
            # print(chefia_ordenado_chaves(obter_chefia(empregado[0]), chaves_chefia()))
            empregado_chefia = merge_empregado_chefia(empregado[0],
                                                      chefia_ordenado_chaves(obter_chefia(empregado[0]),
                                                                             chaves_chefia()))
            print('Empregado-Chefia: {}'.format(empregado_chefia))
            writer.writerow(empregado_chefia)


def main():
    # funcionario = obter_empregado("Allan Reffson")
    # print(len(funcionario))
    # print(sucesso_obter_empregado(funcionario))
    # exibir_empregado(funcionario)
    emp = ler_arquivo_empregados('dados.1.txt')
    gerar_csv(emp)


if __name__ == "__main__":
    main()
