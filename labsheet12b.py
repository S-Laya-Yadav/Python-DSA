n=int(input())
speed = list(map(int, input().split()))
distance= int(input())

minimun = speed[0]

for x in speed:
    if x<minimun:
        minimun = x
time = distance/minimun

print(f"Maximum Time = {time:.2f} hours")