import math

galaop=80
galaol=18
latap=25
latal=3.6





#convente galões para latas, e vice-versa, digitando 0 para g-->l e 1 para l-->g
def convert_gl(operador, quantidade):

  if operador == 0 :
    galoes = quantidade
    gl = galoes*galaol
    nlatas = gl/latal
    
    return math.ceil(nlatas)
  
  if operador == 1 :
    latas = quantidade
    ll=latas*latal
    ngaloes = ll/galaol
    return math.ceil(ngaloes)

  if (operador == 0) or (operador == 1 ) :
    print ('error!!!')

  


#pega os metros quadrados que precisa pintar, e indica quantos litros de tinta serão necessários
#com adicional de 10%
def calculo_ml(metros):
  
  l= metros/6
  ld=l+l*0.1
  arr = math.ceil(ld)

  return arr

#calcula quantidade de galoes
def galoes(litros):
  ngaloes= litros/galaol
  ngaloes= math.ceil(ngaloes)

  return ngaloes

#calcula quantidade de latas
def latas(litros):
  nlatas= litros/latal
  nlatas= math.ceil(nlatas)

  return nlatas
#qt[0] = galoes
#qt[1] = latas
def qtmelhorvalor(litros):

  if litros < galaol :
    nlatas= litros/latal
    nlatas2= math.ceil(nlatas)
   # nlatas= nlatas-nlatas2
   # intlatas=int(nlatas)
    qt=[0, nlatas2]
    

    return qt
    
  if litros == galaol :
    qt=[0, 1]
    
    return qt
  
  if litros > galaol :
    ngaloes= litros/galaol
    ngaloes2= math.ceil(ngaloes)
    difgaloes= ngaloes-ngaloes2
    intgaloes=int(ngaloes)
    gl=convert_gl(0,difgaloes)
    qt= [intgaloes, gl]
    
    return qt

#valor de uma determinada quantidade de galoes
def valorlatas(latas):

  valor=latas*latap

  return valor
#valor de uma determinada quantidade de galoes
def valorgaloes(galoes):
  valor=galoes*galaop

  return valor

def melhorvalor(qt):

  vgaloes=qt[0]*galaop
  vlatas=qt[1]*latap

  valor=vgaloes+vlatas

  return valor

def main():
  
  
  mp= int(input('Quanto em metros quadrados você precisa pintar? '))

  litros= int(calculo_ml(mp))
  qt=qtmelhorvalor(litros)
  ngaloes=galoes(litros)
  nlatas=latas(litros)
  vlatas=valorlatas(nlatas)
  vgaloes=valorgaloes(ngaloes)

  print ('Dado a area que precisa pintar, temos três opções para:')
  print ('1. Apenas Galões -->  Quantidade de galões: ', ngaloes,' valor, R$ ', vgaloes)
  print ('2. Apenas latas -->  Quantidade de latas: ', nlatas,' valor, R$ ', vlatas)
  print ('3. Misto(MELHOR VALOR) -->  Quantidade de galões: ', qt[0], 'Quantidade de latas: ', qt[1],' valor, R$ ', melhorvalor(qt))

  

if __name__ == "__main__":
  main()





