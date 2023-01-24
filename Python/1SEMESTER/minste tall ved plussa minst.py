t1=int(input('Tall '))
t2=int(input('Tall '))
t3=int(input('Tall '))
t4=int(input('Tall '))

minst=t1+t2+t3+t4

if t1<t2:
    minst=t1
else:
    minst=t2
if t3<minst:
    minst=t3
if t4<minst:
    minst=t4
print(minst)

