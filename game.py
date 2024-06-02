from board import Board

class Game:
    def __init__(self, counter: int) -> None:
        self.word = self.get_target_word()
        self.board = Board(self.word)
        self.counter = counter
        self.win = False

    def get_target_word(self):
        word = input("Please Enter The Target Word: ")
        return word

    def get_player_guess(self):
        guess = input("what's your guess? ")
        while not guess.isalpha():
            print("Invalid Value! Please enter an alphabet: ")
            guess = input("what's your guess")
        return guess
    
    def get_winner(self):
        return self.win, self.counter
    
    def play(self):
        guess = self.get_player_guess()
        chances_over = False
        while not self.board.is_guess_in_word(guess):
            self.counter += 1
            if self.counter == 6:
                print("You Loose!")
                chances_over = True
                break
            print(f"Your Guess is not in the Target Word! You have {6- self.counter} chances left!")
            guess = self.get_player_guess()
            
        if chances_over:
            self.win = False
            return
                        
        current_word = self.board.print_board(guess)
        print(f"current status: {current_word}")

        if self.counter == 6 and current_word != self.word:
            print("You Loose!")
            return
        
        elif self.counter == 6 and current_word == self.word:
            print("You Win!")
            self.win = True
            return

        elif self.counter < 6 and current_word == self.word:
            print("You Win!")
            self.win = True
            return 
        
        else:
            return
        


