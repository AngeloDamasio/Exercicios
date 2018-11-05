print ('              Calculo de salario mensal pelo valor da hora\n\n\n\n\n')

ganhoh=int(input('Quanto você ganha por hora? '))
horam=int(input('Quantas horas você trabalha por mês? '))


salariobr= ganhoh * horam
IRRF= salariobr*0.11
INSS= salariobr*0.08
ROUBO= salariobr*0.05
salariolq= salariobr-IRRF-IRRF-ROUBO

print ('Salário Bruto: ', salariobr)
print ('IRRF: ', IRRF)
print ('INSS: ', INSS)
print ('Estorção Sindical: ', ROUBO)
print ('Salário Líquido: ', salariolq)
