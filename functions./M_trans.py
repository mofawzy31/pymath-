def M_trans(a):
    h=[[0 for i in range(len(a))] for i in range(len(a[0]))]
    for i in range(len(a[0])):
        for z in range(len(a)):
            h[i][z]=a[z][i]
    return h
