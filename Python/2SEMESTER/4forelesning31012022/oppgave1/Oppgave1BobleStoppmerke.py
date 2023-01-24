#tekstfil fornavn.txt
#leser navnene inn i en 1-dimensjonal tabell, linje for linje
#navnene i lista sorteres fra A til Å
#sortert liste skrives til ny fil, navn for navn fra lista
#Versjon 1: boblesortering
#Versjon 2: innstikksortering

usortert=[]
fornavnfil=open('fornavn.txt','r',encoding='utf-8')
navn=fornavnfil.readline()
while navn!='':
    navn=navn.rstrip('\n')

    usortert+=[navn]
    navn=fornavnfil.readline()
fornavnfil.close()
print('Den usorterte tabellen er',usortert)

bytte=True
s=1

while bytte==True:
    bytte=False
    for n in range(0,len(usortert)-s,1):

        if usortert[n]>usortert[n+1]:
            byttet=usortert[n]
            usortert[n]=usortert[n+1]
            usortert[n+1]=byttet
            bytte=True
    s=s+1
print(usortert)

sortertfil=open('sortert.txt','w',encoding='utf-8')

for index in range(0,len(usortert),1):
    sortertfil.write(usortert[index]+'\n')
    

sortertfil.close()
