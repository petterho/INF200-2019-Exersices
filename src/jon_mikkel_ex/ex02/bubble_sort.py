def bubble_sort(list_for_sorting):
    sorted_list = list(list_for_sorting)
    number_of_rounds = len(data) - 1
    for rounds in range(number_of_rounds):
        for remaining in range(number_of_rounds - rounds):
            if sorted_list[remaining] > sorted_list[remaining+1]:
                sorted_list[remaining], sorted_list[remaining + 1] = sorted_list[remaining + 1], sorted_list[remaining]

    return sorted_list


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
