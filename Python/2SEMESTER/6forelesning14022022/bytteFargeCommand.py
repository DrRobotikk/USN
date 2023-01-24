#PRG1100-2022-command-argument

from tkinter import *

def bytt_farge():

    if btn_byttfarge['fg']=='blue':
        btn_byttfarge['fg']='red'
    else:
        btn_byttfarge['fg']='blue'

vindu=Tk()
vindu.title('Knapp for fargevalg')

btn_byttfarge=Button(vindu,text='Bytt farge',fg='blue',command=bytt_farge)
btn_byttfarge.grid(padx=100,pady=15)

vindu.mainloop()
