#PRG1100-2022-scrollbar

from tkinter import *

window=Tk()
window.title('Scrollbar')

y_scroll=Scrollbar(window,orient=VERTICAL)
y_scroll.grid(padx=100,pady=15)

window.mainloop()
