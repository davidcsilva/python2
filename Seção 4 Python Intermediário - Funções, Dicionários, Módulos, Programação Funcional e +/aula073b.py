"""
115. Termos técnicos: Higher Order Functions e First-Class Functions

Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)
