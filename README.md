# Exercícios de Programação Orientada a Objetos em Python

Este repositório contém a resolução de uma lista de exercícios práticos de Orientação a Objetos (POO) em Python. O foco principal é a aplicação de conceitos fundamentais, como encapsulamento (uso de getters e setters), herança e polimorfismo.

Todo o código desenvolvido é validado por uma suíte de testes automatizados utilizando a biblioteca `pytest`.

## Estrutura do Projeto

*   **`/codigo`**: Contém as classes desenvolvidas ao longo dos exercícios (ex: Pessoa, Produto, Funcionário, ContaBancaria, entre outras).
*   **`/teste`**: Contém os arquivos de teste unitário criados para validar rigorosamente a lógica de negócio de cada classe.
*   **`.github/workflows`**: Contém a configuração de Integração Contínua (CI). A cada envio de código (push), o GitHub Actions instala as dependências, verifica a formatação do código com `flake8` e executa todos os testes automaticamente.

## Como Executar os Testes

Certifique-se de ter o Python e o `pytest` instalados na sua máquina. 

1. Clone o repositório:
```bash
git clone https://github.com/Stuartti/Exercicios-Python-Poo.git
