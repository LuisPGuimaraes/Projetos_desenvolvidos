#Importar módulos
from palavras import palavras
import random

#Selecionar palavra 
def selecionar_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()


def jogar(palavra):
    palavra_a_completar= "_" * len(palavra) #_ _ _ _ 
    advinhou = False 
    letras_utilizadas = []
    palavras_utilizadas = []
    tentativas = 6

# Boas vindas ao jogador 
    print("Vamos jogar!")
    print(exibir(tentativas))
    print("Esta é a palavra: ", palavra_a_completar)
    print("A palavra tem %s letras " %len(palavra))

# Enquanto o usuário não adivinhar e ainda estiver tentativas
    while not advinhou and tentativas > 0:

        
        tentativa= input("Digite uma palavra ou letra para continuar: ").upper()
        print(tentativa)

# Tentativa de letra única
        if len(tentativa) == 1 and tentativa.isalpha():
            #Verificar se a letra ja foi utilizada
            if tentativa in letras_utilizadas:
    
                print("Você já utilizou esta letra antes %s" %tentativa)
            
            elif tentativa not in palavra:
                print("Esta letra não esta na palavra")
                tentativas = tentativas -1
                letras_utilizadas.append(tentativa)

            
            else:
                print("Acertou esta letra!")
                letras_utilizadas.append(tentativa)
                #Transformar a palavra em lista
                palavra_lista = list(palavra_a_completar)
                #Verificar onde pode substituir
                indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for indice in indices:
                    palavra_lista[indice] = tentativa

                palavra_a_completar = "".join(palavra_lista)
                
                if "_" not in palavra_a_completar:
                    advinhou = True

        # Tentativa de palavra completa 
        elif len(tentativa) == len(palavra) and tentativa.isalpha():
            
            #Palavra utilizada
            if tentativa in palavras_utilizadas:
                print("Você já tentou essa palavra")
            
            elif tentativa != palavra:
                print("A palavra esta incorreta %s " %tentativa )
                tentativas = tentativas - 1 

            else:
                advinhou = True  
                palavra_a_completar = palavra

        # Tentativa inválida 
        else:
            print("Tentativa inválida, tente novamente")

        # Exibi status do jogo 
        print(exibir(tentativas))
        print(palavra_a_completar)


    #Finaliza o jogo ou inicia outro
    if advinhou: 
        print("Parabéns! Você acertou a palavra!")

    else:
        print("Acabaram as tentativas! A palavra era %s" % palavra)

#Status do jogo - boneco
def exibir (tentativas):
    estagios = [  # Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]

    return estagios[tentativas]

#Iniciar jogo/ continuar jogando 
def iniciar():
    palavra = selecionar_palavra()
    jogar(palavra)
    #Quando acaba o jogo, verificar se o usuário quer jogar novamente
    while input("Jogar novamente? (S/N)").upper() == "S":
        palavra = selecionar_palavra()
        jogar(palavra)




iniciar()


