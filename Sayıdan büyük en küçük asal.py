try : 
    girilen_sayı=int(input("Bir sayı giriniz."))
    if girilen_sayı>0 :
        if girilen_sayı==1 :
            print(2)
        elif girilen_sayı==2 :
            print(2)
        else :
            for a in range(2,girilen_sayı):
                if (girilen_sayı%a==0) :
                    girilen_sayı = girilen_sayı+1
            else:
                print(girilen_sayı)
    else:
        print(2)                
except ValueError:
    print("Lütfen bir tam sayı giriniz.")
