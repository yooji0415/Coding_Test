import sys


n = int(sys.stdin.readline().strip())
seq = [int(x) for x in sys.stdin.readline().split()]

k = -1
m = -1
for i in range(len(seq) - 1):
    if seq[i] > seq[i + 1]:
        k = i

if k == -1:
    print(-1)
else:
    for j in range(k + 1, len(seq)):
        if seq[j] < seq[k]:
            m = j

    seq[k], seq[m] = seq[m], seq[k]
    temp = seq[k + 1:]
    temp.sort(reverse=True)
    answer = seq[:k + 1] + temp

    for num in answer:
        print(num, end=" ")
