import random

print('''
      
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
      
      ''')
                

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

kelimeler = [
    "araba", "kalem", "defter", "kitap", "masa", "sandalye", "okul", "kedi", "elma", "armut", "muz", "portakal", "karpuz", "deniz", "bulut",
    "ay", "hava", "su", "toprak", "orman", "insan", "erkek", "bebek", "ev", "pencere", "duvar", "anahtar", "kilit", "yatak", "yorgan", "fizik"
    "battaniye", "perde", "televizyon", "bilgisayar", "telefon", "fare", "klavye", "kamera", "kalp", "manifest", "program", "internet",
    "beyin", "dil", "burun", "el", "ayak", "bacak", "kol", "dudak", "yemek", "ekmek", "peynir", "pilav", "makarna", "tavuk", "et", "sabit"
    "yumurta", "tuz", "biber", "zeytin", "kahve", "bardak", "tabak", "saat", "para", "pantolon", "mont", "oyun", "film", "proje", "sirke"
    "resim", "renk", "cam", "balon", "defne", "evren", "yol", "top", "ada", "gezegen", "kum", "kule", "bilim", "sanat", "tarih", "gelecek",
    "zaman", "gece", "duman", "beyaz", "siyah", "mor", "mavi", "turuncu", "pembe", "gri", "kahverengi", "sanal", "hayal", "umut", "asker",
    "sevgi", "nefret", "korku", "cesaret", "mutluluk", "kader", "hayat", "hikaye", "roman", "yazar", "oyuncu", "karakter", "sahne", "senaryo",
    "enerji", "hizmet", "pazar", "ticaret", "fabrika", "makine", "motor", "elektrik", "metal", "kumanda", "robot", "veri", "kod", "algoritma", 
    "sistem", "sunucu", "dosya", "parola", "ekran", "uygulama", "uzay", "galaksi", "rota", "sinir", "nokta", "merkez", "zincir", "plan", "hedef",
    "kaynak", "hareket", "denge", "model", "seviye", "deney", "tablet", "ford", "mandalina", "metro", "balkon", "mont", "ceket", "kukla", "serap",
]

kelime = random.choice(kelimeler)
print(kelime)

can = 6

yer_tutucu= ""

for pozisyon in range(len(kelime)):
    yer_tutucu += "-"
print(yer_tutucu)

game_over = False

dogru_harfler = []
kullanilan_harfler = []
    
while not game_over:
    
    print(f"******************** {can}/6 CANINIZ KALDI ********************")
        
    tahmin = input("Lütfen bir harf giriniz: ").lower()
    
    if tahmin in kullanilan_harfler:
        print(f"\n'{tahmin}' harfini zaten kullandınız.")
        continue
    else:
        kullanilan_harfler.append(tahmin)   
    
    display = ""
    
    for harf in kelime:
        if harf == tahmin:
            display += harf
            dogru_harfler.append(harf)
        elif harf in dogru_harfler:
            display += harf
        else:
            display += "-"
        
                
    print("\n" + "=" * 25)
    print(f"  KELİME:  {display.upper()}") 
    print("=" * 25)
    
    print(f"\nKullanılan harfler: {', '.join(sorted([h.upper() for h in kullanilan_harfler]))}")
        
    if tahmin not in kelime:
        can -= 1
        print("\nBU HARF KELIMEDE YOK.\n")
        if can == 0:
            game_over = True
            print(f"******************** KAYBETTIN KELIME: {kelime.upper()} ********************")
        
    if "-" not in display:
        game_over = True
        print("******************** KAZANDIN ********************")
    
    print(hangman[6-can])
