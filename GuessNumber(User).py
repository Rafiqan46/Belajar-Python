import random

def computerGuessNumber(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Angka {guess} Terlalu Tinggi(H), Terlalu Rendah(L), Tebakan Benar(C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess - 1
    print(f'Yeyy Komputer Berhasil Menebak Angka Kamu {guess}')

computerGuessNumber(100)