print ('              Programa Sem noção de peso ideal por sexo\n\n\n')

altura=float(input('Digite sua altura: '))
sexo=input('informe seu sexo digitando m para mulher, e h para homem: ')

if sexo == 'h' :
  pesoideal=(72.7*altura)-58
  print ('O seu peso sem noção ideal é: ', pesoideal)
else:
  pesoideal=(62.1*altura)-44.7
  print ('O seu peso sem noção ideal é: ', pesoideal)  
