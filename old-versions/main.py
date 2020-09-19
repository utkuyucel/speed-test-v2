import time
import random

class Engine:
    
    def __init__(self, wordlist, kelime_sayaci):
        self.wordlist = wordlist
        self.kelime_sayaci = kelime_sayaci
        self.zaman = time.perf_counter()
        self.counter = 0 
        self.output = ""
        self.wrong_counter = 0

    def get_sentences(self):
        with open(self.wordlist, "r+", encoding = "utf-8") as f:
            x = f.readlines()
            sentence = random.choice(x)
            self.output = sentence.replace("\n", "") # Cleaning each word.
            return self.output

    def check(self):

        if (self.counter < self.kelime_sayaci):
            self.counter += 1
            self.get_sentences() # For using method from inside of Class.

        else:
            print(self.kelime_sayaci, "Adet kelime sayısına ulaşıldı") # 'Reached to max words'
            return 0 
    
    def start(self):
        self.check() # Using check method.
        while True:
            giris = input(f"{eng.output} -> ")

            if (giris == "q"):
                print(self.counter-1, "Adet doğru kelime girdiniz.") # -1 for discarding the 'q' value.
                print(self.wrong_counter, "Adet yanlış giriş yapıldı.")
                break

            if giris != eng.output:
                self.wrong_counter += 1
                continue
    
            if eng.check() == 0:
                print(self.wrong_counter, "Adet yanlış giriş yapıldı.")
                break 

if __name__ == "__main__":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while True:
        inp = int(input("Kaç adet kelime yazmak istersiniz?: ")) #How many words would you like to write?
        if inp <= 0:
            print("Kelime sayısı  0'dan küçük olamaz") #Word count can't be equal or lower than 0
            continue
        
        ch = input("Hangi dilde alıştırma yapmak istersiniz?(english | turkish): ")
        
        if (ch == "turkish" or ch == "Turkish"):
            eng = Engine("turkish.txt", inp) # Kelimeler -> Words
            eng.start()

        elif (ch == "english" or ch == "English"):
            eng = Engine("english.txt", inp)
            eng.start()

        else:
            print("HATALI GİRİŞ YAPILDI.") # Wrong/unknown input
            print("Türkçe ile devam ediliyor...") # Auto-choosing Turkish if all inputs are False.
            eng = Engine("turkish.txt", inp)
            eng.start()

        break