# Função responsável por criar a lista com todos os niveis de dano

def select_damage_level(records):
    # Variável responsável por guardar os níveis de danos das aeronaves
    uniques = {}

    # Variável responsável por mander o valor da opção que será utilizada pelo usuário
    # para selecionar o nível de dano da aeronave
    option = 0

    # Percorre a lista com os dados para criar o dicionário que irá conter as opções:
    # {'SUBSTANCIAL': 0, ... 'DESTRUIDA':4}
    for record in records:
        if record['aeronave_nivel_dano'] not in uniques.keys():
            uniques[record['aeronave_nivel_dano']] = option
            option += 1

    return uniques


def choose_damage_level(records):
    # Cria o dicionário com todas as opções de dano
    damage_levels = select_damage_level(records)

    # Inicia a string que será exibida ao usuário
    string = f'Selecione a categoria de um dano desejada através dos seus respectivos códigos.\n'

    # Percorre o dicionário com os valores do dicionário e cria a string que será
    # exibida ao usuário
    for key, value in damage_levels.items():
        string += f'{value} = {key}; '

    # Finaliza a string
    string += f'\n'

    # Recupera o dano escolhido pelo usuário
    op = int(input(string))

    # Devolve a strinf com o dano selecionado
    return list(damage_levels.keys())[list(damage_levels.values()).index(op)]
