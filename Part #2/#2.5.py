list = [12,234,12,42,1,432,12,121,1,234,0,123,444,1]
sorted_list = sorted(list)              # сортируем список
min_num = sorted_list[0]                # нашли минимальное
max_num = sorted_list[len(list)-1]      # нашли максимальное
min_index = list.index(min_num)                # сохранили индекс минимального
max_index = list.index(max_num)                # сохранили индекс максимального
list.remove(min_num)
list.remove(max_num)
list.insert(min_index, max_num)
list.insert(max_index, min_num)

print(list)

