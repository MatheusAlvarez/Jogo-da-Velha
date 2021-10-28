# Variável para definir o espaço em branco
branco = " "

#Lista do j1 e j2
token = ["X", "O"]


# Função para criar as posições do jogo da velha 
def criarBoard():
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return board


#Função para mostrar a tabela
def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if(i < 2):
            print("------")


#Função para verificar se o valor
def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if(n >= 1 and n <= 3):
            return n - 1

        else:
            print("Numero precisa estar entra 1 e 3")
            return getInputValido(mensagem)

    except:
        print("Numero nao valido")
        return getInputValido(mensagem)


#Função para verificar o movimento 
def verificaMovimento(board, i , j):
    if(board[i][j] == branco):
        return True
    else:
        return False


#Função utilizada para fazer o movimento
def fazMovimento(board, i, j, jogador):
    board[i][j] = token[jogador]



#Função para verificar o ganhador
def verificaGanhador(board):

    # Estrutura da linha
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco):
            return board[i][0]
    
    # Estrutura coluna
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco):
            return board[0][i]

    # Condição diagonal principal
    if(board[0][0] != branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

    # Condição diagonal secudario
    if(board[0][2] != branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

    #Estrutura vencedor
    for i in range(3):
        for j in range(3):
            if(board[i][j] == branco):
                return False

    return "EMPATE"
