from tkinter import *
from sys import *
from tkinter import filedialog
from time import *
import string
#edited locally
#edited online
time = ""
def currentTime():
    codedTime = str(ctime())
    codedTime = codedTime.replace(" ", "_")
    codedTime = codedTime.replace(":", "-")
    return(codedTime)


window = Tk()
window2 = Tk()
window2.geometry("100x300")
Cypherable = "abcdefghijklmnopqrstuvwxyz0123456789"
global finalstring
finalstring = "hold"
window2.resizable(TRUE, FALSE)
window.resizable(FALSE, FALSE)
#-------------------------------------------------------------------------
#Defining cypher function
def cypher(key, string1):
    global finalstring
    finalstring = ""
    #length of the string
    string1Len = len(string1)
    #loops as many times as there are characters in string1
    for i in range(string1Len):
        letterInIndexLocation = Cypherable.find(string1[i])
        if string1[i] in Cypherable:
            maxindex = len(Cypherable) - 1
            if (letterInIndexLocation + key) > maxindex:
                letterInIndexLocation = ((letterInIndexLocation + key) % (maxindex +1))
            else:                letterInIndexLocation += key
            finalstring = finalstring + (Cypherable[letterInIndexLocation])
            #countForLetter +=1
        else:
            finalstring = finalstring + (string1[i])
            #countForLetter +=1
    outputs.config(text=finalstring)
#------------------------------------------------------------------------
#Defining decypher function
def decypher(key, string1):
    global finalstring
    string1Len = len(string1)
    finalstring = ""
    #the maximum index of the cypherable
    maxindex = len(Cypherable) - 1
    #loops as many times as there are characters in string1
    for i in range(string1Len):
        #Finds the letter in the string in the cypherable letters
        letterInIndexLocation = Cypherable.find(string1[i])
        #if the letter is able to be cyphered, it gets cyphered
        if string1[i] in Cypherable:
            key %= (maxindex + 1)
            if (letterInIndexLocation - key) < 0:
                letterInIndexLocation = (letterInIndexLocation - key) + (maxindex + 1)
            else:
                letterInIndexLocation -= key
            finalstring = finalstring + (Cypherable[letterInIndexLocation])
        #if the character is not able to be cyphered, just prints the normal character
        else:
            finalstring = finalstring + (Cypherable[letterInIndexLocation])
    outputs.config(text=finalstring)
#Chooses between Cyphering or De-Cyphering
def encodeButton():
        #Gets string to cypher
        x = stringInput.get().lower()
        #Gets cypher key from user
        y = int(keyInput.get())
        #Count for printing 
        countForLetter = 0
        #Prints reconstructed string
        #Executes cypher function
        cypher(y, x)
def decodeButton():
        #Gets string to cypher
        x = stringInput.get().lower()
        #Gets cypher key from user
        y = int(keyInput.get())
        #Count for printing 
        countForLetter = 0
        #Prints reconstructed string
        #Executes cypher function
        decypher(y, x)
#-----------
def writeCypher():
        with open(currentTime()+".txt", "w") as sWrite:
            sWrite.write(finalstring)
        sWrite.close()

label1 = Label(window, text="Basic Caesar's Cipher", width=50, bg="lightgray")
label1.grid(row=0, column=0)
#Input Boxes
inputFrame = Frame(window)
title1 = Label(inputFrame, text="String Input", width=50)
title2 = Label(inputFrame, text="Key Input", width=50)
stringInput = Entry(inputFrame, width=50, bg="lightgray")
keyInput = Entry(inputFrame, width = 50, bg="lightgray")
title1.grid(row=0, column=0)
stringInput.grid(row=1, column=0)
title2.grid(row=2, column=0)
keyInput.grid(row=3, column=0)
inputFrame.grid(row=1, column=0)
#Button Boxes
def set_text(text):
    stringInput.delete(0,END)
    stringInput.insert(0,text)
    return
def browseFiles():
    try:
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("Text files",
                                                            "*.txt*"),
                                                           ("all files",
                                                            "*.*")))

        datafile = open(filename, "r")
        data = datafile.read()
        datafile.close()
        set_text(data)
        return data
    except:
        pass

frame1 = Frame(window)
encodeButton = Button(frame1, text="encode", width=25, command=encodeButton)
decodeButton = Button(frame1, text="decode", width=25, command=decodeButton)
encodeButton.grid(row=0, column=0)
decodeButton.grid(row=0, column=1)
saveButton = Button(frame1, text="Save Cypher To File", width=25, fg="black", bg="lightgray", command=writeCypher)
openButton = Button(frame1, text="Open Cypher Text File", width=25, fg="black", bg="lightgray",command=browseFiles)
saveButton.grid(row=1, column = 0)
openButton.grid(row=1, column = 1)
frame1.grid(row=2, column=0)
#Window 2 / Output Text
outputTitle = Label(window2, text="Outputs", bg="lightgray")
outputs = Label(window2, text="")
outputTitle.pack()
outputs.pack()
window2.mainloop()
window.mainloop()