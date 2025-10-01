def tri_fusion(l):
    if len(l) <= 1:
        return l
    else:
        mid = len(l) // 2
        left = tri_fusion(l[:mid])
        right = tri_fusion(l[mid:])
        return fusion(left, right)
    
def fusion(g,d):
    resultat = []
    i = j = 0
    while i < len(g) and j < len(d):
        if g[i] < d[j]:
            resultat.append(g[i])
            i += 1
        else:
            resultat.append(d[j])
            j += 1
    return resultat + g[i:] + d[j:]

def recherche_dicho(l,x):
    g,d = 0, len(l)-1
    while g<=d:
        m = (g+d)//2
        if l[m] == x:
            return m
        elif l[m] < x:
            g = m+1
        else:
            d = m-1

def fibonnacci_dyn(n):
    c=[ 0 for i in range(n+1)]
    c[0] = 0
    c[1] = 1
    for i in range(2,n+1):
        if c[i] == 0:
            c[i] = c[i-1] + c[i-2]
    return c[n]


print(fibonnacci_dyn(40))
