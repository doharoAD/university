# Бинарный поиск(двоичный поиск)
# Суть: Список изначально обязательно должен быть отсортирован.
# Пример работы: телефонный справочник - мы ищем по названию и тд.

nums = [5, 7, 6, 9, 8, 4, 2, 3, 1]
nums.sort() # сортируем список
print(nums)

search_for = 9 #что ищем
lowest = 0
highest = len(nums) - 1
index = None #будущий индекс искомого элемента

while(lowest <= highest) and (index is None):
    # повторяем пока не найдено

    mid = (lowest + highest) // 2 # середина
    if nums[mid] == search_for:
        # нашли по середине

        index = mid
    else:
        if search_for < nums[mid]:
            # ищем в левой части списка(разреза)
            highest = mid-1
        else:
            #ищем в правой части списка(разреза)
            lowest = mid + 1
print("Искомый элемент ", search_for, " находится под индексом: ", index)