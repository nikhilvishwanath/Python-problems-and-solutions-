#Hexadecimal to decimal
n = input("Enter the number in hexadeciamal")
l = list(n)
a={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
'9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
ans = 0
for i in range(len(l)):
        ans = ans + (a[l[len(l) - 1 - i]])**(i)
if l[len(l-1) != 0:
    print(ans)
else:
    print (ans - 1)
