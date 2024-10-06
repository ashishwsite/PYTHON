def magic(n):
    # magicsqure=[][]
    # magicsquare = [[0 for _ in range(n)] for _ in range(n)]
    magicsquare=[ [0 for i in range (6)] for  i in range (6)]
    for i in range (n):
        for j in range (n):
            magicsquare[i][j]=i+j
            print(magicsquare[i][j],end=' ')
        print()    
            
          
# n=int(input("enter a number to print magic square "))
magic(3)
