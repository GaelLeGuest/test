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