## 1. ASCII 2 Binary converter


inp = input("Entered String : ")
print(inp)
bin = []
for i in inp:
    st = ''
    j=int(ord(i))
    if j==1:
        print('00000001')
    elif j==0:
        print('00000000') 
    while j>=2:
        a = j%2
        st = str(a) + st
        j//=2
        if j==1:
            st = '1' + st
            while len(st)<8:
                st = '0' + st
            bin.append(st)
            break
z = '        '.join(bin)
print("\n",z,sep='')

## 2. Binäry 2 ASCII...

inp = input("Entered String : ")
print(inp)
bin = []
for i in inp:
    st = ''
    j=int(ord(i))
    if j==1:
        print('00000001')
    elif j==0:
        print('00000000') 
    while j>=2:
        a = j%2
        st = str(a) + st
        j//=2
        if j==1:
            st = '1' + st
            while len(st)<8:
                st = '0' + st
            bin.append(st)
            break
z = '        '.join(bin)
print("\n",z,sep='')

#END