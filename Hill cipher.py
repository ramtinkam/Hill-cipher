from tkinter import *   #char code starts at 0 ends at 93(ascii-33)

root = Tk()

root.title("Hill cipher")

root.geometry('300x300')

key = StringVar()
text = StringVar()
output = StringVar()

keyLabel = Label(root, text="Key:")
keyEntry = Entry(root,textvariable=key)

textLabel = Label(root, text="Enter Text:")
textEntry = Entry(root,textvariable=text)

encodeButton = Button(root,text="Encode",command=encode)
decodeButton = Button(root,text="Decode",command=decode)

outputEntry = Entry(root,textvariable=output,state=DISABLED)

keyLabel.pack(padx=1, pady=1)
keyEntry.pack()

textLabel.pack(padx=1, pady=1)
textEntry.pack()

encodeButton.pack(pady=10)
decodeButton.pack()

outputEntry.pack(pady=10)







root.mainloop()