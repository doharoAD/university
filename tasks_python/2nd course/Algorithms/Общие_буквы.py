def group_words(list_wordss):
    new_dict = {}

    for word in list_wordss:
        sorted_word = sorted(word)
        sorted_word = ''.join(sorted_word)

        if sorted_word not in new_dict.keys():
            new_dict[sorted_word] = []

        new_dict[sorted_word].append(word)
    return new_dict


list_words = input().split()  # ввод списка с клавиатуры
print(group_words(list_words))
