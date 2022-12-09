#Menu basico de selecao que vai retornar a opcao escolhida para o laco while
def Menu():
  try:
    print("\n-------------------------------------------------------")
    print("\n1-Soma dos digitos de um numero")
    print("\n2-Soma ponderada dos digitos de um numero")
    print("\n3-Detalhes")
    print("\n4-Sair")
    print("\n-------------------------------------------------------")
    escolha=int(input("\nEscolha uma das opcoes acima: "))
    return escolha
  except:
    print("\nDigitou algo fora das opcoes disponiveis,ou ocorreu algum erro, tente novamente mais tarde.")

#funcao de detalhes das funcoes existentes para os usuarios
def Detalhes():
  try:
    print("\n--------------------------------------------------------")
    opcao=str(input("\nDeseja detalhes de qual metodo: \n\t\t\t1-Soma dos digitos de um numero\n\t\t\t2-Soma ponderada dos digitos de um numero\n: "))
    if opcao=="1":
      print("\nA soma de digitos de um numero funciona da seguinte maneira:\n\tApos voce digitar um numero por exemplo: 23, vai se pegar cada digito do numero, nesse exemplo seriam o 2 e o 3, e somaria ambos, no caso resultado em 5")
    elif opcao=="2":
      print("\nA soma ponderada de digitos de um numero funciona da seguinte forma:\n\tApos voce digitar um numero por exemplo: 150, vai se pegar cada digito do numero, nesse caso o 1, 5 e o 0(zero), e vai primeiro multiplicar cada um deles pelo valor de sua posicao, nesse caso: \n\t1*1=1 e 5*2=10 e 0*3=0 e depois vai se somar os resultados: \n\t1 + 10 + 0 = 11")
    else:
      print("opcao nao disponivel, tente mais tarde baseado nas opcoes existentes.")
    
  except:
    print("\nOcorreu algum erro durante o detalhamento, tente novamente mais tarde.")

#funcao para realizar a soma ponderada dos digitos do numero
def Somando_digitos_ponderada():
  #o try e except para tratamento de possiveis erros ja que tem input do usuario
  try:
    #contador que vai ser usado para verificar se o que foi digitado se trata de um numero, independente do tamanho dele(obviamente que respeitando o tamanho maximo que o tipo int pode ter)
    cont=0

    #variavel que vai ser usada para guardar e ser exibida mostrando o resultado
    resultado=0

    entrada=str(input("\nValor que deseja realizar o processo de soma ponderada dos seus digitos: "))

    #percorrendo baseado no tamanho da entrada digitada pelo usuario
    for i in range(len(entrada)):

      #percorrendo para verificar se os caracteres sao digitos ou nao, se for o contador vai sendo somado
      if entrada[i].isdigit():
        cont+=1

      #caso a soma do contador seja igual ao tamanho da entrada, significa que a entrada foi um numero, entao pode executar os procedimentos
      if cont==len(entrada):
        
        #laco baseado no tamanho da entrada
        for x in range(len(entrada)):
          #a variavel resultado vai somando ponderadamente
          resultado+=int(int(entrada[x])*(x+1))
        print("\nResultado foi: {}". format(resultado))
  except:
    print("\nOcorreu um erro durante a parte selecionada de somando digitos de forma ponderada, tente novamente mais tarde.")

#funcao para realizar a soma dos digitos do numero
def Somando_digitos():
  #o try e except para tratamento de possiveis erros ja que tem input do usuario
  try:
    #contador que vai ser usado para verificar se o que foi digitado se trata de um numero, independente do tamanho dele(obviamente que respeitando o tamanho maximo que o tipo int pode ter)
    cont=0

     #variavel que vai ser usada para guardar e ser exibida mostrando o resultado
    resultado=0
    entrada=str(input("\nValor que deseja realizar o processo de soma dos seus digitos: "))
    #laco baseado no tamanho da entrada digitada pelo usuario
    for j in range(len(entrada)):
      #percorrendo para verificar se os caracteres sao digitos ou nao, se for o contador vai sendo somado
      if entrada[j].isdigit():
        cont+=1
      #caso a soma do contador seja igual ao tamanho da entrada, significa que a entrada foi um numero, entao pode executar os procedimentos  
      if cont==len(entrada):
        #laco baseado no tamanho da entrada
        for x in range(len(entrada)):
          #a variavel resultado vai somando ponderadamente
          resultado+=int(entrada[x])
        print("\nResultado foi: {}". format(resultado))
  except:
    print("\nOcorreu um erro durante a execucao da parte selecionada de somando digitos de um numero.")

#laco infinito, que vai executar algum dos metodos selecionados e so vai se encerrar quando a opcao sair for selecionada
while True:
  escolhido=Menu()
  if escolhido==1:
    Somando_digitos()
  elif escolhido==2:
    Somando_digitos_ponderada()
  elif escolhido==3:
    Detalhes()
  elif escolhido==4:
    break  
