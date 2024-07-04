def minor(A, i, j):
    temp = A[:i] + A[i+1:]
    return [row[:j] + row[j + 1:] for row in temp]

def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]
    tempA = [[determinant(minor(A, 0, 0)), determinant(minor(A, 0, n - 1))],
             [determinant(minor(A, n - 1, 0)), determinant(minor(A, n - 1, n - 1))]]
    det = tempA[0][0] * tempA[1][1] - tempA[1][0] * tempA[0][1]
    divideVal = determinant(minor(minor(A, 0, 0), n - 2, n - 2))
    return det / divideVal

def modMatInv(A,p):      
  n=len(A)

  adj = [[0 for x in range(n)] for y in range(n)]
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(determinant(minor(A,j,i))))%p

  for i in range(0,n):
    for j in range(0,n):
        adj[i][j]=(modInv(int(determinant(A)),p)*adj[i][j])%p
  return adj

def modInv(a,p):
  for i in range(1,p):
    if (i*a)%p==1:
      return i


def encode(keyMatrix , n):
    output = ""
    keyValid = False
    text = input()
    text= text.upper()
    text=text.replace(" ","_")
    if determinant(keyMatrix)!=0:
        keyValid=True
    if (not keyValid):
        print('NO_VALID_KEY')
        return
    padding = len(text)%n
    if (padding):
        text = text+("_"*(n-padding))
    textMatrix = [[0 for x in range(n)] for y in range(int(len(text)/n))]
    textIndex=0
    for i in range(int(len(text)/n)):
        for j in range(n):
            textMatrix[i][j]=ord(text[textIndex])-65
            if (text[textIndex]=='_'):
                textMatrix[i][j]=26
            textIndex += 1
    for i in range(int(len(text)/n)):
        for j in range(n):
            temp = 0
            for r in range(n):
                temp += keyMatrix[j][r]*textMatrix[i][r]
            if (temp%27==26):
                output+='_'
            else:
                output+=chr((temp%27)+65)
    print(output)
    return

n=int(input())
keyMatrix = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    row = input()
    row = row.split(' ')
    for j in range(n):
        keyMatrix[i][j]=int(row[j])
for i in range(n):
    for j in range(n):
        if (keyMatrix[i][j]>27 or keyMatrix[i][j]<0):
            print('NO_VALID_KEY')
            exit()
keyMatrix = modMatInv(keyMatrix,27)
encode(keyMatrix,n)