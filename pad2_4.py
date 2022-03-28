import random
import string

class Game():

    def _play(self):
        self.number_of_players()     
        if (self.players_number == 1):
          print("Wybrales 1 gracza, zacznijmy gre!")
        if self.players_number == 2:
          print("Wybrales 2 graczy, zacznijmy gre!")

    def number_of_players(self):
        players_number = 0
        while (players_number is not type(int) and players_number not in range(1,3)):           
            try:
                players_number = int(input("Wybierz liczbe graczy (maksymalnie moze byc 2 graczy)\n"))
                if(players_number not in range(1,3)):
                    print("Liczba graczy musi byc rowna 1 lub 2")
                else:
                    self.players_number = players_number
            except:
                print("Napisz liczbe graczy")

class Hangman(Game):

    def choose_word(self):
        words = ['samochod', 'walec', 'tramwaj', 'samolot', 'listonosz', 'awokado','las', 'atlas', 'utalentowany', 'komiczny', 'python', 'polska'.upper()]
        word = random.randint(1,len(words))
        return words[word]

    def __init__(self):
        super().__init__()
        print("Wybierz poziom zaawanasowania: 1 - bardzo latwy, 2 - latwy, 3 - sredni, 4 - zaawansowany")
        while True:
            try:
                self.difficulty = int(input())
            except ValueError:
                print('Wybierz inna wartosc.')
            else:
                if 1<= self.difficulty <=4:
                    break
                else:
                    print('Bledna wartosc, poziom trudnosci powinien zawierac sie w przedziale od 1 do 3.')
        if self.difficulty == 1:
            self.chances_left = 10
        elif self.difficulty == 2:
            self.chances_left = 7
        elif self.difficulty == 3:
            self.chances_left = 4
        elif self.difficulty == 4:
            self.chances_left == 2

    def _play(self):
        super()._play()
        if self.players_number == 1:
            word = self.choose_word().upper()
        else:
            print("Wpisz slowo dla drugiego gracza: ")
            word = input().upper()
        word = list(word)
        letters = []
        for i in range(0,len(word)):
            letters.append("_")
        print(F"Twoje slowo do odgadniecia to:\n{letters}")
        while True:
            try:
                print("Wpisz litere: ")
                letter = str(input()).upper()
                assert len(letter) == 1
                assert letter.isalpha()
            except AssertionError:
                print("Wpisz tylko jedna litere!\n")
            else:
                if letter in word:
                    for i in range (0,len(word)):
                        if letter == word[i]:
                            letters[i] = letter
                    
                else:
                    self.chances_left -= 1
                    print(F'Wybrana litera nie znajduje sie w slowie')
                    
            print(F"Slowo do odgadniecia:\n{letters}\nLiczba pozostalych szans wynosi: {self.chances_left}")
            if self.chances_left == 0:
                print(F'Przegrana\nSlowo do odgadniecia to: {word}')
                break
            if "_" not in letters:
                print('Wygrana! Jestes super! Gratulujemy!')
                break
            
game = Hangman()
game._play()