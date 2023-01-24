
from tkinter import*
#Her oppretter vi en def for selve beregninga av lånekalkulatoren
#Denne beregninga må hentes inn (command) i "button-funksjonen"
def beregn_lan():
    if (int(egenkapital.get())/int(kjopesum.get()))>=0.35:
        lanetilsagn.set('Lån innvilges')
    else:
        lanetilsagn.set('Lån innvilges ikke')


window=Tk()

#Gir vinduet et navn
window.title('Lånekalkulator billån')

#Lager ledetekster (labels) for kjøpesum, egenkapital og lånetilsagn
lbl_kjopesum=Label(window, text='Kjøpesum:')
lbl_kjopesum.grid(row=0, column=0, padx=100,pady=15)#grid viser plassering for ordet"kjøpesum"

lbl_egenkapital=Label(window, text='Egenkapital:')
lbl_egenkapital.grid(row=1, column=0, padx=100, pady=15)

lbl_lanetilsagn=Label(window, text='Lånetilsagn:')
lbl_lanetilsagn.grid(row=3, column=0, padx=100,pady=15)

#Vi lager inndatafelt(innskrivningsvinduer) for kjøpesum og egenkapital.

kjopesum=StringVar()
ent_kjopesum=Entry(window, width=9, textvariable=kjopesum)
ent_kjopesum.grid(row=0, column=1, padx=100, pady=15)

egenkapital=StringVar()
ent_egenkapital=Entry(window, width=9, textvariable=egenkapital)
ent_egenkapital.grid(row=1, column=1, padx=100, pady=15)

#Lager en knapp for å beregne lånetilsagnet
btn_beregn=Button(window, text='Beregn lånetilsagn',command=beregn_lan)#Her henter vi inn def beregn_lan
btn_beregn.grid(row=2, column=0, columnspan=2, pady=15)

#Lager et utdatafelt (visningsfelt) for konklusjonen på lånetilsagnet
lanetilsagn=StringVar()
ent_lanetilsagn=Entry(window, width=17, state='readonly', textvariable=lanetilsagn)
ent_lanetilsagn.grid(row=3, column=1, padx=100, pady=15)

#en knapp for å avslutte vinduet
btn_avslutt=Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=4, column=0, columnspan=2, pady=15)

window.mainloop()

#Arbeidsliste:

#1) Samle definisjon av ledetekst, komponent og variabel for de som hører sammen
#2) Bruke lokale variable på get'ere og set'ere
#   eks. ek=int(egenkapital.get())

