# Importando os módulos
import pacote_inicializado.modulo_1, pacote_inicializado.modulo_2

print(f'O Arquivo __init__.py do Pacote {__name__} foi executado')

# Criação de uma variável Global
v_global = ['Pedro', 32, 1.82, True]

#Criação de uma função Global
def f_global():
	print(f'A Função de inicialização foi executada!')