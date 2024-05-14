# Projeto de Cálculo de Macronutrientes e Gasto Calórico

Este projeto foi feito por RafaelyReis e Sutsca(Beatriz Salles) e é um programa simples em Python que calcula a Taxa de Metabolismo Basal (TMB), os macronutrientes necessários e o gasto calórico com base em informações fornecidas pelo usuário. Ele usa a equação de Harris-Benedict para calcular a TMB e fornece recomendações de consumo de macronutrientes. Além disso, estima o gasto calórico durante diferentes tipos de exercícios.

## Funcionalidades

- **Cálculo da TMB**: Utiliza a equação de Harris-Benedict para calcular a TMB com base no peso, altura, idade e sexo do usuário.
- **Recomendação de Macronutrientes**: Calcula a quantidade de proteína, carboidratos e gorduras que o usuário deve consumir diariamente.
- **Estimativa de Gasto Calórico**: Estima o gasto calórico durante atividades físicas específicas.

## Pré-requisitos

- Python 3.x
- Biblioteca `sys` (parte da biblioteca padrão do Python)

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/RafaelyReis/TrabalhoPython.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd TrabalhoPython
    ```

3. Execute o script principal:
    ```bash
    python Trabalho_Python.py
    ```

## Estrutura do Código

### Funções Principais

#### `calcular_tmb(peso, altura, idade, sexo)`

Calcula a Taxa de Metabolismo Basal (TMB) usando a equação de Harris-Benedict.

- **Parâmetros**:
  - `peso` (float): Peso do usuário em kg.
  - `altura` (float): Altura do usuário em cm.
  - `idade` (int): Idade do usuário em anos.
  - `sexo` (str): Sexo do usuário ("masculino" ou "feminino").
- **Retorna**: TMB calculada (float) ou None se o sexo não for reconhecido.

#### `calcular_macronutrientes(peso)`

Calcula a quantidade de macronutrientes com base no peso do usuário.

- **Parâmetros**:
  - `peso` (float): Peso do usuário em kg.
- **Retorna**: Quantidade de proteína, carboidratos e gorduras em gramas (tuple).

#### `calcular_gasto_calorico(exercicio, peso, tempo)`

Calcula o gasto calórico com base no tipo de exercício, peso e tempo de atividade.

- **Parâmetros**:
  - `exercicio` (int): Tipo de exercício (1, 2 ou 3).
  - `peso` (float): Peso do usuário em kg.
  - `tempo` (float): Tempo de exercício em horas.
- **Retorna**: Gasto calórico estimado (float) ou None se o exercício não for reconhecido.

### Função Principal

#### `main()`

- Captura as informações do usuário (peso, altura, idade, sexo).
- Calcula a TMB e imprime o resultado.
- Calcula as necessidades diárias de macronutrientes e imprime o resultado.
- Pergunta ao usuário sobre o tipo de exercício e tempo de prática, calcula o gasto calórico e imprime o resultado.

## Exemplo de Uso

```bash
$ python nome_do_script.py
Digite seu peso (em kg): 70
Digite sua altura (em centímetros): 175
Digite sua idade: 25
Digite seu sexo (masculino/feminino): masculino
Sua taxa de metabolismo basal é 1756.75 calorias.
Para atender suas necessidades diárias, consuma 140.00g de proteína, 210.00g de carboidratos e 35.00g de gordura.
Digite o número do exercício que você pratica:
1 - Musculação média
2 - Musculação alta
3 - Não pratico nenhum desses exercícios / Sair
Digite o número do exercício desejado: 1
Por quanto tempo você pratica essa atividade em horas: 1.5
Durante 1.5 horas de Musculação média, você queimou 367.50 calorias.
