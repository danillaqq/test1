s = input()
t = input()

pos = []
for i in range(len(s) - len(t) + 1):
    if s[i:i+len(t)] == t:
        pos.append(i)

if pos:
    print(*pos)
else:
    print(-1)