#formatering av desimaltall

pris_pr_kg=10.37
antall_kg=9.6
totalpris=pris_pr_kg*antall_kg
print('Totalprisen er:',totalpris)

dobbel_total=2*totalpris
print('Dobbel av totalpris er:',dobbel_total)

#Utskrift av totalpris avrundet til 2 desimaler
print('Totalpris er:',format(totalpris,'.2f'))
