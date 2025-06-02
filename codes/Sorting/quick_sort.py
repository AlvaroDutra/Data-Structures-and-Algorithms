def quick_sort(arr, left, right):
    if left < right:
        print(arr[left:right + 1])
        pi = partition(arr, left, right)
        quick_sort(arr, left, pi - 1)
        quick_sort(arr, pi + 1, right)

def partition(arr, left, right):
    sub_arr = arr[left:right]
    pivot = arr[right]

    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    
    return i + 1    


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)

# Time complexity: 
#   -Best and Avg: O(n log n)
#   -Worst: O(n^2)
# Space complexity: 
#   -Best and Avg: O(log n)
#   -Worst: O(n)