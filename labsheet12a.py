# find the minimum element from unsorted array
# def find_min(arr):
#     if not arr:  
#         return None
#     minimum = arr[0]
#     for num in arr:
#         if num < minimum:
#             minimum = num
#     return minimum
# n = int(input("Enter the number of elements: "))
# arr = []

# print("Enter the elements:")
# for i in range(n):
#     element = int(input())
#     arr.append(element)

# print("Your array:", arr)
# print("Minimum element:", find_min(arr))


n=int(input())

arr= list(map(int, input().split()))

minimun = arr[0]

for x in arr:
    if x<minimun:
        minimun = x
print(minimun)