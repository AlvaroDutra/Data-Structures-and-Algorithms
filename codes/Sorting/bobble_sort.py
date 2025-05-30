def bubble(list):
    size = len(list)

    for _ in list:
        is_sorted = True
        print(list)
        for i in range(size - 1):
            if list[i] > list[i +1]:
                is_sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]
        if is_sorted:
                return

bubble([1,2,3,4,5,6,7,8,9,10])

# Time complexity: 
#  - Best: O(n)
#  - Worst: O(n^2)
# Space complexity: O(1)