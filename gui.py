# Python program to implement Morse Code Translator
from tkinter import *
'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
            # 1 space indicates different characters
			# and 2 indicates different words
            cipher += ' '
    textbox2.delete("0","end")
    textbox2.insert("end",cipher)

# Function to decrypt the string
# from morse to english
def decrypt(message):

    # extra space added at the end to access the
	# last morse code
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:

            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
                citext = ''
    textbox2.delete("0", "end")
    textbox2.insert("end",decipher)
def table():
    win = Tk()
    win.geometry("600x320")
    win.title("Morse Code Table")
    win.configure(bg = "black")
    win.resizable(0,0)
    table_txt = ""
    index = 1
    for key in MORSE_CODE_DICT:
        value = MORSE_CODE_DICT[key]
        table_txt += key+" = "+value+"   "
        index+= 1
        if index%5 == 0:
            table_txt += "\n"

    label2 = Label(win, text=table_txt, border=5, font="time 20 bold", fg="white",
                       bg="black")
    label2.pack()

def clear():
    textbox2.delete("0","end")

root = Tk()
root.title("Morse Code Converter")
root.geometry("1900x900")

# FOR GIVING BACKGROUND COLOR root['background']='#95EB78' IS USED
background = PhotoImage(file="background.ppm")
label = Label(root, image=background)
label.pack()

black = PhotoImage(file="black.ppm")
label = Label(root, image=black)
label.place(x=420, y=50)

# padx and pady give space to vertical and horizontal line
border_color_lab2 = Frame(root, background="white")
label2 = Label(border_color_lab2, text="Morse Code Converter", border=5, font="time 20 bold", fg="white", bg="black")
label2.pack(padx=1, pady=1)
border_color_lab2.place(x=620, y=100)

border_color_lab1 = Frame(root, background="white")
label1 = Label(border_color_lab1, text="Enter your text for converting ", border=5, font="time 15 bold", fg="white",
               bg="black")
label1.pack(padx=1, pady=1)
border_color_lab1.place(x=450, y=200)

border_color_lab3 = Frame(root, background="white")
label3 = Label(border_color_lab3, text="       Convert into Morse code                  ", border=5,
               font="time 15 bold", fg="white", bg="black")
label3.pack(padx=1, pady=1)
border_color_lab3.place(x=680, y=280)

border_color_lab3 = Frame(root, background="white")
label3 = Label(border_color_lab3, text="       Convert to text                                 ", border=5,
               font="time 15 bold", fg="white", bg="black")
label3.pack(padx=1, pady=1)
border_color_lab3.place(x=680, y=350)

border_color_lab3 = Frame(root, background="white")
label3 = Label(border_color_lab3, text="          Morse code Table                         ", border=5,
               font="time 15 bold", fg="white", bg="black")
label3.pack(padx=1, pady=1)
border_color_lab3.place(x=680, y=420)

textbox1 = Entry(root, fg='black',bg="white",border=3, font=('Arial', 20))
textbox1.place(x=780, y=200)
textbox1.focus()

button_border = Frame(root, highlightbackground="white",
                      highlightthickness=2, bd=0)
button1 = Button(button_border, text=" ", padx=20, pady=6, border=0, bg="black",fg="white",command=lambda : encrypt(textbox1.get().upper()))
button1.pack()
button_border.place(x=600, y=280)

button_border = Frame(root, highlightbackground="white",
                      highlightthickness=2, bd=0)
button1 = Button(button_border, text=" ", padx=20, pady=6, border=0, bg="black",fg="white",command=lambda : decrypt(textbox1.get()))
button1.pack()
button_border.place(x=600, y=350)

button_border = Frame(root, highlightbackground="white",
                      highlightthickness=2, bd=0)
button1 = Button(button_border, text=" ", padx=20, pady=6, border=0, bg="black",fg="white",command=table)
button1.pack()
button_border.place(x=600, y=420)

textbox2 = Entry(root, fg='black',bg="white",border=0, font=('Arial', 20),width=20)
textbox2.place(x=630, y=550)
textbox2.focus()

button_border = Frame(root, highlightbackground="white",
                      highlightthickness=2, bd=0)
button1 = Button(button_border, text="Clear", padx=20, border=0, bg="black",fg="white",font="time 12 bold",command=clear)
button1.pack()
button_border.place(x=950, y=550)

root.mainloop()
#Here ppm stands for Portable Pixmap Format
#frame:meansif we increse the hight of frame the the  inner things  in it like buttons,labels size willl also increase.