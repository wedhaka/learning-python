"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.
    Parameters:
        word (str): The root word.
    Returns:
        str: Root word prepended with 'un'.
    """
    return "un" + word

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.
    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.
    Returns:
        str: Prefix followed by vocabulary words with prefix applied.
    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and th['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
                  'echolalia', 'encoder', 'biography']e words with prefix applied, separated by ' :: '.
    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.
    """
    new_list = ""
    prefix = ""
    for word in vocab_words : 
        if len(prefix) == 0 :
            new_list = new_list + word
            prefix = prefix + word
        else :
            new_list = new_list + " :: " + prefix + word

    return new_list
    

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """
    
    modified_word = word.removesuffix("ness")

    if modified_word[-1] == "i" :
        return modified_word[:-1] + "y"

    return modified_word
    # pass


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """
    array_sentence = sentence.split()

    if array_sentence[index][-1] == "." :
        return array_sentence[index][:-1] + "en"

    return array_sentence[index] + 'en'
    

print(adjective_to_verb("His expression went dark.", -1))