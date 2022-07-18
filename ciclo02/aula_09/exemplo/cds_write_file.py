import csv  # leitura do arquivo
import json  # criação do arquivo json
import sys  # busca de erros na criação
import os  # criação do diretorio aonde vão ser salvos os arquivos gerados

from .cds_helpers import choose_damage_level



# Função que irá criar o arquivo JSON
def save_json(records, file_name='statistics', path='exemplo/json_out'):
    # Lista que será escrita dentro do arquivo JSON
    array_of_incidents = []

    # Pega a quantidade total de dados
    count = len(records)

    # Dicionário criado para conter a estrutura desejada para o arquivo JSON
    map_of_incidents = {}

    # Itera sobre os registros
    for record in records:

        # Recupera o conteúdo da Fase de Operação
        key = record['aeronave_fase_operacao']

        # Verifica se a fase de operação separada ja está inserida dentro do conteúdo
        # do arquivo. Se ainda não estiver, insere o registro com a contagem iniciando
        # em 1, se já tiver, aumenta a contagem em 1

        if key in map_of_incidents:
            map_of_incidents[key] += 1  # Se existir, incrementa + 1 acidente
        else:
            map_of_incidents[key] = 1

    # Itera sobre o dicionário com os dados
    for key, value in map_of_incidents.items():
        # Cria o conteúdo que será escrito no arquivo
        array_of_incidents.append(
            {
                "fase_operacao": key,
                "ocorrencias": value,
                "percentual": '{:.2%}'.format(value / count)
            }
        )

    # Cria o arquivo com os dados ajustados
    try:
        # Cria o arquvi no caminho/diretório escolhido
        # A biblioteca 'os' serve para conseguirmos criar tanto o arquivo quanto o
        # diretório, caso ambos não existam
        # Essa linha faz com que não ocorram erros na criação do arquivo
        # os.makedirs(os.path.dirname(f'{path}/{file_name}.json'), exist_ok=True)

        with open(f'{path}/{file_name}.json', 'w', encoding='utf-8') as outfile:

            json.dump(array_of_incidents, outfile, ensure_ascii=False, indent=4)

        print('Arquivo criado com sucessso')

    except:

        print(F'ERRO AO CRIAR O ARQUIVO: {sys.exc_info()[0]} - {sys.exc_info()[1]}')


# Função que irá criar o arquivo CSV
def save_csv(records, op=0, file_name='levels', path='exemplo/csv_out'):
    # Lista que irá guardar os dados
    list_of_incidents = []

    damage_level = choose_damage_level(records)

    # Cabeçalho do arquivo CSV

    header = ['operation',
              'type',
              'manufacturer',
              'engine_type',
              'engines',
              'year_manufacturing',
              'seating',
              'fatalities'
              ]
    # Itera sobre oss registros
    for row in records:

        # Verifica se
        if row['aeronave_nivel_dano'] == damage_level:
            # Adiciona as linhas selecionadas
            list_of_incidents.append(
                [
                    row['aeronave_operador_categoria'],
                    row['aeronave_tipo_veiculo'],
                    row['aeronave_fabricante'],
                    row['aeronave_motor_tipo'],
                    row['aeronave_motor_quantidade'],
                    row['aeronave_ano_fabricacao'],
                    row['aeronave_assentos'],
                    row['total_fatalidades']
                ]
            )

        # Cria o arquivo com os dados ajustados
    try:
        os.makedirs(os.path.dirname(f'{path}/{file_name}.csv'), exist_ok=True)

        with open(f'{path}/{file_name}.csv', 'w', encoding='utf-8', newline='') as outfile:
            w = csv.writer(outfile)
            w.writerow(header)
            w.writerows(list_of_incidents)

        print('Arquivo criado com sucesso')
    except:
        print(F'ERRO AO CRIAR O ARQUIVO: {sys.exc_info()[0]} - {sys.exc_info()[1]}')


