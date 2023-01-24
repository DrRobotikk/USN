
gutter=int(input('Antall gutter '))
jenter=int(input('Antall jenter '))
total=gutter+jenter

gutter_p=gutter/total*100
jenter_p=jenter/total*100

totalt=gutter_p+jenter_p

print(format(gutter_p,'.0f'),format(jenter_p,'.0f'),format(totalt,'.0f'))
