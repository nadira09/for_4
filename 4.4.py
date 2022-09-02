# задача 4

list_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def my_func(list_2, index):
    if index == 0:
        return True

    for i in range(len(list_2)):
        if i == index:
            return True
        if list_2[i] == list_2[index]:
            return False

    return True

result_2 = [list_2[index] for index in range(len(list_2)) if my_func(list_2, index)]

print(result_2)
