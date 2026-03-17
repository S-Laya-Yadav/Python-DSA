n = int(input("Enter the n value: "))
arr = list(map(int, input("Enter n integers: ").split()))

left, right = 0, len(arr) - 1

while left <= right:
    if left == right:
        print(arr[left], end=" ")
    else:
        print(arr[left], arr[right], end=" ")
    right -= 1
