#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

valor_salario = float(input("insira o valor de seu salario:\n"))

if valor_salario <= 280:
    valor_final = valor_salario * 0.20
    valor_final = valor_salario + valor_final
    valor_resto = valor_final - valor_salario
    print (f"\nSeu valor após aumento é: {valor_final}\n")
    print (f"Seu salario antes era: {valor_salario}\n")
    print (f"Sua diferença foi de: {valor_resto}\n")

elif valor_salario > 280 and valor_salario < 700:
    valor_final = valor_salario*0.15
    valor_final = valor_final + valor_salario
    valor_resto = valor_final - valor_salario
    print (f"\nSeu valor após aumento é: {valor_final}\n")
    print (f"Seu salario antes era: {valor_salario}\n")
    print (f"Sua diferença foi de: {valor_resto}\n")

elif valor_salario >= 700 and valor_salario < 1500:
    valor_final = valor_salario*0.10
    valor_final = valor_final + valor_salario
    valor_resto = valor_final - valor_salario
    print (f"\nSeu valor após aumento é: {valor_final}\n")
    print (f"Seu salario antes era: {valor_salario}\n")
    print (f"Sua diferença foi de: {valor_resto}\n")
    
elif valor_salario > 1500:
    valor_final = valor_salario*0.05
    valor_final = valor_final + valor_salario
    valor_resto = valor_final - valor_salario
    print (f"\nSeu valor após aumento é: {valor_final}\n")
    print (f"Seu salario antes era: {valor_salario}\n")
    print (f"Sua diferença foi de: {valor_resto}\n")

#ass: Pedro Macegosa/CrazyOreoYT
#Caso encontre algum erro no codigo, avise ou pode att