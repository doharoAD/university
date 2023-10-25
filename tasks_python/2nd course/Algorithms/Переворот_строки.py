# Переворот_строки
# Суть: поменять символы в строке местами, 1й с последним, 2й с предпоследним и так далее,
# пока не дойдет до середины

some_string = "Ghost Show"


def reverse_string(s):
    chars = list(s)  # разбиваем строку на символы

    for i in range(len(s) // 2):
        # до середины
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp
    return ''.join(chars)


print("Что было:", some_string)
print("Что стало:", reverse_string(some_string))
print("Оператор среза в Python, быстрее и легче: ", some_string[:: - 1]) # самый быстрый и легкий способ в python
