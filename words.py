def print_upper_words(words):
    """
    function will return a list of capitalized words from a list entered by the user
    """

    for word in words:
        print(word.upper()):

def print_upper_words2(words):

    """
    Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """
    function will return the list of words that begin with the corresponding value

    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter)
            print(word.upper())
            break


    
    
