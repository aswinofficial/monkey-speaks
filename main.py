from tkinter import *
from translate import Translator
from tkinter import ttk


root = Tk()
root.geometry("700x400")
root.resizable(0, 0)


def Translate():
    from_lan = str(from_lang_select.get())
    to_lang = str(to_lang_select.get())
    text = str(text_widget.get())

    translator = Translator(from_lang=str(from_lan), to_lang=str(to_lang))
    translation = translator.translate(text)

    output_label.config(text=translation)


canvas = Canvas(root, width=700, height=400, bg="#000000")
canvas.pack()

canvas.create_text(120, 40, text="Enter the text here : ",
                   font="Arial 18", fill="#FF00FF")

text_widget = Entry(canvas, fg="#4B0082", bg="#DCDCDC",
                    font="arial 16", width=35)

from_lang_select = Entry(canvas, font="arial 18",
                         fg="black", bg="grey", width=12)

to_lang_select = Entry(canvas, font="arial 18",
                       fg="black", bg="grey", width=12)


output_label = Label(canvas, text="", font="arial 12",
                     fg="#FF00FF", bg="black")


process_button = Button(canvas, fg="#FF00FF", bg="black", text="GO >>",
                        font="arial 14", relief="flat", command=Translate)


canvas.create_line(0, 150, 700, 150, dash=(4, 2), fill="#FF00FF")
canvas.create_line(0, 155, 700, 155, dash=(4, 2), fill="#FF00FF")


process_button.place(x=500, y=99)
output_label.place(x=5, y=160)
from_lang_select.place(x=12, y=100)
to_lang_select.place(x=247, y=100)
text_widget.place(x=250, y=20)
root.mainloop()
