from tkinter import *   #char code starts at 0 ends at 94(ascii-32)
import math

root = Tk()

root.title("Hill cipher")

root.geometry('500x500')

keyVar = StringVar()
textVar = StringVar()
outputVar = StringVar()




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




def encode():
    output = ""
    keyValid = FALSE
    text = textEntry.get("1.0",END)
    text = text[:-1]
    key = keyEntry.get()
    for i in range(5):
        if (len(key) == (i+1)**2):
            keyValid = TRUE
            n=i+1
    keyMatrix = [[0 for x in range(n)] for y in range(n)]
    keyIndex=0
    for i in range(n):
        for j in range(n):
            keyMatrix[i][j]=ord(key[keyIndex])-32
            keyIndex +=1
    if determinant(keyMatrix)==0:
        keyValid=FALSE
    if (not keyValid):
        outputEntry.config(state=NORMAL)
        outputEntry.delete("1.0",END)
        outputEntry.insert(END,"NO_VALID_KEY")
        outputEntry.config(state=DISABLED)
        return
    padding = len(text)%n
    if (padding):
        text = text+("~"*(n-padding))
    textMatrix = [[0 for x in range(n)] for y in range(int(len(text)/n))]
    textIndex=0
    for i in range(int(len(text)/n)):
        for j in range(n):
            textMatrix[i][j]=ord(text[textIndex])-32
            textIndex += 1
    for i in range(int(len(text)/n)):
        for j in range(n):
            temp = 0
            for r in range(n):
                temp += keyMatrix[j][r]*textMatrix[i][r]
            output+=chr((temp%95)+32)
    outputEntry.config(state=NORMAL)
    outputEntry.delete("1.0",END)
    outputEntry.insert(END,output)
    outputEntry.config(state=DISABLED)
    return


def decode():
    output = ""
    keyValid = FALSE
    text = textEntry.get("1.0",END)
    text = text[:-1]
    key = keyEntry.get()
    for i in range(5):
        if (len(key) == (i+1)**2):
            keyValid = TRUE
            n=i+1
    keyMatrix = [[0 for x in range(n)] for y in range(n)]
    keyIndex=0
    for i in range(n):
        for j in range(n):
            keyMatrix[i][j]=ord(key[keyIndex])-32
            keyIndex +=1
    if determinant(keyMatrix)==0:
        keyValid=FALSE
    if (not keyValid):
        outputEntry.config(state=NORMAL)
        outputEntry.delete("1.0",END)
        outputEntry.insert(END,"NO_VALID_KEY")
        outputEntry.config(state=DISABLED)
        return
    keyMatrix =modMatInv(keyMatrix,95)
    
    textMatrix = [[0 for x in range(n)] for y in range(int(len(text)/n))]
    textIndex=0
    for i in range(int(len(text)/n)):
        for j in range(n):
            textMatrix[i][j]=ord(text[textIndex])-32
            textIndex += 1
    for i in range(int(len(text)/n)):
        for j in range(n):
            temp = 0
            for r in range(n):
                temp += keyMatrix[j][r]*textMatrix[i][r]
            output+=chr((int(temp%95))+32)
    output = output.replace('~','')
    outputEntry.config(state=NORMAL)
    outputEntry.delete("1.0",END)
    outputEntry.insert(END,output)
    outputEntry.config(state=DISABLED)
    return



######################################## UI #########################################
keyLabel = Label(root, text="Key:")
keyEntry = Entry(root,textvariable=keyVar)

textLabel = Label(root, text="Enter Text:")
textEntry = Text(root,width=60,height=10)

encodeButton = Button(root,text="Encrypt",command=encode)
decodeButton = Button(root,text="Decrypt",command=decode)

outputEntry = Text(root,width=60,height=10,state=DISABLED)

keyLabel.pack(padx=1, pady=1)
keyEntry.pack()

textLabel.pack(padx=1, pady=1)
textEntry.pack()

encodeButton.pack(pady=10)
decodeButton.pack()

outputEntry.pack(pady=10)







root.mainloop()