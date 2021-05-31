#python 3.7.9 üzerinde test edilmiştir.
def s(x:int):
    while True:
        with open("toplamlar", "a") as f2:
            n=sum([int(i) for i in str(x)])
            f2.write(str(n) + " ");p=x;x=n
        if n<10:break
    with open("toplamlar", "a") as f2:f2.write("\n")
with open("sayilar.txt", "r") as f:[s(int(i)) for i in f.readlines()]
