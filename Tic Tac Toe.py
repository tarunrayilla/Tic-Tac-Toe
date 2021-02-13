board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    
def match():
    
    #player1
    #horizontal match
    if(board[1]=='X' and board[2]=='X' and board[3]=='X'):
        return 1
    elif(board[4]=='X' and board[5]=='X' and board[6]=='X'):
        return 1
    elif(board[7]=='X' and board[8]=='X' and board[9]=='X'):
        return 1
    #vertical match
    elif(board[1]=='X' and board[4]=='X' and board[7]=='X'):
        return 1
    elif(board[2]=='X' and board[5]=='X' and board[8]=='X'):
        return 1
    elif(board[3]=='X' and board[6]=='X' and board[9]=='X'):
        return 1
    #diagonal match
    elif(board[1]=='X' and board[5]=='X' and board[9]=='X'):
        return 1
    elif(board[3]=='X' and board[5]=='X' and board[7]=='X'):
        return 1

    #player2
    #horizontal match
    elif(board[1]=='O' and board[2]=='O' and board[3]=='O'):
        return 2
    elif(board[4]=='O' and board[5]=='O' and board[6]=='O'):
        return 2
    elif(board[7]=='O' and board[8]=='O' and board[9]=='O'):
        return 2
    #vertical match
    elif(board[1]=='O' and board[4]=='O' and board[7]=='O'):
        return 2
    elif(board[2]=='O' and board[5]=='O' and board[8]=='O'):
        return 2
    elif(board[3]=='O' and board[6]=='O' and board[9]=='O'):
        return 2
    #diagonal match
    elif(board[1]=='O' and board[5]=='O' and board[9]=='O'):
        return 2
    elif(board[3]=='O' and board[5]=='O' and board[7]=='O'):
        return 2
    else:
        return 0

    

def game(board):
    
    print("TIC-TAC-TOE")
    print(' 1 | 2 | 3')
    print('---+---+---')
    print(' 4 | 5 | 6')
    print('---+---+---')
    print(' 7 | 8 | 9')
    total_moves=0
    player=1
    c=0

    while(True):
        if(total_moves==9 or c!=0):
            break
        if(player==1):
            n=int(input('player1:'))
            if((n>=1 and n<=9) and board[n]==' '):
                board[n]='X'
            else:
                print('Choose a valid entry!')
                continue
            print(' '+str(board[1])+' | '+str(board[2])+' | '+str(board[3]))
            print('---+---+---')
            print(' '+str(board[4])+' | '+str(board[5])+' | '+str(board[6]))
            print('---+---+---')
            print(' '+str(board[7])+' | '+str(board[8])+' | '+str(board[9]))
            player=2
        else:
            n=int(input('player2:'))
            if(board[n]!=' '):
                print('Choose a valid entry!')
                n=int(input('Player2:'))
            if(n>=1 and n<=9):
                board[n]='O'
            else:
                print('Choose a valid entry!')
                n=int(input('Player2:'))
                
            print(' '+str(board[1])+' | '+str(board[2])+' | '+str(board[3]))
            print('---+---+---')
            print(' '+str(board[4])+' | '+str(board[5])+' | '+str(board[6]))
            print('---+---+---')
            print(' '+str(board[7])+' | '+str(board[8])+' | '+str(board[9]))   
            player=1
        total_moves+=1    
        c=match()
        if(c==1):
            print('Player1 won the game!!')
        if(c==2):
            print('Player2 won the game')
game(board)            
while(True):
    ans=input('Do you want to play again?(y/n)')
    if(ans=='y'):
        board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        game(board)
    else:
        exit()
    
            
            
            
