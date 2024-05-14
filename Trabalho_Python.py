import sys


def calcular_tmb(peso, altura, idade, sexo):
    
    #Calcula a Taxa de Metabolismo Basal (TMB) usando a equação de Harris-Benedict.
    
    #peso (float): Peso do usuário em kg.
    #altura (float): Altura do usuário em cm.
    #idade (int): Idade do usuário em anos.
    #sexo (str): Sexo do usuário ("masculino" ou "feminino").
 
    #Return:(float): TMB calculada.
    
    if sexo == "masculino":
     tmb = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
    
    
    elif sexo == "feminino":
        tmb = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
   
    else:
        tmb = None
        print("Sexo não reconhecido.")
   
    return tmb

def calcular_macronutrientes(peso):
    
    #Calcula a quantidade de macronutrientes com base no peso do usuário.
    
    #peso (float): Peso do usuário em kg.    
    #Return: Quantidade de proteína, carboidratos e gorduras em gramas.
    
    prot = 2 * peso 
    carb = 3 * peso
    gord = 0.5 * peso
   
    return prot, carb, gord

def calcular_gasto_calorico(exercicio, peso, tempo):
    

    #musculação media
    if exercicio == 1:
        return 3.5 * peso * tempo
    
    #musculação alta
    elif exercicio == 2:
         return 6 * peso * tempo
  
    #sair
    elif exercicio == 3:
        print("Saindo do programa!")
        sys.exit()
   
   #nao selecionou nenhuma das opções
    else:
        print("Exercício não reconhecido.")
        return None
 

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

        #Pergunta que faremos a pessoa.
        print("Digite o número do exercício que você pratica:")
        print("1 - Musculção média")
        print("2 - Musculção alta")
        print("3 - Não pratico nenhum desses exercícios / Sair")
        exercicio = int(input("Digite o numero do exercício desejado: "))
        tempo = float(input("Por quanto tempo você pratica essa atividade em horas: "))
        gasto_calorico = calcular_gasto_calorico(exercicio, peso, tempo)
       
        if gasto_calorico is not None:
            if exercicio == 1:
                print(f"Durante {tempo} horas de Musculação média, você queimou {gasto_calorico:.2f} calorias.")
            elif exercicio == 2:
                print(f"Durante {tempo} horas de Musculação alta, você queimou {gasto_calorico:.2f} calorias.")
        else:
            print("Exercício não reconhecido.")
    else:
        print("Não foi possível calcular a TMB. Verifique os dados fornecidos.")

if __name__ == "__main__":
    main()