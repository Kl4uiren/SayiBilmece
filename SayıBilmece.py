import random
import time
def func2():
    #bu fonksiyon 0-100 arasında rasgele bir sayı belirler.
    global x
    x = random.randint(0, 101)

def func():
    cevap = input("Sayınızı Giriniz... ")
    raw_cevap = int(cevap)

    if raw_cevap > x:
        print("Daha küçük sayılar deneyebilirsin...")
        func()


    if raw_cevap < x:
        print("Daha büyük sayılar deneyebilirsin...")
        func()

    if raw_cevap == x:

        print("Kazandınız!")
        time.sleep(1)
        cevap2 = input("Devam etmek için E çıkmak için H tuşuna basabilirsiniz... ")
        if cevap2 == "H":
            print("Pekala iyi günler dilerim :)")
            time.sleep(2)
            quit()

        if cevap2 == "E":
            print("Tamamdır oyun başlıyor...")
            time.sleep(3)
            func2()
            func()

soru1 = input("Bir oyun oynamak istermisin? (E/H) ")
if soru1.lower() != "E":
    print("Tamam 0 ile 100 arasında bir sayı tuttum bakalım bilebilecekmisin...")
    time.sleep(2.5)
    func2()
    func()



















