import csv


# Resolução
# Função que irá processar o Arquivo

def read_file(file_path, delimiter=',', quotechar='"', encoding='utf-8'):
    # Estruturas que serão utilizadas para produzir as respostas
    retorno = []

    # Abre e processa o arquivo
    with open(file_path, 'r', encoding=encoding) as f:
        reader = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)

        # Itera pelas linhas do arquivo para
        for row in reader:
            retorno.append(row)

    return retorno