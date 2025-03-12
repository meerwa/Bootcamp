def create_letter_index_dict(word):
    letter_dict = {}
    for index, letter in enumerate(word):
        if letter in letter_dict:
            letter_dict[letter].append(index)
        else:
            letter_dict[letter] = [index]
    return letter_dict

user_word = input("Enter a word: ").strip()
print(create_letter_index_dict(user_word))
