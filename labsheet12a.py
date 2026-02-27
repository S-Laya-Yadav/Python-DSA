# find the minimum element from unsorted array
def find_min(arr):
    if not arr:  
        return None
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

print("Your array:", arr)
print("Minimum element:", find_min(arr))
