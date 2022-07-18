import csv

# Função que irá processar o Arquivo
def read_file(file_path, delimiter = ',', quotechar='', encoding = 'utf-8'):
   
    # Estruturas que serão utilizadas para produzir os registros
    list_of_registers = []
    
    # Abre e processa o arquivo
    with open(file_path, 'r', encoding = encoding) as f:
        reader = csv.DictReader(f, delimiter = delimiter)
        
        # Itera pelas linhas do arquivo para 
        for row in reader:
            
            # Recupera cada registro do insere na lista
            list_of_registers.append(row)
            
    # Retorna a lista com todos os registros
    return list_of_registers

