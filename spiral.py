def make_spiral(matrix):
    #output = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    #some variables
    top = 0
    left = 0
    bottom = len(matrix)
    right = len(matrix)
    
    while top < bottom and left < right:

        # Work on the top row now
        for j in range(left,right):
            #output[top][j] = matrix[top][j]
            print(matrix[top][j])
        top += 1
        #print(output)
        # Top row is done!

        # Work on the last column now
        for i in range(top,bottom):
            #output[i][right-1] = matrix[i][right-1]
            print(matrix[i][right-1])
        right -= 1
        #print(output)
        # Last column is done!

        #Work on the last row now!
        for j in range(right-1,left-1,-1):
            #output[bottom-1][j] = matrix[bottom-1][j]
            print(matrix[bottom-1][j])
        bottom -= 1
        #print(output)
        # Last column is done!

        #Work on the first column now!
        for i in range(bottom-1,top-1,-1):
            #output[i][left] = matrix[i][left]
            print(matrix[i][left])
        left += 1
        #print(output)
        #Last column done!

    #return output

#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#print(make_spiral(matrix))