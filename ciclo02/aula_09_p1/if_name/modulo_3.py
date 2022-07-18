def calcula_imc(nome, peso, altura):
	string = f'O usuario {nome} possuí {peso} Kg de massa e {altura} cm de altura. Logo, seu IMC é {(peso / (altura * altura)):.2f}'
	print(string)

if __name__ == '__main__':
	nome = 'Pedro'
	peso = 93.5
	altura = 1.82
	calcula_imc(nome, peso, altura)
else:
	nome = 'Guilherme'
	peso = 76.0
	altura = 1.82
	print(f'A função "calcula_imc()" está pronta para ser utilizada!')