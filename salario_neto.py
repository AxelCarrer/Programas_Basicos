salarioBruto = float(input("Ingrese su salario bruto: "))
porcentaje = float(input("Ingrese el porcentaje de impuestos: "))
deducciones = float(input("Ingrese las deducciones: "))

impuesto = salarioBruto * (porcentaje / 100)
salarioNeto = salarioBruto - impuesto - deducciones

print("Su salario Neto es de: ", salarioNeto)