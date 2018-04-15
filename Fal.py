import random


def fal_oyunu_switch_casi(tum_kartlar):                
    toplam_puan = [0] * 1                              
    sayac = 0
    niyet_cevap = input("Niyetinizi Tuttunuz Mu?(E/H)")
    niyet_cevap = niyet_cevap.capitalize()                              
    while not (niyet_cevap == 'E' or niyet_cevap == 'H'):
        print("Hatalı Giriş..!")
        niyet_cevap = input("Niyetinizi Tuttunuz Mu?(E/H)")
        niyet_cevap = niyet_cevap.capitalize()
    if niyet_cevap == 'E':
        kartlar_klon = tum_kartlar
        i = -1
        dizi = []
        asıl_dizi = []
        fal_oyunu( i,dizi, kartlar_klon,asıl_dizi,toplam_puan)

    elif niyet_cevap == 'H':
        sayac+=1
        main()
    if sayac ==0:
        print("Bitti, toplam puanınız: ", toplam_puan[0])
        print("Dileginizin gerceklesme olasılıgı = % ", toplam_puan[0])

def fal_oyunu(sayi,dizi,kartlar_klon, asıl_dizi,toplam_puan):

    sayaç =0
    sayi+=1

    for i in range(4):
        if len(kartlar_klon[i])==0:
            sayaç+=1

    if sayaç != 4:                               

        while (1):          

            desenler = random.randint(0, 3)                    
            if len(kartlar_klon[desenler]) !=0:
                icindeki_kart_sayisi=len(kartlar_klon[desenler])-1
                secilen_kart = random.randint(0, icindeki_kart_sayisi)
            if (len(kartlar_klon[desenler])!= 0):
                break
        secilen_kartlar=kartlar_klon[desenler][secilen_kart]
        kart_ve_degeri = secilen_kartlar.split(",")

        if (sayi != int(kart_ve_degeri[1])):

            dizi.append(secilen_kartlar)
            if sayi == 12:

                dizi = []
                print(sayi + 1, ".", kart_ve_degeri[0], "(Hiç eşleşmedi, saymaya yeniden başlanıyor...)")
                del kartlar_klon[desenler][secilen_kart]
                fal_oyunu(-1, dizi, kartlar_klon, asıl_dizi,toplam_puan)

            else:

                print(sayi + 1, ".", kart_ve_degeri[0])
                del kartlar_klon[desenler][secilen_kart]
                fal_oyunu(sayi,dizi,kartlar_klon, asıl_dizi,toplam_puan)

        if sayi == int(kart_ve_degeri[1]):
            asıl_dizi+=dizi
            dizi = []
            print(sayi + 1, ".", kart_ve_degeri[0], "((Eşleşti, saymaya yeniden başlanıyor...)")
            toplam_puan[0]+=sayi+1
            del kartlar_klon[desenler][secilen_kart]
            fal_oyunu(-1, dizi, kartlar_klon, asıl_dizi,toplam_puan)
    else:

          if(len(asıl_dizi)!=0):
                secilen_kartlar = asıl_dizi[0]
                kart_ve_degeri = secilen_kartlar.split(",")
                if (sayi != int(kart_ve_degeri[1])):
                    dizi.append(secilen_kartlar)
                    if sayi == 12:
                        dizi = []
                        print(sayi + 1, ".", kart_ve_degeri[0], "(Hiç eşleşmedi, saymaya yeniden başlanıyor...)")
                        del asıl_dizi[0]
                        fal_oyunu(-1, dizi, kartlar_klon, asıl_dizi,toplam_puan)
                    else:
                        print(sayi + 1, ".", kart_ve_degeri[0])
                        del asıl_dizi[0]
                        fal_oyunu(sayi, dizi, kartlar_klon, asıl_dizi,toplam_puan)
                if sayi == int(kart_ve_degeri[1]):
                    asıl_dizi+=dizi
                    dizi = []
                    print(sayi + 1, ".", kart_ve_degeri[0], "((Eşleşti, saymaya yeniden başlanıyor...)")
                    toplam_puan[0] += sayi + 1
                    del asıl_dizi[0]
                    fal_oyunu(-1, dizi, kartlar_klon, asıl_dizi,toplam_puan)



def main():
    tum_kartlar = [
        ["♣ As,0","♣ İki,1", "♣ Üç,2", "♣ Dört,3", "♣ Beş,4", "♣ Altı,5", "♣ Yedi,6", "♣ Sekiz,7",
         "♣ Dokuz,8", "♣ On,9", "♣ Vale,10", "♣ Kız,11", "♣ Papaz,12"],
        ["♥ As,0", "♥ İki,1", "♥ Üç,2", "♥ Dört,3", "♥ Beş,4", "♥ Altı,5", "♥ Yedi,6", "♥ Sekiz,7",
         "♥ Dokuz,8", "♥ On,9", "♥ Vale,10", "♥ Kız,11", "♥ Papaz,12"],
        ["♤ As,0", "♤ İki,1", "♤ Üç,2", "♤ Dört,3", "♤ Beş,4", "♤ Altı,5", "♤ Yedi,6", "♤ Sekiz,7",             
         "♤ Dokuz,8", "♤ On,9", "♤ Vale,10", "♤ Kız,11", "♤ Papaz,12"],
        ["♢ As,0", "♢ İki,1", "♢ Üç,2", "♢ Dört,3", "♢ Beş,4", "♢ Altı,5", "♢ Yedi,6", "♢ Sekiz,7",
         "♢ Dokuz,8", "♢ On,9", "♢ Vale,10", "♢ Kız,11", "♢ Papaz,12"]
    ]
    fal_oyunu_switch_casi(tum_kartlar)
    cikis=input("Cikmak İstediginize Emin misiniz?")        
    if cikis=='E' or cikis=='e':
         exit()
    if cikis=='H'or cikis=='h':
         main()

main()
