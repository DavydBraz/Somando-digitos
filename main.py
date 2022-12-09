#Menu basico de selecao que vai retornar a opcao escolhida para o laco while
def Menu():
  try:
    print("\n-------------------------------------------------------")
    print("\n1-Soma dos digitos de um numero")
    print("\n2-Soma ponderada dos digitos de um numero")
    print("\n3-sair")
    print("\n-------------------------------------------------------")
    escolha=int(input("\nEscolha uma das opcoes acima: "))
    return escolha
  except:
    print("\nOcorreu um erro no menu de selecao")

#funcao para realizar a soma ponderada
def Somando_digitos_ponderada():
  #o try e except para tratamento de possiveis erros ja que tem input do usuario
  try:
    #contador que vai ser usado para verificar se o que foi digitado se trata de um numero, independente do tamanho dele(obviamente que respeitando o tamanho maximo que o tipo int pode ter)
    cont=0

    #resultado
    resultado=0
    entrada=str(input("\nValor que deseja realizar o processo de soma ponderada dos seus digitos: "))
    for i in range(len(entrada)):
      if entrada[i].isdigit():
        cont+=1
      if cont==len(entrada):
        for x in range(len(entrada)):
          resultado+=int(int(entrada[x])*(x+1))
        print("\nResultado foi: {}". format(resultado))
  except:
    print("\nOcorreu um erro durante a parte selecionada de somando digitos de forma ponderada, tente novamente mais tarde.")
    
def Somando_digitos():
  try:
    cont=0
    resultado=0
    entrada=str(input("\nValor que deseja realizar o processo de soma dos seus digitos: "))
    for j in range(len(entrada)):
      if entrada[j].isdigit():
        cont+=1
      if cont==len(entrada):
        for x in range(len(entrada)):
          resultado+=int(entrada[x])
        print("\nResultado foi: {}". format(resultado))
  except:
    print("\nOcorreu um erro durante a execucao da parte selecionada de somando digitos de um numero.")
        
while True:
  escolhido=Menu()
  if escolhido==1:
    Somando_digitos()
  elif escolhido==2:
    Somando_digitos_ponderada()
  elif escolhido==3:
    break
  else:
    print("\nDigitou algo fora das opcoes disponiveis, tente novamente mais tarde.")
