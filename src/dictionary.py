import enchant

dictionary = enchant.Dict("en_GB")


def is_valid_word(word: str):
    return dictionary.check(word) and len(word) >= 3


def any_words_begin_with(string: str):
    return any(
        word.startswith(string)
        for word in dictionary.suggest(string)
    )
