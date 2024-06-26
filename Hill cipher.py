from tkinter import *   #char code starts at 0 ends at 94(ascii-32)

root = Tk()

root.title("Hill cipher")

root.geometry('500x500')

keyVar = StringVar()
textVar = StringVar()
outputVar = StringVar()

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
    text = text+("~"*padding)
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
    output = output[:-padding]
    outputEntry.config(state=NORMAL)
    outputEntry.delete("1.0",END)
    outputEntry.insert(END,output)
    outputEntry.config(state=DISABLED)
    return


def decode():
    text = textVar.get()



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