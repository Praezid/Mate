def remove_vowels(document: str) -> str:
    # write your code here
    char_to_remove = ['a', 'e', 'i', 'o', 'u', 'y' ]
    new_doc = document
    for char in char_to_remove:
        new_doc = new_doc.replace(char, '').replace(char.upper(), '')
    return new_doc
