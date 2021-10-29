def partition(start, end, array):
    pivot_index = start 
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end

def quick_sort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
          

def consecutiveRanges(a, n):
 
    length = 1
    largest_array = []
    if (n == 0 or n ==1 ):
        return list

    for i in range (1, n + 1):
        if (i == n or a[i] -
            a[i - 1] != 1):
            if len(largest_array)==0:
                largest_array.append(a[i-length]) 
                largest_array.append(a[i-1])           
            elif (a[i-1] - a[i-length]  > largest_array[1] - largest_array[0]): 
                largest_array[0] = a[i-length]
                largest_array[1] = a[i-1]
            length = 1
        else:
            length += 1
    return largest_array

if __name__ == "__main__":
    array = [1, 11, 3, 0, 15, 5, 5, 2, 4, 10, 7, 12, 6]
    quick_sort(0, len(array) - 1, array)
    array = list(set(array))
    print(f'Sorted array: {array}')
    n = len(array)
    print (n)
    return_array = consecutiveRanges(array, n)
    print (return_array)
    
