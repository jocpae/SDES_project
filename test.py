# This function checks for the winner after every token, it is also capable of running test cases.
#How to run the testcases is described below.

m1 = [[ 0, 0 , 0, 0, 0, 0, 0], 
	 [ 0, 0, 0, 0, 0, 0, 0],
	 [ 0, 0, 0, 0, 2, 0, 0],
	 [ 0, 0, 0, 1, 2, 0, 0],
	 [ 0, 0, 1, 2, 2, 2, 0],
	 [ 0, 1, 2, 1, 1, 1, 1]] # the following matrices m1 - m4 are our default test matrices
 
m2 = [[ 0, 0 , 0, 0, 0, 0, 0],
	 [ 0, 0, 0, 0, 0, 0, 0],
	 [ 0, 0, 0, 2, 0, 0, 0],
	 [ 0, 0, 0, 2, 1, 0, 0],
 	 [ 0, 0, 0, 2, 1, 2, 1],
	 [ 0, 0, 1, 2, 1, 2, 1]]
   
m3 = [[ 0, 0 , 0, 0, 0, 0, 0],
	 [ 0, 0, 0, 0, 0, 0, 0],
	 [ 0, 0, 0, 1, 0, 0, 0],
	 [ 0, 0, 0, 1, 2, 0, 0],
	 [ 0, 0, 0, 1, 2, 0, 0],
	 [ 0, 0, 0, 1, 2, 0, 0]]

m4 = [[ 2, 1, 2, 1, 2, 1, 2],
	 [ 2, 1, 2, 1, 2, 1, 2],
	 [ 2, 1, 2, 1, 2, 1, 2],
	 [ 1, 2, 1, 2, 1, 2, 1],
	 [ 1, 2, 1, 2, 1, 2, 1],
	 [ 1, 2, 1, 2, 1, 2, 1]]
   
def creatematrix():          #this function creates the Matrix m of the form shown above, I think it should be implemented in another class
    mt = [[]]               # Or do we already have a matrix of this kind in the other classes that can be directly given to checkwinner() ?
                            # If that is the case this function will transfer the given matrix to the matrix needed for the checkwinner()-functions
        
    return mt
    
    
   
   
   
def checkwinner():           # This calls the three other functions which determine if we have a horizontal, vertical or diagonal winner, do you want to put all of them in one function? gives us less variability, as we could easily change the rules this way, e.g. deniying the players to win horizontally.     
      print "Checking for Winner."
      m = creatematrix()                #If we want to test the test cases we just put m1-m4 here instead of creatematrix().
      if checkwinnerhoritontal (m) or checkwinnervertical (m) or checkwinnerdiagonal(m):
          sys.exit()
            
def checkwinnerhorizontal (m):   # check horizontal winner function --> checks for winner and returns winner: 0,1,2
      h=0
      v=0
       
      for h in range(rows):
          for v in range(columns):
              try:
                  if (m[h][v] == 1 and m[h+1][v] == 1 and m[h+2][v] == 1 and m[h+3][v] == 1):
                      print "Player 1 wins!"
                      return 1
                      
      for h in range(rows):             #!!!!!!!!!!!!!! It says that here is an uexpected unindent.... do you have any Idea what could be the problem?
          for v in range(columns):
              try:
                  if (m[h][v] == 2 and m[h+1][v] == 2 and m[h+2][v] == 2 and m[h+3][v] == 2):
                      print "Player 2 wins!"
                      return 2
                       
                       
def checkwinnervertical (m):   # check vertical winner function --> checks for winner and returns winner: 0,1,2
     h=0
     v=0
       
     for h in range(rows):
         for v in range(columns):
             try:
                 if (m[h][v] == 1 and m[h][v+1] == 1 and m[h][v+2] == 1 and m[h][v+3] == 1):
                     print "Player 1 wins!"
                     return 1
                       
     for h in range(rows):
         for v in range(columns):
             try:
                 if (m[h][v] == 2 and m[h][v+1] == 2 and m[h][v+2] == 2 and m[h][v+3] == 2):
                     print "Player 2 wins!"
                     return 2
                      
                       
def checkwinnerdiagonal (m):   # check diagonal winner function --> checks for winner and returns winner: 0,1,2
     h=0
     v=0
       
     for h in range(rows):
         for v in range(columns):
             try:
                 if (m[h][v] == 1 and m[h+1][v+1] == 1 and m[h+2][v+2] == 1 and m[h+3][v+3] == 1):
                     print "Player 1 wins!"
                     return 1
                       
     for h in range(rows):
         for v in range(columns):
             try:
                 if (m[h][v] == 2 and m[h+1][v+1] == 2 and m[h+2][v+2] == 2 and m[h+3][v+3] == 2):
                     print "Player 2 wins!"
                     return 2
                     
  # what else does this function/class have to do?
