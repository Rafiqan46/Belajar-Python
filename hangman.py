import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src/'))
import random
from kataKata import kataKata

def get_valid_word(kataKata):
    kata = random.choice(kataKata)
    while '-' in kata or ' ' in kata:
        kata = random.choice(kataKata)

def hangman():
    kata = get_valid_word(kataKata)
    hurufKata = set(kata)
    alphabet = set(string.ascii_uppercase)
    hurufDigunakan = set()

    user_huruf = input('Tebak Sebuah Huruf: ').upper
    if user_huruf in alphabet - hurufDigunakan:
        hurufDigunakan.add(user_huruf)
        if user_huruf in hurufKata:
            hurufKata.remove(user_huruf)

    elif user_huruf in hurufDigunakan:
        print("Kamu Sudah Mengunnakan Karakter itu, Coba Lagi")

    else:
        print('Invalid Character, Coba Lagi!!')

user_input = input("ketik Sesuatu: ")
print(user_input)

