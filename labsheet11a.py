#first line integer N (number of products)
n=int(input())
prices=list(map(int, input().split()))
# qty=list(map(int, input().split()))

total=0
for p in prices:
    print(p, end=" ")
    total += p

print()
print("total price =", total)
# print(*prices)

# print(sum(prices))

