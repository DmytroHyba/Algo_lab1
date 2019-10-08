from time import time

selection_swaps = 0
selection_comparisons = 0

merge_swaps = 0
merge_comparisons = 0


class Helicopter:
    def __init__(self, name, max_lifting_weight, max_height):
        self.name = name
        self.max_lifting_weight = max_lifting_weight
        self.max_height = max_height

    def __repr__(self): return "\n name: " + str(self.name) + "  max_lifting_height: " + str(
        self.max_lifting_weight) + "  max_height: " + str(self.max_height) + "\n"


def selection_sort(array):
    global selection_swaps
    global selection_comparisons
    length = len(array)
    for i in range(length):     # проходимо усі елементи масиву
        low_idx = i             # знаходимо мінімальний елемент який залишився у не сортовануму масиві
        for j in range(i + 1, length):
            selection_comparisons += 1
            if array[j].max_height < array[low_idx].max_height:
                low_idx = j
        array[i], array[low_idx] = array[low_idx], array[i]    # заміна знайденого найменшого елемнта на перший елемент
        selection_swaps += 1
    return array


def merge_sort(array):
    global merge_swaps
    global merge_comparisons
    length = len(array)
    if length <= 1:
        return array
    result = []
    mid = int(length / 2)  # Заміщення середини масиву
    left_half = merge_sort(array[:mid])    # розділення елементів масиву
    right_half = merge_sort(array[mid:])   # розділення на 2-гу половину
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):  # копіюєм дані в тимчасові масиви L [] та R []
        merge_comparisons += 1
        if left_half[left_index].max_lifting_weight > right_half[right_index].max_lifting_weight:
            merge_comparisons += 1
            merge_swaps += 1
            result.append(left_half[left_index])
            left_index += 1
        else:
            merge_comparisons += 1
            merge_swaps += 1
            result.append(right_half[right_index])
            right_index += 1

    result += left_half[left_index:]
    result += right_half[right_index:]

    return result


s1 = Helicopter("Sikorsky_S-62", 6350, 3300)
s2 = Helicopter("Mil-8MT", 5800, 3200)
s3 = Helicopter("Mil_V-12", 35900, 3500)
s4 = Helicopter("Bell_206_Jetranger", 2018, 3050)
s5 = Helicopter("Boeing_CH-47_Chinook", 24494, 3900)

helicopter_array = [s1, s2, s3, s4, s5]


print("Seletcion Sort:\n")
start = time()
print(selection_sort(helicopter_array))
end = time()
comp_time = end - start
print("\nComparisons: " + str(selection_comparisons) +
      "\nSwaps: " + str(selection_swaps))
print("\nCompilation time: %.20f" % comp_time)


print("\n\nMerge Sort:\n")
start = time()
print(merge_sort(helicopter_array))
end = time()
comp_time = end - start
print("\nComparisons: " + str(merge_comparisons) +
      "\nSwaps: " + str(merge_swaps))
print("\nCompilation time: %.20f" % comp_time)