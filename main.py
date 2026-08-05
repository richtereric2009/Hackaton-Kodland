print("=" * 55)
print("      CALCULADORA DE EMISSÃO DE CARBONO")
print("=" * 55)

# ==========================
# TRANSPORTE
# ==========================

print("\n=== Transporte ===")

km = float(input("Quantos quilômetros você dirige por semana? "))

print("\nTipo de veículo:")
print("1 - Gasolina")
print("2 - Etanol")
print("3 - Diesel")
print("4 - Elétrico")

tipo = int(input("Escolha uma opção: "))

if tipo == 1:
    fator_carro = 0.19
elif tipo == 2:
    fator_carro = 0.12
elif tipo == 3:
    fator_carro = 0.21
else:
    fator_carro = 0.05

onibus = int(input("\nQuantas viagens de ônibus você faz por semana? "))

aviao = int(input("Quantas viagens de avião você faz por ano? "))


# ==========================
# ENERGIA
# ==========================

print("\n=== Energia ===")

energia = float(input("Consumo mensal de energia (kWh): "))


# ==========================
# ALIMENTAÇÃO
# ==========================

print("\n=== Alimentação ===")

print("Consumo de carne bovina:")
print("1 - Nunca")
print("2 - Pouco")
print("3 - Algumas vezes por semana")
print("4 - Todos os dias")

carne = int(input("Escolha uma opção: "))


# ==========================
# RECICLAGEM
# ==========================

print("\n=== Reciclagem ===")

plastico = input("Você recicla plástico? (S/N): ").upper()
papel = input("Você recicla papel? (S/N): ").upper()
vidro = input("Você recicla vidro? (S/N): ").upper()


# ==========================
# CÁLCULOS
# ==========================

co2_carro = km * 52 * fator_carro

co2_onibus = onibus * 52 * 0.8

co2_aviao = aviao * 250

co2_energia = energia * 12 * 0.08

if carne == 1:
    co2_carne = 0
elif carne == 2:
    co2_carne = 300
elif carne == 3:
    co2_carne = 700
else:
    co2_carne = 1200

desconto = 0

if plastico == "S":
    desconto += 50

if papel == "S":
    desconto += 50

if vidro == "S":
    desconto += 50

total = (
    co2_carro
    + co2_onibus
    + co2_aviao
    + co2_energia
    + co2_carne
    - desconto
)


# ==========================
# RESULTADOS
# ==========================

print("\n" + "=" * 55)
print("RESULTADO")
print("=" * 55)

print(f"Carro: {co2_carro:.1f} kg CO₂/ano")
print(f"Ônibus: {co2_onibus:.1f} kg CO₂/ano")
print(f"Avião: {co2_aviao:.1f} kg CO₂/ano")
print(f"Energia: {co2_energia:.1f} kg CO₂/ano")
print(f"Alimentação: {co2_carne:.1f} kg CO₂/ano")
print(f"Redução por reciclagem: -{desconto:.1f} kg CO₂/ano")

print("-" * 55)
print(f"Emissão total estimada: {total:.1f} kg CO₂ por ano")


# ==========================
# CLASSIFICAÇÃO
# ==========================

if total < 1000:
    classificacao = "Excelente"
elif total < 2500:
    classificacao = "Boa"
elif total < 4000:
    classificacao = "Alta"
else:
    classificacao = "Muito Alta"

print(f"Classificação: {classificacao}")


# ==========================
# SUGESTÕES
# ==========================

print("\nSugestões para diminuir sua emissão de carbono:")

tem_sugestao = False

if km > 200:
    print("- Utilize transporte público, bicicleta ou caminhe em trajetos curtos.")
    tem_sugestao = True

if aviao >= 3:
    print("- Reduza viagens de avião quando possível.")
    tem_sugestao = True

if energia > 250:
    print("- Desligue aparelhos da tomada quando não estiverem em uso.")
    print("- Troque lâmpadas por modelos LED.")
    tem_sugestao = True

if carne == 4:
    print("- Reduza o consumo de carne bovina, pois sua produção gera muitas emissões.")
    tem_sugestao = True

if plastico == "N" or papel == "N" or vidro == "N":
    print("- Recicle plástico, papel e vidro para diminuir resíduos e emissões.")
    tem_sugestao = True

if onibus == 0 and km > 100:
    print("- Considere utilizar ônibus em alguns deslocamentos.")
    tem_sugestao = True

if not tem_sugestao:
    print("Parabéns! Seus hábitos já apresentam uma emissão relativamente baixa.")
    print("Continue mantendo práticas sustentáveis!")

print("\nObrigado por utilizar a Calculadora de Emissão de Carbono!")