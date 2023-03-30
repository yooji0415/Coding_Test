n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
idx = 0

while idx < n and k > 0:
    if a[idx] < b[idx]:
        a[idx], b[idx] = b[idx], a[idx]
        idx += 1
        k -= 1
        continue
    break

print(a)
print(b)
print(sum(a))
