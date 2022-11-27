from tkinter import *
from tkinter import filedialog


def saveDoc():
    global textarea
    text = textarea.get("1.0", "end-1c")
    location = filedialog.asksaveasfilename()
    file = open(location, "w+")
    file.write(text)
    file.close()


def courier():
    global textarea
    textarea.config(font=('Courier', 16))


def cambria():
    global textarea
    textarea.config(font=("Cambria", 16))


def helvetica():
    global textarea
    textarea.config(font=("Helvetica", 16))


def italic():
    global textarea
    textarea.config(font=("Times", 16, "bold italic"))


def boldDoc():
    global textarea
    textarea.config(font=('arial', 16, 'bold'))


window = Tk()
window.title("Text Editor From Avtex")
window.configure(background="white")

save_button = Button(window, command=saveDoc, text="Save")
save_button.grid(row=1, column=0)
save_button.config(font=('arial', 20, 'bold'), bg="DodgerBlue2", fg="black")

font_button = Menubutton(window, text="Font")
font_button.config(font=('arial', 20, 'bold'), bg="DodgerBlue2", fg="black")
font_button.grid(row=1, column=1)
font_button.menu = Menu(font_button, tearoff=0)
font_button["menu"] = font_button.menu

font_button.menu.add_checkbutton(label="Cambria",
                                 command=cambria)

font_button.menu.add_checkbutton(label="Courier",
                                 command=courier)
font_button.menu.add_checkbutton(label="Italic",
                                 command=italic)
font_button.menu.add_checkbutton(label="Helvetica",
                                 command=helvetica)

bold_button = Button(window, command=boldDoc, text="Bold")
bold_button.grid(row=1, column=2)
bold_button.config(font=('arial', 20, 'bold'), bg="DodgerBlue2", fg="black")

textarea = Text(window)
textarea.grid(row=2, columnspan=5)

if __name__ == "__main__":
    mainloop()

