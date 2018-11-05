print ('              Calculo da multa do pescador\n\n\n\n\n')

peso=int(input('Quantos kilos de peixe você trouxe? '))
cota= 50

if cota >= peso :
  
  print ('Não há multa')

else :
  
  dif= peso - cota
  multa= dif * 4
  print ('Sua multa por exedente de peso é: ', multa)
