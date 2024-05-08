"tabela de quantidade de calorias"

exercicio = input(" digite o exercicio que voce pratica: ")

musculaçaoMedia = 3.5

musculaçaoAlta = 6

peso = float(input("digite o seu peso: "))

tempo = float(input("por quant tempo voce pratica essa atividade em horas:  "))

if exercicio == "musculaçaoMedia":

   met =  3.5 * peso * tempo 

   print(f"a quantidade de calorias que voce consome é de {met}") 


elif exercicio == "musculaçaoAlta":

   met =  6 * peso * tempo 

   print(f"a quantidade de calorias que voce consome é de {met}") 

"--------------------------------------------------------------------------------"

"macronutrientes"

peso = float(input("digite o seu peso: "))

prot = 2 * peso 

carb = 3 * peso

gord = 0.5 * peso

print(f"os macro nutrientes que voce devera consumir diariamente sao {prot} gramas de proteina, {carb} gramas de carboidrato, {gord} gramas de gordura")

"----------------------------------------------------------------------------------"

"taxa de metabolismo basal"

peso = float(input("digite seu peso:  "))

altura = float(input("digite sua altura:  "))

idade = float(input("digite sua idade:  "))

sexo = input("por ultimo mas nao menos importante digite seu sexo: ")

if sexo == "homem":

    tmb = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)

    print(f"sua taxa de metabolismo basal sendo com base nos seus dados sendo homem é {tmb}")

elif sexo == "feminino":

    tmb = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

    print(f"sua taxa de metabolismo basal sendo com base nos seus dados sendo mulher é {tmb}")"