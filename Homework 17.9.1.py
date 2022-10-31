a = list(str.split(input('Enter the array ')))
array = []
for i in a:
    array.append(int(i))
print(array)
element = int(input('Enter the number '))
left = 0
right = len(array) - 1


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1 if middle != 0 else 'No number fits the requirements'

    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


print(merge_sort(array))


def shiftcompare(element):

    if element in array:
        return binary_search(merge_sort(array), element, left, right)
    else:
        if element > merge_sort(array)[right]:
            return "No number fits the requirements"
        else:
            return shiftcompare(element + 1)


print(shiftcompare(element))