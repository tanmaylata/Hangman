from game import Game

hangman = Game(counter=0)
def run():
    is_game_over, counter = hangman.get_winner()
    while not is_game_over and counter < 6:
        hangman.play()
        is_game_over,counter = hangman.get_winner()


if __name__ == "__main__":
    run()
    play_again = input("Play Again? y/n: ")
    if play_again == "y":
        run()
    else:
        print("Thanks for Playing! Bye!")