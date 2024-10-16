import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src/'))
import random
import string
from kataKata import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

def hangman():
    word = get_valid_word(words)
    hurufKata = set(word)
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

hangman()

