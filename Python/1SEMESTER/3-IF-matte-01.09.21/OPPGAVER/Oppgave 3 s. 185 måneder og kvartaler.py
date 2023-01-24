#måneder fra 1-12; deles i kvartaler
#om tallet er større enn 12, skal det bli error


måned=int(input('Skriv inn måneden i tall: '))

minst=0

if måned==0:
    print('Det finnes ingen måneder med denne verdien')
else:
    if måned<=3:
        print('Denne måneden er i det første kvartalet')
    else:
        if måned<=6:
            print('Denne måneden er i det andre kvartalet')
        else:
            if måned<=9:
                print('Denne måneden er i det tredje kvartalet')
            else:
                if måned<=12:
                    print('Denne måneden er i det fjerde kvartalet')
            


    if måned>12:
        print('Du, din luring...Det finnes kun 12 måneder i et år')
