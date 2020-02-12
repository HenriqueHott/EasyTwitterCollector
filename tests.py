import json
import time
from sys import exit
from glob import glob
from util import util
from services import streaming

""" Modulo executavel para testes. Seja feliz """

def test1():
    """
        Teste para contabilizar a consistencia dos JSON savlos em disco recebidos da API
        Historico:
        Data 07/02/2020 -- Status OK  -- Obs
    """
    teste_file_list = glob('F:\\workfolder\\bolsonaro\\statuses\\2020\\02\\10\\*')
    x = 0
    for name in teste_file_list:
        print(util.count_file_lines(name))
        x += util.count_file_lines(name)
    print(x)

def test2():
    """
        Teste para checar a consistencia dos JSON savlos em disco recebidos da API
        Historico:
        Data 07/02/2020 -- Status OK  -- Obs
    """

    teste_file_list = glob('')
    output = open('', mode='w')
    for name in teste_file_list:
        output.write(name + '\n')
        for line in open(name, encoding='utf8'):
            data = json.loads(line, encoding='utf8')
            output.write(data['id_str'] + ' ' + data['created_at'] + '\n')

    output.close()


def test3():
    """
        Teste para gerenciamento de logs da aplicacao
        Historico:
        Data 11/02/2020 -- Status OK  -- Obs
    """

    flag = True
    while True:
        if flag:
            util.write_log('testando1', 'execution')
            util.write_log('testando2', 'error')
            flag = False

        else:

            flag = True

        time.sleep(10)


def test4():

    """
        Teste para salvar o log de execoes
        Historico:
        Data 11/02/2020 -- Status OK  -- Obs
    """

    try:
        raise Exception('testTesteTest')
    except Exception as e:
        util.write_log('teeeest', 'exception', e)

if __name__ == '__main__':
    test3()
    exit(0)