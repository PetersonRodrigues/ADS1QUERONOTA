import random

class cor:
    ROXO = '\033[1;35;48m'
    AZUL = '\033[1;34;48m'
    VERDE = '\033[1;32;48m'
    AMARELO = '\033[1;33;48m'
    VERMELHO = '\033[1;31;48m'
    BRANCO = '\033[1;30;48m'
    FIM = '\033[1;37;0m'
    AZULCALCINHA = "\33[1;36m"

def cabecalho():
    print(cor.VERMELHO+'''
                █   █       
              '''+cor.AZULCALCINHA+'''█████████   
              '''+cor.AZULCALCINHA+'''█▄█████▄█
              '''+cor.AZULCALCINHA+'''█▼▼▼▼▼▼ █
              '''+cor.AZULCALCINHA+'''█       █
              '''+cor.VERMELHO+'''█ JOGO DA FORCA >>>> SE DER 10 HUMILDE
              '''+cor.AZULCALCINHA+'''█▲▲▲▲▲▲ █
              '''+cor.AZULCALCINHA+'''█████████
              '''+cor.AZULCALCINHA+''' ██ ██'''+cor.FIM)




FORCAPAINEL = [
    '''
    |-----
    |    | 
    |    
    |    
    |     
    |   
    |
    ''',
    '''
    |-----
    |    | 
    |    O 
    |    
    |     
    |   
    |
    ''',
    '''
    |-----
    |    | 
    |    O 
    |    |
    |     
    |    
    |
    ''',
    '''
    |-----
    |    | 
    |    O 
    |   /| 
    |     
    |    
    |        
    ''',
    '''
    |-----
    |    | 
    |    O 
    |   /|\ 
    |   
    |    
    |       
    ''',
    '''
    |-----
    |    | 
    |    O 
    |   /|\ 
    |    |
    |    
    |       
    ''',
    '''
    |-----
    |    | 
    |    O 
    |   /|\ 
    |    |
    |   / 
    |    
    ''',
    '''
    |-----
    |    | 
    |    O 
    |   /|\ 
    |    |
    |   / \\
    | 
    ''']

palavras = 'bacon tijolo churrasco berinjela candango dalmata cabrito jacare '.split()

def main():

    global FORCAPAINEL
 
    letrasErradas = '' 
    letrasAcertadas = '' 
    palavraSecreta = geraPalavraAleatoria().upper()
    jogando = True
 
    while jogando: 
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
 
        palpite = recebePalpite(letrasErradas + letrasAcertadas) 
 
        if palpite in palavraSecreta: 
            letrasAcertadas += palpite
 
            if VerificaSeGanhou(palavraSecreta, letrasAcertadas): 
                print(cor.VERDE+"Parabens! A palavra secreta é "+palavraSecreta+'.! Você ganhou marreco !!'+cor.FIM)
                jogando = False
        else:
            letrasErradas += palpite 
 
            if len(letrasErradas) == len(FORCAPAINEL) - 1: 
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta) 
                print(cor.VERMELHO+'Número máximo de palpites alcansados!'+cor.FIM)
                print(cor.VERMELHO+"Depois de "+str(len(letrasErradas))+' letras erradas e '+str(len(letrasAcertadas)), end = ' '+cor.FIM)
                print(cor.VERMELHO+'palpites corretos, a palavra era '+palavraSecreta+'.'+cor.FIM)
 
                jogando = False
 
        if not jogando: 
            if JogarNovamente(): 
                letrasErradas = ''
                letrasAcertadas = '' 
                jogando = True
                palavraSecreta = geraPalavraAleatoria().upper() 
                
def geraPalavraAleatoria():
    
    global palavras
    return random.choice(palavras)

def imprimeComEspacos(palavra):
   
    for letra in palavra:
        print(letra, end = ' ')
 
    print()
 
def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    
    global FORCAPAINEL 
    print(FORCAPAINEL[len(letrasErradas)]+'\n')  
 
    print("Letras Erradas:", end = ' ') 
    imprimeComEspacos(letrasErradas) 
 
    vazio = '_'*len(palavraSecreta)
    for i in range(len(palavraSecreta)): 
        if palavraSecreta[i] in letrasAcertadas: 
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:] 
 
    imprimeComEspacos(vazio)

def recebePalpite(palpiteFeitos):


    while True:
        palpite = input('Chute uma letra. \n').upper() 
        
        if len(palpite) != 1: 
            print('Coloque uma unica letra')
        elif palpite in palpiteFeitos: 
            print('Voce ja digitou essa letra, digite de novo!')
        elif not 'A' <= palpite <= 'Z':
            print('Escolha Somente uma letra!')
        else:
            return palpite  

def JogarNovamente():
    
    return input("Voce quer jogar novamente? (sim ou nao)\n").upper().startswith('S')
 
def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    
    ganhou = True
    for letra in palavraSecreta: 
        if letra not in letrasAcertadas: 
            ganhou = False 
            break 
 
    return ganhou 
cabecalho()

main()