# Curadoria de Desafios: Python Fundamentos 🐍

Este repositório reúne uma seleção dos desafios de lógica mais complexos e estruturados que desenvolvi durante o Módulo 3 do curso de Python do **Curso em Vídeo (Prof. Gustavo Guanabara)**. 

O objetivo desta coleção é demonstrar maturidade na escrita de algoritmos, manipulação de coleções de dados na memória e estruturação de projetos modulares.

---

## 📂 Visão Geral dos Projetos

Aqui está o que cada script resolve e os conceitos chave aplicados em cada um:

### 📑 Scripts de Arquivo Único
* **`analise_peso_pessoas.py`**: Sistema de análise que utiliza listas compostas (aninhadas) para catalogar dados e identificar extremos (maiores e menores valores) dentro de uma única estrutura.
* **`cadastro_jogadores.py`**: Gerenciador de aproveitamento esportivo baseado em dicionários aninhados e listas, lidando com a leitura e exibição de dados tabulares complexos no terminal.
* **`validador_votacao.py`**: Algoritmo focado no escopo de funções e controle de fluxo, determinando a obrigatoriedade de voto com base em dados de nascimento.
* **`analisador_notas.py`**: Função avançada que recebe múltiplas notas empacotadas (`*n`), gera relatórios de situação e retorna um dicionário estruturado com os metadados da turma.
* **`validacao_dados.py`**: Script focado em resiliência de software. Implementa validação estrita de dados numéricos (inteiros e floats) utilizando blocos de tratamento de exceções (`try/except`) para impedir interrupções inesperadas causadas por inputs inválidos.

### 📦 Projetos Modularizados e Pacotes
* **`validador_monetario/`**: Projeto focado em modularização através da criação de pacotes locais (`dados` e `moeda`). Centraliza funções de formatação visual de moedas e validação de dados de entrada de forma desacoplada.
* **`sistema_cadastro/`**: Mini-sistema de cadastro dividido em bibliotecas. Realiza a persistência de dados local simulando um banco de dados simples através da leitura e escrita em arquivos de texto (`.txt`), contando com um sistema de menu robusto.

---

## 🛠️ Tecnologias e Conceitos Aplicados
* **Lógica de Programação Pura**
* **Estruturas de Dados Compostas** (Listas, Dicionários e Tuplas)
* **Funções** (Modularização, Parâmetros Opcionais e Empacotamento)
* **Tratamento de Erros e Exceções** (`try`, `except`, `ValueError`)
* **Manipulação de Arquivos de Texto** (Persistência de Dados)

---

## 📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.