def green(n):
    tekrar=0
    a=0
    while True:
        a+=1
        uzunluk=len(str(a))
        sonuc=a*a
        sonuc=list(str(sonuc))
        son="".join(sonuc[-uzunluk::])
        if int(a)==int(son):
            snc=a
            tekrar+=1
        if tekrar==n:
            print(snc)
            break