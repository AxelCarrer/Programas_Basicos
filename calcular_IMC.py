#Calcular IMC
peso = float(input("Ingrese su peso (KG): "))
altura = float(input("Ingrese su altura (m): "))

imc = peso / (altura ** 2)

print("Su IMC es: ", imc)