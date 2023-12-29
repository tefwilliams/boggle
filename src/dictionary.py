import enchant


class Dictionary:
    def __init__(self, language_tag: str) -> None:
        self.__lookup = enchant.Dict(language_tag)

    def is_valid_word(self, word: str):
        '''
        Checks that the word exists in the dictionary and that it
        is valid for Boggle (at least three letters).
        '''
        return self.__lookup.check(word) and len(word) >= 3

    def any_words_begin_with(self, string: str):
        '''
        Checks if any words in the dictionary begin with the
        provided string.
        '''
        return any(
            word.startswith(string)
            for word in self.__lookup.suggest(string)
        )
