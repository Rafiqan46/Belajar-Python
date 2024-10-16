import random

def play():
    user = input("Silahkan Pilih!\n(B) Untuk Batu, (K) Untuk Kertas, (G) Untuk Gunting.\n--> ").lower()
    computer = random.choice(['b', 'k', 'g'])

    if user == computer:
        return 'Seri'
    
    if is_win(user, computer):
        return 'Kamu Menang!!'
    
    if is_win(computer, user):
        return 'Kamu Kalah -_-'
    
def is_win(player, opponent):
    if (player == 'b' and opponent == 'g') or (player == 'k' and opponent == 'b') or (player == 'g' and opponent == 'k'):
        return True
    
print(play())