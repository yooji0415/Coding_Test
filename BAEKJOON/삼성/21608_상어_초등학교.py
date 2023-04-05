n = int(input())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

students = [[0] * n for _ in range(n)]
likes_dict = {}
for _ in range(n ** 2):
    student_num, num1, num2, num3, num4 = map(int, input().split())
    likes = {num1, num2, num3, num4}
    likes_dict[student_num] = likes
    most_like_cnt = -1
    most_empty_cnt = -1

    pos = [0, 0]
    for x in range(n):
        for y in range(n):
            like_cnt = 0
            empty_cnt = 0
            if students[x][y] != 0:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if students[nx][ny] == 0:
                    empty_cnt += 1
                elif students[nx][ny] in likes:
                    like_cnt += 1
            if most_like_cnt < like_cnt:
                most_like_cnt = like_cnt
                most_empty_cnt = empty_cnt
                pos = [x, y]
            elif most_like_cnt == like_cnt and most_empty_cnt < empty_cnt:
                most_empty_cnt = empty_cnt
                pos = [x, y]
    students[pos[0]][pos[1]] = student_num

answer = 0
for x in range(n):
    for y in range(n):
        likes = likes_dict[students[x][y]]
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if students[nx][ny] in likes:
                cnt += 1
        if cnt <= 1:
            answer += cnt
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        else:
            answer += 1000

print(answer)
