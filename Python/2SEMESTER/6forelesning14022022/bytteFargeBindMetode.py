#PRG1100-2022-Bind-metode

from tkinter import *

def bytt_farge(event):
    if ent_navn["fg"]=="blue":
        ent_navn["fg"]="red"
    else:
        ent_navn["fg"]="blue"

vindu=Tk()
vindu.title("Inndatafelt og fargevalg")

ent_navn=Entry(vindu,fg="blue")
ent_navn.grid(padx=100,pady=15)
ent_navn.bind("<Button-3>",bytt_farge)

vindu.mainloop()
