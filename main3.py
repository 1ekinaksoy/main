# Kullanıcı giriş paneli tasarlayınız

"""
Kullanıcıadı/Email ve şifre ile giriş sağlanacak
     Giriş başarılı ise ekrana "Giriş Başarılı" yazsın
     Değilse
        Kullanıcıya kayıt olmak ister misiniz?
           Hayır ise PEKİ!!!
           Evet ise kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                şifre ve şifretekrarının aynı olması
"""


kullanici_adi: str = "aksoyekin"
email: str = "info@aksoyekin.net"
sifre: str = "123555"

print("----------GİRİŞ PANELİ----------")

username_or_email: str = input("Lütfen kullanıcı adınızı veya e-posta adresinizi giriniz: ")
password: str = input("Lütfen şifrenizi giriniz: ")

if (kullanici_adi == username_or_email or email == username_or_email) and (password == sifre):
    print("Giriş Başarılı !")
else:
    cevap: str = input("Kayıt olmak ister misiniz ?(E/H): ")
if cevap == "H":
    print("Teşekkürler")
elif cevap == "E":
    ad: str = input("Adınız: ")
    soyad: str = input("Soyadınız: ")
    email: str = input("E-Posta: ")
    sifren: str = input("Şifreniz: ")
    sifren_tekrar: str = input("Şifre Tekrar: ")

    if sifren == sifren_tekrar:
        print("Hoş Geldiniz !")
    else:
        print("Şifreleriniz birbiriyle uyuşmuyor")