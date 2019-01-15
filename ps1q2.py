

def bsearch(l,v):
    L = 0
    R = len(l) - 1
    if l[0] > v :
        return -1
    if l[R]< v:
        return R
    while(L < R):
        m = (L + R)//2
        if l[m] == v :
            return m
        if l[m] < v :
            L = m + 1
        else:
            R = m - 1
    if L == R :
        return L

def bleft(l,v):
    i = bsearch(l,v)

    while l[i] >= v and i != -1 :
        i = i - 1
    return i

def bcount(l,v):
    i = bleft(l,v) + 1
    count = 0
    while  i < len(l) and l[i]==v :
        count = count + 1
        i = i + 1
    return count
