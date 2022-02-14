import sys

n = int(sys.stdin.readline())
meetings = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    m = [s, e]
    meetings.append(m)

meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

end_time = 0
cnt = 0
for i in range(n):
    if end_time <= meetings[i][0]:
        cnt += 1
        end_time = meetings[i][1]

print(cnt)