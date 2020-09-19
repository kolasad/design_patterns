def check_name(name, sentence):
    if name in sentence:
        return True
    return False


def get_name(sentence):
    """
    Outputs first name found in sentence
    :param sentence: description with name
    :return: first first name found in sentence
    """
    if check_name('Jan', sentence):
        return 'Jan'
    elif check_name('Marcin', sentence):
        return 'Marcin'


def check_if_name_in_sentence(sentence):
    result = check_name('Jan', sentence)
    if result:
        return result

    return check_name('Marcin', sentence)


print(get_name('Dominik ma kota'))

assert check_if_name_in_sentence('Dominik ma kota') is False
assert check_if_name_in_sentence('Jan ma kota') is True
assert check_if_name_in_sentence('Marcin ma kota') is True
