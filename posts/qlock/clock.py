import datetime as d
import datetime as D
import time

#t = d.datetime.now().isoformat()[11:19]
t = time.strftime('%H:%M:%S')
e = [31599,18724,29671,31207,18925,31183,31695,18727,31727,31215,1040]

print(t)
print('---')
for y in range(5):
    for x in range(8*4):
        l = x % 4 == 3
        if l:
            print(' ', end='')
            continue
        d = e[ord(t[x//4])-48]
        p = d & (1 << (y*3+(x%4)))
        print('**' if p else '  ', end='')
    print('')

print('---')
r=('abcde'*15)[:59]
r='\n'.join([r]*9) + '\n'
print(r, end='')

print('---')
for z in range(9*60):
    x = z % 60
    y = z // 60
    c = r[x+y*60]
    if x % 7 != 1 and 0 < x < 57 and y>1:
        d = e[ord(t[(x-2)//7])-48]
        d = int('ODREG4MW7O2VELPO27OGFEG7OHBO33SW'[(ord(t[(x-2)//7])-48)*3:][:3],36)
        p = d & (1 << ((y-2)*3+((x-2)%7)//2))
        print(f'{chr(27)}[7m{c}{chr(27)}[0m' if p else c, end='')
    else:
        print(c, end='')

print('---')
[(t:=time.strftime('%H:%M:%S'))and((x:=z%60)or 1)and((y:=z//60)or 1)and((c:=r[x+y*60])or 1)and print(f'{chr(27)}[7m{c}{chr(27)}[0m' if ((x%7!=1 and 0<x<57 and y>1)and(int('ODREG4MW7O2VELPO27OGFEG7OHBO33SW'[(ord(t[(x-2)//7])-48)*3:][:3],36)&(1<<((y-2)*3+((x-2)%7)//2))))else c,end='')for z in range(9*60)]
