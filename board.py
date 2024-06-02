from collections import defaultdict

class Board:
    def __init__(self, word) -> None:
        self._word = word
        self._state = ['_']* len(self._word)
        self._word_dict = self.word_dict()

    def word_dict(self):
        word_dict = defaultdict(list)
        for idx, val in enumerate(self._word):
            word_dict[val].append(idx)
        return word_dict
    
    def is_guess_in_word(self, guess):
        return guess in self._word.strip()

    def get_word_dict(self):
        return self._word_dict
    
    def get_state(self):
        return self._state
    
    def update_state(self, guess):
        word_dict = self.get_word_dict()
        current_state = self.get_state()
        if guess in word_dict.keys():
            idx_to_update = word_dict[guess]
            for idx in idx_to_update:
                current_state[idx] = guess
        self._state = current_state
        return self._state

    def print_board(self, guess):
        return ''.join(self.update_state(guess))

