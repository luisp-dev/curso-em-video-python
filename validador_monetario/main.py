"""Curso em Vídeo - Exercício 112: Entrada de Dados Monetários"""

from funcoes import moeda
from funcoes import dados

if __name__ == '__main__':
    preco = dados.leia_dinheiro('Digite o preço: R$')
    moeda.resumo(preco, 35, 22)
