distanciakm = float(input("Digite a distânicia em km: "))
if distanciakm >= 200:
    ate200 = distanciakm * 0.50
    print(f"O valor de sua viagem foi: {ate200}.")
else:
    maisde200 = distanciakm * 0.45
    print(f"O valor de sua viagem foi {maisde200}.")