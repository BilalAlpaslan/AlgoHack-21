#python 3.7.9 üzerinde test edilmiştir.
s=""
def c(i):global s;s+=i;return i
print(*[c(i) for i in input()[::-1] if i not in s and i.isalpha()],sep="")

