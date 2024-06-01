import re;exec(q:=re.sub(chr(27)+'...','','''import time;((
r:="import re;exec(q:=re.sub(chr(27)+'...','',%s%s%s))" % (
chr(39)*3,q,chr(39)*3))and [(t:=time.strftime('%I:%M:%S') )
and((x:=z%60)or 1)  and((y:=z//60)or 1)  and((c:=r[x+y*60])
or 1)and print(f'{chr(27)}[7m{c}{chr(27)}[0m' if((( x%7!=1)
and 0 <x<57 and y>  1)and(int(('ODREG4'  'MW7O2VELPO27OGFE'
'G7OHBO33SW')[(ord(t[(x-2)//7])-48)*3:][:3],36)&(1<<((y-2)*
3+((x-2)%7)//2))))else c,end='')for z in range(9*60-1)] and
print('')); # Even a broken code is quine twice a day.'''))
