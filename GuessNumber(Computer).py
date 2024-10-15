import random

def guessNumber(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Silahkan Tebak Angka Antara 1 Dan {x}: "))
        if guess < randomNumber:
            print("Tebakan Terlalu Rendah, Coba Lagi!!")
        elif guess > randomNumber:
            print("Tebakan Terlalu Tinggi, Coba Lagi!!")
        
    print(f"Tebakan Anda Benar, Angka Rahasinya Adalah {randomNumber}")

guessNumber(10)