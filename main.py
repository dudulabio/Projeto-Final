from pivo import Pivo

pivo1 = Pivo(tipo="Pivo Central Móvel Valley 8000 Series ", th="Th 1", cultura="Soja", potencia_vazao="3 m/s aproximadamente 152.1 L/s", area_ha="50")


print('________________________')
pivo1.imprimir()


# Pergunta ao usuário sobre a umidade do solo
while True:
    opcao = input("Qual a umidade do solo? (%): ").strip().lower()

    try:
        umidade = int(opcao)

        if umidade == 14:
            print('Umidade do solo ideal, não há necessidade de irrigação.')
            break
            
        if umidade == 13:
            print('A umidade do solo está em um nível ideal.')
            break

        elif umidade < 13:
            print("Umidade do solo abaixo do esperado, ligando pivo.")
            pivo1.ligar()
            break

        elif umidade > 14:
            print("Umidade do solo acima do ideal, não há necessidade de irrigação.")
            break

    except ValueError:
        print("Opção inválida. Por favor, digite um valor numérico para a umidade do solo.")



#############################################

pivo2 = Pivo(tipo="Pivo Lateral Móvel Valley 7000 Series ", th="Th 2", cultura="Sorgo", potencia_vazao="3 m/s aproximadamente 124.5 L/s.", area_ha="20")


print('________________________')
pivo2.imprimir()


# Pergunta ao usuário sobre a umidade do solo
while True:
    opcao = input("Qual a umidade do solo? (%): ").strip().lower()

    try:
        umidade = int(opcao)

        if umidade == 17:
            print('Umidade do solo ideal, não há necessidade de irrigação.')
            break

        if umidade == 14:
            print('A umidade do solo está em um nível ideal.')
            break

        elif umidade < 14:
            print("Umidade do solo abaixo do esperado, ligando pivo.")
            pivo1.ligar()
            break

        elif umidade > 14:
            print("Umidade do solo acima do ideal, não há necessidade de irrigação.")
            break

    except ValueError:
        print("Opção inválida. Por favor, digite um valor numérico para a umidade do solo.")
