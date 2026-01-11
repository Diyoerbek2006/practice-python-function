def count_characters(text: str) -> int:
    return len(text)
def count_vowels(text: str) -> int:
    i = 0
    unlilar = ['a', 'e', 'o', 'u', 'i']
    for harf in text:
        if harf.lower() in unlilar:
            i += 1
        return i
def is_palindrome(text: str) -> bool:
    a = text.lower()
    if a[::-1] == a:
        return True
    else:
        return False
