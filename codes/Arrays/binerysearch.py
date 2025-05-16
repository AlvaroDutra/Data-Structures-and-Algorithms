def b_search(arr, target,l=0,r=None):
    if r is None:
        r = len(arr) 
    
    while l < r:
        middle = int((l + r) /2)
        
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            l = middle + 1
        else:
            r = middle
    return -1
        


#a = [1,2,3,4,5]
#b = [1,2,3,4,5,6,7,8,9,10]
#c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

#target = 5

#print(b_search(a,target))
#print(b_search(b,target))
#print(b_search(c,target))
#print(b_search(d,target))
