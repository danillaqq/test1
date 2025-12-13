def count_repeats(sequence):
    nums = sequence.split(",")
    nums = [n.strip() for n in nums]
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    result = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return result
s = input("Введіть послідовність через кому: ")
print(count_repeats(s))