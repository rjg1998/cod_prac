def spiralOrder(self, A):
    Left = 0
    Right = len(A[0])-1
    Bottom = len(A)-1
    Top = 0
    direction = 0
    output = []
    while(Top <= Bottom and Left <= Right):
        if direction == 0:
            for i in range(Left , Right+1):
                output.append(A[Top][i])
            Top += 1
            
        elif direction == 1:
            for i in range(Top, Bottom+1):
                output.append(A[i][Right])
            Right = Right-1
            
        elif direction == 2:
            for i in range (Right, Left-1 ,-1):
                output.append(A[Bottom][i])
            Bottom = Bottom-1
            
        else:
            for i in range(Bottom , Top-1 , -1):
                output.append(A[i][Left])
            Left = Left+1
        direction = (direction+1)%4
    return output
