def calcular_tmb(peso, altura, idade, sexo):
    
    if sexo == "masculino":
     tmb = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
    
    
    elif sexo == "feminino":
        tmb = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
   
    else:
        tmb = None
        print("Sexo não reconhecido.")
   
    return tmb

def calcular_macronutrientes(peso):
   
    prot = 2 * peso 
    carb = 3 * peso
    gord = 0.5 * peso
   
    return prot, carb, gord

def calcular_gasto_calorico(exercicio, peso, tempo):
    tabela_met = {"musculacao_media": 3.5, "musculacao_alta": 6}
   
    if exercicio in tabela_met:
        met = tabela_met[exercicio] * peso * tempo
   
    else:
        met = None
        print("Exercício não reconhecido.")
   
    return met

def main():
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em centimetros): "))
    idade = float(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (masculino/feminino): ").lower()

    tmb = calcular_tmb(peso, altura, idade, sexo)
   
    if tmb is not None:
        print(f"Sua taxa de metabolismo basal é {tmb:.2f} calorias.")

        prot, carb, gord = calcular_macronutrientes(peso)
        print(f"Para atender suas necessidades diárias, consuma {prot:.2f}g de proteína, {carb:.2f}g de carboidratos e {gord:.2f}g de gordura.")

        exercicio = input("Digite o exercício que você pratica: ")
        tempo = float(input("Por quanto tempo você pratica essa atividade em horas: "))
        gasto_calorico = calcular_gasto_calorico(exercicio, peso, tempo)
       
        if gasto_calorico is not None:
            print(f"Durante {tempo} horas de {exercicio}, você queimou {gasto_calorico:.2f} calorias.")
   
    else:
        print("Não foi possível calcular a TMB. Verifique os dados fornecidos.")

if __name__ == "__main__":
    main()