#python 3.7.9 üzerinde test edilmiştir.
with open("oruntumatrisi.txt", "r") as f:d = [[int(j) for j in i.split()] for i in f.readlines()]
do=[int(i) for i in input().split()]
mode= 0 if do!=do[::-1] else 1
s=0
#sağdan soldan + yukarı aşağı + sol eğik çapraz
for i in range(len(d)-len(do)):
    for j in range(len(d[0])-len(do)):
        if str(d[i][j:j+len(do)])==do:s+=1
        if str(d[i][j:j+len(do)])==do[::-1]:s+=1
        # if str(d[i:i+len(do)][j])==do:s+=1
        # if str(d[i:i+len(do)][j])==do[::-1]:s+=1
        # sol çarpraz
        sc=""
        for k in range(1,len(do)+2):sc+=str(d[i:i+k][j:j+k])
        if sc==do:s+=1
        if sc==do[::-1]:s+=1

print([s,s//2][mode])