n = int(input())
lengths = list(map(int, input().split()))
speeds = list(map(int, input().split()))

left = 0
right = n - 1

time_left = lengths[left] / speeds[left]
time_right = lengths[right] / speeds[right]

max_time = max(time_left, time_right)

for i in range(1, n-1):
    t = lengths[i] / speeds[i]
    max_time = max(max_time, t)

print(int(max_time))
