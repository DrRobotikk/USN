#regn ut arealet av en sirkel etter at brukeren taster inn sirkelradiussen

radius=int(input('Skriv inn radiussen her: '))

#deretter må programmet beregne arealet ved hjel av pi (3.14159)evt import math=math.pi

areal=3.14159*radius**2
print('Arealet av sirkelen er ',format(areal,'.2f'))
