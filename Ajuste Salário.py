#Entrada de Dados:
salario = float(input("Entre com o salario [R$]: "))
aumento = float(input("Entre com o aumento [ %]: "))

#Processamento:
novoSalario = salario + (salario*(aumento/100))

#Saida:
print("O novo salario do funcionario com aumento de ",aumento," %"," é de R$ ",novoSalario)
