import math



def main():
  letra=input('Digite uma letra: ')
  vogal=('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y')
  consoantes=('Q', 'Z', 'X', 'S', 'W', 'D', 'C', 'V', 'F', 'R', 'T', 'G', 'B', 'N', 'H', 'J', 'M', 'K', 'L', 'P', 'q', 'z', 'x', 's', 'w', 'd', 'c', 'v', 'f', 'r', 't', 'g', 'b', 'n', 'h', 'j', 'm', 'k', 'l', 'p')
  x=0
  nvogal=len(vogal)
  nconsoantes=len(consoantes)
  
  while(x < nvogal):
    if(letra == vogal[x]):
      print('É uma vogal!')
      exit()
    x+=1

  x=0
  while(x < nconsoantes):
    if(letra == consoantes[x]):
      print('É uma consoante!')
      exit()
    x+=1  


  

if __name__ == "__main__":
  main()





