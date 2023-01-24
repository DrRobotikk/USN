#regn ut prosenten av antall gutter og antall jenter i en kalsse
# la oss gå ut ifra at det er 8 gutter og 12 jenter i en klasse, totalt 20 elever

gutter=int(input('Hvor mange gutter er det i klassen? '))
jenter=int(input('Hvor mange jenter er det i klassen? '))

#Nå må vi regne ut antallet i prosen, bruk formel 8:20*100

gutter_prosent=gutter/20*100
jenter_prosent=jenter/20*100



#få med totalen bare for å showe off

totalt=gutter_prosent+jenter_prosent

print('Det er',gutter_prosent,'% gutter og',jenter_prosent,'% jenter i klassen.')
print('Det er totalt',totalt,'elever i klassen')
