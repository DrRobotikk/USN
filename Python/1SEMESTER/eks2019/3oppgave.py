#Plusse sammen to lister til en ny liste, ved ett og ett element
liste1=[1,14,26,37,100,86,77,99]
liste2=[2,13,27,38,99,85,78,101,4,47,56]
nyliste=[]

print('Liste 1 er: ',liste1)
print('Liste 2 er: ',liste2)
print('Den nye lista hittil er: ',nyliste)
print()

for index in range(0,len(liste1),1):
    nyliste+=[liste1[index]]
print('Lista etter å ha lagt inn første del er:')
print(nyliste)
print()

for index in range(0,len(liste2),1):
    nyliste+=[liste2[index]]
print('Den komplette nye lista er:')
print(nyliste)

#Index er antall elementer i ei liste;
#starter på plass 0 og går gjennom hele lista

#range er 0=plassen der lista starter;
#len=listelengde; 1=antall steg i lista


