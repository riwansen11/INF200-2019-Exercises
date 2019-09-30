def bubble_sort(tuple_data):
    """
    :param tuple_data:
    - Write code for the bubble sort function;
    - The function shall not modify the list or tuple passed to it.
    :return:
    - A new list with the data in sorted order.
    """
    list_d = list(tuple_data)
    for pass_left in range(len(list_d) - 1, 0, -1):
        for i in range(pass_left):
            if list_d[i] > list_d[i + 1]:
                list_d[i], list_d[i + 1] = list_d[i + 1], list_d[i]
    return list_d


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
