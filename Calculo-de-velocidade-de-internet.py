import math

def main():
  tamanhoMB=int(input('Digite o tamanho do arquivo em MB: '))
  velocidadeMb=int(input('Digite a velocidade da banda em Mb\s: '))

  tamanhoMb=tamanhoMB*8
  tempoS=tamanhoMb/velocidadeMb
  tempoM=tempoS/60
  print('Tempo de download em minutos será: ', tempoM)


  
if __name__ == "__main__":
 main()





