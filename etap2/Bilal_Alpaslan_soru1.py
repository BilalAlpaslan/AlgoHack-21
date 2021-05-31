SKOR = 100

def toplam_op(min:int,max:int) -> int:
    global SKOR

    print()
    print("skor: ",SKOR)
    print("Bilgisayarın Tahmini: " + str((max+min) // 2) )
    y = input("Kullanıcıdan Alınacak İnput: ")
    
    if y == "1":SKOR-=1;return toplam_op( (max+min) // 2 , max)#yukarı
    elif y == "2":SKOR-=1;return toplam_op( min, (max+min) // 2 )#aşağı
    elif y == "0":return (max+min) // 2
    else:print("hatalı giriş")

def sayi(d) -> str:
    for i in range(10):
        if str(i) not in d:
            return str(i)

def tahmin(t,a,b,da,db) -> (int, int):
    global SKOR
    
    print()
    print("skor: ",SKOR)
    print("Bilgisayarın Tahmini: "+a,b)
    c1,c2 = input("Kullanıcıdan Alınacak İnput: ").split(",")
    al=[str(i) for i in a]
    
    if c1=="+++" and c2=="+++":return (a,b)
    else:
        SKOR-=1
        for i in range(3):
            if c1[i]=="+":da.append(a[i])
            elif c1[i]=="-":
                al[i]=sayi(da)
            elif c1[i]=="*":
                da.append(a[i])
                al[i]=sayi(da)
        a="".join(al)
        return tahmin(t,a,str(t-int(a)),da,db)

def main():
    toplam = toplam_op(min=204,max=1974) #sayılar min 102 max da 987 olacağından böyle ayarlanmıştır ilk orta değer 
    # print(toplam,SKOR) # debug için kullanılabilir ilk operasyon başarılı
    a,b = tahmin(toplam,str(toplam//2-53),str(toplam//2+53),[],[])
    print(a,b,SKOR)

if __name__ == '__main__':
    main()