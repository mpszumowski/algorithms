def swap(list, first_index, second_index):
    temp = list[first_index]
    list[first_index] = list[second_index]
    list[second_index] = temp


def index_of_minimum(list, start_index):
    min_value = list[start_index]
    min_index = start_index
    for i in range(start_index, len(list)):
        if list[i] < min_value:
            min_index = i
            min_value = list[i]

    return min_index


def selection_sort(list):
    minimum = 0
    for index in range(len(list) - 1):
        minimum = index_of_minimum(list, index)
        swap(list, index, minimum)
        print(list)


ex = [22, 11, 99, 88, 7, 42, 100, 8]
selection_sort(ex)
print("List after sorting:  " + str(ex))