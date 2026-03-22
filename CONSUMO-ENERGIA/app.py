## app.py 

print("="*40)
print("   Calculadora de Consumo Elétrico   ")
print("="*40)

# 1. ENTRADA DE DADOS (Responda no terminal!)
nome_aparelho = input("Qual o nome do aparelho? ")
potencia_w = float(input(f"Qual a potência de {nome_aparelho} (W)? "))
horas_dia = float(input(f"Quantas horas de uso por dia? "))

# 2. CONFIGURAÇÕES E CÁLCULOS
dias_mes = 30
tarifa_kwh = 0.75
consumo_kwh_mes = (potencia_w * horas_dia * dias_mes) / 1000
custo_estimado = consumo_kwh_mes * tarifa_kwh

# 3. RESULTADO DINÂMICO (Usa as chaves {} para mostrar o que você digitou)
print("\n" + "-"*40)
print(f" RELATÓRIO DE CONSUMO: {nome_aparelho}")
print(f" Potência: {potencia_w} W")
print(f" Uso Diário: {horas_dia} horas")
print(f" Consumo Estimado: {consumo_kwh_mes:.2f} kWh/mês")
print(f" Custo Estimado: R$ {custo_estimado:.2f}/mês")
print("-"*40)
print(" Economize Energia!")
print("="*40)