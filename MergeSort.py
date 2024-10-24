from xml.dom.minicompat import defproperty


def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    right_half = l[mid:]
    left_half = l[:mid]

    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)

    return merge(left_half_sorted, right_half_sorted)


def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

l = [4, 5, 1, 2, 8, 6, 0, 10]
print(merge_sort(l))