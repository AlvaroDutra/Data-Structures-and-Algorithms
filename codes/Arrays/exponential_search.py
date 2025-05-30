from codes.Arrays.binery_search import b_search

def e_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    r = 1

    while r < n and arr[r] < target:
        r*=2
    
    if arr[r] == target:
        return r

    return b_search(arr, target,r//2, min(r,n-1))


d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

target = 25

res = e_search(d,target)

print(f'element found at index {res}')
        
    