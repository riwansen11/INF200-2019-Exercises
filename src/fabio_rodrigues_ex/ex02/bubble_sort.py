def bubble_sort(tuple_data):
    list_data = list(tuple_data)
    for pass_left in range(len(list_data) - 1, 0, -1):
        for i in range(pass_left):
            if list_data[i] > list_data[i + 1]:
                list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
    return list_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
