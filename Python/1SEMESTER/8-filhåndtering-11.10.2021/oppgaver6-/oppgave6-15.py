#program som legger til kaffe i kaffe.txt fila

def main():
    ny_kaffe="ja"

    kaffefil=open('kaffe.txt','a')

    while ny_kaffe=="ja":
        print('Skriv inn informasjon om kaffe')
        kaffetype=input('Type kaffe: ')
        mengde=input('Mengde kaffe (i kg): ')

        #Add informasjon til fila
        kaffefil.write(kaffetype+'\n')
        kaffefil.write(mengde+'\n')

        #skal det legges til flere kaffeer?
        print('Vil du legge til flere typer kaffe?')
        ny_kaffe=input('Skriv "ja" for ny kaffe ')
    kaffefil.close()

main()
