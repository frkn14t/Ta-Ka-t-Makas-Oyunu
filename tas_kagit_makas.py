import random

def tas_kagit_makas_ADINIZ_SOYADINIZ():
    # Karşılama mesajı
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyun kuralları: Taş, kağıt veya makas seçin. İlk iki turu kazanan oyunu kazanır.")
    print("Oyun devam etmek istiyor musunuz? Oyundan çıkmak için 'Hayır' yazın.")

    while True:
        # Oyun sayaçları
        oyun_sayisi = 1
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0
        secenekler = ["taş", "kağıt", "makas"]

        # Oyun döngüsü
        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            print(f"\nOyun {oyun_sayisi}:")
            oyuncu_secimi = input("Lütfen seçiminizi yapın (taş, kağıt, makas): ").lower()

            # Geçerli seçim kontrolü
            if oyuncu_secimi not in secenekler:
                print("Geçersiz seçim! Lütfen tekrar deneyin.")
                continue

            # Bilgisayarın rastgele seçimi
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            # Kazananı belirle
            if oyuncu_secimi == bilgisayar_secimi:
                print("Beraberlik!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Oyuncu kazandı!")
                oyuncu_galibiyetleri += 1
            else:
                print("Bilgisayar kazandı!")
                bilgisayar_galibiyetleri += 1

            oyun_sayisi += 1

        # Oyun galibi
        if oyuncu_galibiyetleri == 2:
            print("\nTebrikler! Oyunu kazandınız!")
        else:
            print("\nBilgisayar oyunu kazandı!")

        # Tekrar oynamak ister misiniz?
        tekrar = input("Tekrar oynamak ister misiniz? (Evet/Hayır): ").lower()
        if tekrar != "evet":
            print("Oyun bitti. Teşekkürler!")
            break

tas_kagit_makas_ADINIZ_SOYADINIZ()