def tri(l):

    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[i]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
l = [5, 2, 9, 1]
tri(l)
print(l)