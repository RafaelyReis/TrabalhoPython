# Parte 1: Cálculo da Taxa Metabólica Basal (TMB)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
idade = float(input("Digite sua idade: "))
sexo = input("Por último, mas não menos importante, digite seu sexo: ")

if sexo == "masculino":
    tmb = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
    print(f"Sua taxa de metabolismo basal, com base nos seus dados sendo do sexo masculino, é {tmb}")

elif sexo == "feminino":
    tmb = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    print(f"Sua taxa de metabolismo basal, com base nos seus dados sendo do sexo feminino, é {tmb}")

print()

# Parte 2: Cálculo dos Macronutrientes

prot = 2 * peso 
carb = 3 * peso
gord = 0.5 * peso
print(f"Os macronutrientes que você deverá consumir diariamente são {prot} gramas de proteína, {carb} gramas de carboidrato, {gord} gramas de gordura")

print()

# Parte 3: Cálculo do Gasto Calórico durante o Exercício

musculacao_media = 3.5
musculacao_alta = 6

exercicio = input("Digite o exercício que você pratica: ")
tabela_met = [musculacao_media, musculacao_alta]

tempo = float(input("Por quanto tempo você pratica essa atividade em horas: "))

if exercicio == "musculacao_media":
   met = 3.5 * peso * tempo 
   print(f"A quantidade de calorias que você consome é de {met}") 

elif exercicio == "musculacao_alta":
   met = 6 * peso * tempo 
   print(f"A quantidade de calorias que você consome é de {met}")