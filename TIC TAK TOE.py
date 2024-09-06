''' GAMES USING PYTHON (TIC TAK TOE !!!)'''

# TIC TAK TOE!!!!

a=[[1,2,3],[4,5,6],[7,8,9]]
c=1
cho='d'
p1=input("enter the choice of player no:1 - 'X' or 'O':")
p1=p1.upper()
if p1=='X':
    p2='O'
else:
    p2='X'

while cho=='d':
    if c==1:
        for i in range(0,3):
            for j in range(0,3):
                print('|_',a[i][j],'_|',end='')
            print()

# FOR PLAYER NO:01

    p=int(input("enter the number where u want to place x or o by player no:01 :"))
    for i in a:
        for j in i:
            if j==p:
                i.insert(i.index(j),p1)
                del i[i.index(j)]
                break
    for i in range(0,3):
        for j in range(0,3):
            print('|_',a[i][j],'_|',end='')
        print()
    if (a[0][0]==a[0][1]==a[0][2]==p1) or (a[1][0]==a[1][1]==a[1][2]==p1) or (a[2][0]==a[2][1]==a[2][2]==p1) or (a[0][0]==a[1][0]==a[2][0]==p1) or (a[0][1]==a[1][1]==a[2][1]==p1) or (a[0][2]==a[1][2]==a[2][2]==p1) or (a[0][0]==a[1][1]==a[2][2]==p1) or (a[0][2]==a[1][1]==a[2][0]==p1):
        cho='w'
    if cho=='w':
        print("The player no:01 had won!!") 
        break
    if c==5:
        print("The match is a DRAW!!")
        break
    
# FOR PLAYER NO:02

    h=int(input("enter the number where u want to place x or o by player no:02 :"))
    for i in a:
        for j in i:
            if j==h:
                i.insert(i.index(j),p2)
                del i[i.index(j)]
                break
    for i in range(0,3):
        for j in range(0,3):
            print('|_',a[i][j],'_|',end='')
        print()
    if (a[0][0]==a[0][1]==a[0][2]==p2) or (a[1][0]==a[1][1]==a[1][2]==p2) or (a[2][0]==a[2][1]==a[2][2]==p2) or (a[0][0]==a[1][0]==a[2][0]==p2) or (a[0][1]==a[1][1]==a[2][1]==p2) or (a[0][2]==a[1][2]==a[2][2]==p2) or (a[0][0]==a[1][1]==a[2][2]==p2) or (a[0][2]==a[1][1]==a[2][0]==p2):
        cho='w'
    if cho=='w':
        print("The player no:02 had won!!")
    c=c+1