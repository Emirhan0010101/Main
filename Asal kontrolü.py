try:
    girilen_sayı=int(input("Bir sayı giriniz."))
    if girilen_sayı>0 : 
        if (girilen_sayı==1) :
            print(girilen_sayı,"bir asal sayı değildir.")
        elif (girilen_sayı==2) :
            print(girilen_sayı,"bir asal sayıdır.")
        else :
         for a in range(2,girilen_sayı):
            if(girilen_sayı%a==0):
                print(girilen_sayı,"bir asal sayı değildir.")
                break
            else:
                print(girilen_sayı,"bir asal sayıdır.")
                break
    else :
        print("Lütfen sıfırdan büyük bir tam sayı girin.")
except ValueError:
    print("Lütfen sıfırdan büyük bir tam sayı girin.")
    