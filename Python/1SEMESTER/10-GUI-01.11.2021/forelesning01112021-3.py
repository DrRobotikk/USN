#Introduksjon til GUI-programmering
#Grunnstruktur
#Utvider med komponentene ledetekst, inndatafelt, utdatafelt og knapp

from tkinter import*
window=Tk()

#Vi gir vinduet et navn
window.title('Lånekalkulator billån') #Angir vinduets navn

#Vi lager ledetekster (labels) for kjøpesum, egenkapital og lånetilsagn
lbl_kjopesum=Label(window, text='Kjøpesum:')
lbl_kjopesum.grid(row=0, column=0, padx=100,pady=15)#viser hvor ordet"kjøpesum" vises

lbl_egenkapital=Label(window, text='Egenkapital:')
lbl_egenkapital.grid(row=1, column=0, padx=100, pady=15)

lbl_lanetilsagn=Label(window, text='Lånetilsagn:')
lbl_lanetilsagn.grid(row=3, column=0, padx=100,pady=15)

#Vi lager inndatafelt(innskrivningsvinduer) for kjøpesum og egenkapital.
ent_kjopesum=Entry(window, width=9)
ent_kjopesum.grid(row=0, column=1, padx=100, pady=15)

ent_egenkapital=Entry(window, width=9)
ent_egenkapital.grid(row=1, column=1, padx=100, pady=15)

#Vi lager en knapp for å beregne lånetilsagnet
btn_beregn=Button(window, text='Beregn lånetilsagn')
btn_beregn.grid(row=2, column=0, columnspan=2, pady=15)

#Vi lager et utdatafelt (visningsfelt) for konklusjonen på lånetilsagnet
ent_lanetilsagn=Entry(window, width=20, state='readonly')
ent_lanetilsagn.grid(row=3, column=1, padx=100, pady=15)

window.mainloop()
