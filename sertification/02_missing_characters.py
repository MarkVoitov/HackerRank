def missingCharacters(s):
    digits = set('0123456789')
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sorted_digits = sorted(digits - set(s))
    sorted_alphabet = sorted(alphabet - set(s))
    return ''.join(sorted_digits + sorted_alphabet)
