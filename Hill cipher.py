from tkinter import *   #char code starts at 0 ends at 94(ascii-32)
import math

root = Tk()

root.title("Hill cipher")

root.geometry('500x500')

keyVar = StringVar()
textVar = StringVar()
outputVar = StringVar()


import numpy
import math
from numpy import matrix
from numpy import linalg

def modMatInv(A,p):      
  n=len(A)
  A=matrix(A)
  adj=numpy.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):
  A=numpy.array(A)
  minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor




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
    if (not keyValid):
        outputEntry.config(state=NORMAL)
        outputEntry.delete("1.0",END)
        outputEntry.insert(END,"NO_VALID_KEY")
        outputEntry.config(state=DISABLED)
        return
    keyMatrix = [[0 for x in range(n)] for y in range(n)]
    keyIndex=0
    for i in range(n):
        for j in range(n):
            keyMatrix[i][j]=ord(key[keyIndex])-32
            keyIndex +=1
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
    if (not keyValid):
        outputEntry.config(state=NORMAL)
        outputEntry.delete("1.0",END)
        outputEntry.insert(END,"NO_VALID_KEY")
        outputEntry.config(state=DISABLED)
        return
    keyMatrix = [[0 for x in range(n)] for y in range(n)]
    keyIndex=0
    for i in range(n):
        for j in range(n):
            keyMatrix[i][j]=ord(key[keyIndex])-32
            keyIndex +=1
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