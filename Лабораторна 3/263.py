n = int(input())  # кількість днів
min_temp = 1000   # початкове велике число

for i in range(n):
    t = int(input())
    if t < min_temp:
        min_temp = t

print(min_temp)
if min_temp < -15:
    print("Yes")
else:
    print("No")