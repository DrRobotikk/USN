liste1=[1,2,3,4,5,6,7]
liste2=[8,9,10,11,12,13,14,15,16]
nyliste=[]
print(liste1)
print(liste2)

#Lager oss variabel for listelengde
lengdeL1=len(liste1)
lengdeL2=len(liste2)

#Ny variabel for totallengde
totallengde=lengdeL1+lengdeL2

for index in range(0,totallengde,1):
    if index<lengdeL1:
        nyliste+=[liste1[index]]
    if index<lengdeL2:
        nyliste+=[liste2[index]]
print(nyliste)
